from flask import Flask, request, redirect, session, url_for, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Spotify OAuth Configuration
SPOTIPY_CLIENT_ID = os.getenv('CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8239/callback'
SCOPE = 'user-read-recently-played'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Create SpotifyOAuth instance
    sp_oauth = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE
    )
    # Get the authorization URL
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/callback')
def callback():
    # Handle the callback from Spotify
    sp_oauth = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE
    )
    
    # Get the access token
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    
    # Store token info in session
    session['token_info'] = token_info
    
    return redirect(url_for('get_history'))

@app.route('/history')
def get_history():
    if 'token_info' not in session:
        return redirect(url_for('login'))
    
    # Create Spotify client
    sp = spotipy.Spotify(auth=session['token_info']['access_token'])
    
    try:
        # Get user's recently played tracks
        results = sp.current_user_recently_played(limit=50)
        return render_template('history.html', tracks=results['items'])
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, port=8239)