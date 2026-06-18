# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Playlist Generator is a Python application that uses OpenAI's GPT-4o-mini to generate Spotify playlist recommendations based on user input, then creates and populates the playlist on Spotify.

**Architecture**: Two-module design
- **frontend.py**: Tkinter GUI for user input and result display
- **spotifyPlaylistGenerator.py**: Core logic for OpenAI API calls and Spotify Web API integration

## Setup & Configuration

### Dependencies

Install required Python packages:
```bash
pip install openai spotipy python-dotenv
```

### Environment Configuration

Create a `.env` file in the project root with:
```
API_KEY=your_openai_api_key
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
```

**Getting credentials:**
- **OpenAI API Key**: Visit https://platform.openai.com/api-keys
- **Spotify Developer Credentials**: Register at https://developer.spotify.com/dashboard, create an app, and set the redirect URI to `http://localhost:8080` in your app settings

## Running the Application

Start the GUI application:
```bash
python3 frontend.py
```

The application opens a Tkinter window where users:
1. Enter a prompt describing desired songs (e.g., "party music", "study beats")
2. Specify the number of songs (1-50)
3. Click "Generate Playlist" to create and populate a private Spotify playlist

## Key Implementation Details

**Song Generation Flow** (`spotifyPlaylistGenerator.py`):
1. User prompt is sent to OpenAI's gpt-4o-mini with a system prompt instructing it to return song recommendations as JSON
2. The response includes 2 few-shot examples (hindi peaceful songs, christmas party songs) to guide format and quality
3. OpenAI returns a JSON array with artist/song pairs

**Spotify Integration Flow**:
1. Uses Spotipy's SpotifyOAuth for user authentication (requires browser redirect)
2. Searches Spotify for each recommended song by name + artist
3. Creates a private playlist named after the user's prompt
4. Adds the first unique match for each song to the playlist (deduped via set)

**Input Validation** (`frontend.py`):
- Prompt must be non-empty
- Song count must be integer between 1-50
- User-friendly error messages via messagebox

## Common Issues & Debugging

- **Spotify authentication fails**: Ensure `redirect_uri` in app settings matches `http://localhost:8080` and Spotify browser window opens
- **Songs not found on Spotify**: OpenAI might generate obscure tracks; the code gracefully handles by using the first available match in Spotify's top 10 results
- **Invalid JSON from OpenAI**: Error is caught and logged; user is prompted to retry. The few-shot examples should prevent this
- **API rate limits**: Both OpenAI and Spotify have rate limits; consider adding delays between requests if making many playlists

## Files to Modify for Customization

- **frontend.py**: GUI window title, labels, input constraints
- **spotifyPlaylistGenerator.py**: System prompt for recommendations, GPT model selection, Spotify playlist scope/visibility
