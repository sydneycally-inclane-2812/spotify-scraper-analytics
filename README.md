# Spotify Scraper
A web application that allows for Spotify listening data extraction for deepeer analysis.
Since Spotify only allows the last 50 songs to be extracted from its API, this script will routinely call the API to retrieve your listening history and save it to a PostgreSQL database.

This project will not go to production for the foreseeable future - major focus is on data extraction and analysis.

# Project Structure:
|___ README.md
|___ .gitignore
|___ auth_test: code for testing the Spotipy library for navigating the OAuth process to authenticate with Spotify
|   |___ test_auth.ipynb: original testing notebook
|   |___ working_auth.py: polished single Python script for the authentication process

    