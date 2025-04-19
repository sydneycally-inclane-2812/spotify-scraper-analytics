# Spotify Scraper
A web application that allows for Spotify listening data extraction for deepeer analysis.
Since Spotify only allows the last 50 songs to be extracted from its API, this script will routinely call the API to retrieve your listening history and save it to a PostgreSQL database.

This project will not go to production for the foreseeable future - major focus is on data extraction and analysis.

# Project Structure:

```
spotify-history-grabber/
├── README.md
├── .gitignore
└── auth_test/
    ├── test_auth.ipynb
    └── working_auth.py
```

### Directory Details

- `README.md` - Main documentation file
- `.gitignore` - Specifies which files Git should ignore
- `auth_test/` - Authentication testing directory
  - `test_auth.ipynb` - Initial Spotipy authentication testing notebook
  - `working_auth.py` - Refined authentication implementation script

    