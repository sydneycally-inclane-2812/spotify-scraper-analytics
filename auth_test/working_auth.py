from flask import Flask, request, redirect, session, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIPY_CLIENT_ID  = os.getenv("CLIENT_ID")
SPOTIPY_CLIENT_SECRET  = os.getenv("CLIENT_SECRET")
scope = "user-read-recently-played"
REDIRECT_URI = "http://127.0.0.1:8239/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=REDIRECT_URI))
results = sp.current_user_recently_played(limit=1)

print(results)