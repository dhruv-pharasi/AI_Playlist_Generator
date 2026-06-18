# AI Playlist Generator

An intelligent application that uses **OpenAI's GPT-4o-mini** to generate personalized song recommendations and automatically creates **Spotify playlists** based on your preferences.

Simply describe the type of songs you want, specify how many tracks you'd like, and the app will generate AI recommendations and create a private Spotify playlist for you.

## Features

- 🎵 **AI-powered recommendations** – Uses OpenAI's GPT-4o-mini to understand and match your music preferences
- 🎯 **Natural language prompts** – Describe the playlist mood/theme in your own words (e.g., "upbeat party music", "sad indie songs", "study beats")
- 📊 **Flexible song counts** – Generate playlists with 1-50 songs
- 🔒 **Private playlists** – Created playlists are private by default
- 🎨 **Simple GUI** – User-friendly Tkinter interface for easy interaction
- ✅ **Spotify integration** – Automatically searches Spotify and adds real tracks to your playlist

## Prerequisites

You'll need:
- **Python 3.7+** installed on your system
- **OpenAI API key** (free tier available)
- **Spotify Developer account** for client credentials (free)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dhruv-pharasi/AI-Playlist-Generator.git
cd AI-Playlist-Generator
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install openai spotipy python-dotenv
```

## Configuration

### Step 1: Get Your OpenAI API Key

1. Visit https://platform.openai.com/api-keys
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (you won't be able to see it again)

### Step 2: Get Spotify Developer Credentials

1. Go to https://developer.spotify.com/dashboard
2. Sign in or create a free account
3. Click "Create an App" and accept the terms
4. Copy your **Client ID** and **Client Secret**
5. Go to "Edit Settings" and add this **Redirect URI**: `http://localhost:8080`
   - This is critical for authentication to work

### Step 3: Create the `.env` File

In the project root directory, create a file named `.env` with your credentials:

```
API_KEY=your_openai_api_key_here
CLIENT_ID=your_spotify_client_id_here
CLIENT_SECRET=your_spotify_client_secret_here
```

**Example:**
```
API_KEY=sk-proj-abc123xyz789...
CLIENT_ID=a1b2c3d4e5f6g7h8i9j0
CLIENT_SECRET=your_secret_key_here
```

⚠️ **Important:** Never commit the `.env` file to version control. Add it to `.gitignore`.

## Usage

### Running the Application

```bash
python3 frontend.py
```

This opens a simple Tkinter window with two input fields:

1. **"What songs do you want?"** – Describe the playlist theme
   - Examples: "upbeat party music", "peaceful meditation songs", "90s hip hop", "lo-fi study beats"
2. **"How many songs?"** – Enter a number between 1 and 50

3. Click **"Generate Playlist"** to create your playlist

The app will:
- Send your prompt to OpenAI for song recommendations
- Search Spotify for each recommended song
- Create a private playlist with your prompt as the name
- Add all found songs to the playlist

### Success Message

Once complete, you'll see a confirmation message. Check your Spotify account—the new playlist will appear in your library!

## Project Structure

```
AI-Playlist-Generator/
├── frontend.py                    # Tkinter GUI for user input
├── spotifyPlaylistGenerator.py    # Core logic: OpenAI + Spotify integration
├── .env                          # API credentials (create this file)
└── README.md                     # This file
```

### File Descriptions

- **frontend.py** – Simple GUI with input validation
  - Validates prompt (non-empty) and song count (1-50)
  - Calls the playlist generation function
  - Displays success/error messages

- **spotifyPlaylistGenerator.py** – Backend API integration
  - `song_generator()` – Calls OpenAI GPT-4o-mini to generate recommendations
  - `spotify_playlist()` – Authenticates with Spotify, searches for songs, creates playlist

## Troubleshooting

### "Please enter a song prompt!" error
- The prompt field is empty. Describe the type of songs you want (e.g., "party music").

### "Song count must be between 1 and 50!" error
- Enter a whole number between 1 and 50.

### Spotify authentication opens a browser but then fails
- Make sure your **Redirect URI** in Spotify Developer settings is exactly: `http://localhost:8080`
- Check that your **Client ID** and **Client Secret** are correct in the `.env` file

### "An error occurred, please try again!" message
- **Invalid .env file**: Verify API keys are correct and the `.env` file is in the project root
- **API rate limits**: You've exceeded OpenAI or Spotify API limits. Wait a few minutes and try again
- **No songs found**: The songs recommended by AI might not exist on Spotify. Try a different prompt

### Some songs from the recommendation aren't in my playlist
- Spotify's search may not find obscure or misspelled songs. The app adds the first available match for each recommendation
- Try requesting songs that are more popular or well-known

## How It Works

1. **You provide a prompt** → "chill vibes"
2. **OpenAI generates recommendations** → Returns a JSON list of artist/song pairs using few-shot prompting
3. **We search Spotify** → Looks up each song by artist and name
4. **Playlist is created** → Creates a private playlist with your prompt as the name
5. **Tracks are added** → Populates the playlist with found songs

The app uses **few-shot prompting** with OpenAI—providing 2 example prompts/responses to guide the model in generating consistent, high-quality recommendations in the correct JSON format.

## Limitations

- Spotify searches use fuzzy matching, so very obscure songs may not be found
- The app is limited by OpenAI API rate limits (check https://platform.openai.com/account/usage)
- Requires internet connection for both OpenAI and Spotify API calls

## Future Improvements

Potential enhancements:
- Add error retry logic with exponential backoff
- Display a preview of recommended songs before creating the playlist
- Allow customization of playlist visibility (public/private)
- Support for adding songs to existing playlists
- Batch API calls for improved performance

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
- Check the Troubleshooting section above
- Verify your API credentials are correct
- Ensure you have the latest versions of the required packages

Enjoy your AI-generated playlists! 🎵
