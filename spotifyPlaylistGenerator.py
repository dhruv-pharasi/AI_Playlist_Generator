"""
IMPORTANT:

- Lines 14 and 15: replace with your own OpenAI API key
- Line 59: replace with your own Spotify client ID
- Line 60: replace with your own Spofify secret key
"""


import openai, spotipy, json
from dotenv import dotenv_values


config = dotenv_values(".env")
openai.api_key = config["API_KEY"]


def song_generator(prompt: str, num_songs):

    system_prompt = """
    You are a music recommendation expert specializing in curating Spotify playlists. 
    Given a sentence describing the type of songs needed (e.g., 'songs for a party' or 'songs for a night drive'), 
    provide a list of songs that match the mood, theme, or occasion. 
    Each list should contain a mix of genres, moods, and tempos to keep it varied and interesting, while staying true to the theme. 
    Ensure that the recommendations are diverse, popular, and suitable for the given context.

    Return the response as a JSON array of key-value pairs, where the keys are artist name and song name.
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role" : "system", "content" : system_prompt},
            {"role" : "user", "content" : "Generate of playlist of 5 songs based on this prompt: hindi peaceful songs"},
            {"role" : "assistant", "content" : """[ {"artist": "Arijit Singh", "song": "Tum Hi Ho"}, {"artist": "A. R. Rahman", "song": "Dil Se Re"}, {"artist": "Lata Mangeshkar", "song": "Tujhe Kitna Chahne Lage"}, {"artist": "Mohit Chauhan", "song": "Pee Loon"}, {"artist": "Sonu Nigam", "song": "Kal Ho Naa Ho"} ]"""},
            {"role" : "user", "content" : "Generate of playlist of 4 songs based on this prompt: christmas party songs"},
            {"role" : "assistant", "content" : """[ {"artist": "Mariah Carey", "song": "All I Want for Christmas Is You"}, {"artist": "Michael Bublé", "song": "It's Beginning to Look a Lot Like Christmas"}, {"artist": "Wham!", "song": "Last Christmas"}, {"artist": "Justin Bieber", "song": "Mistletoe"} ]"""},
            {"role" : "user", "content" : f"Generate of playlist of {num_songs} songs based on this prompt: {prompt}"}
        ]
    )

    try:
        return json.loads(response.choices[0].message.content)
    except json.decoder.JSONDecodeError:
        print("\nOutput format generated by the ChatGPT API is invalid. Try again!")
        return None

def spotify_playlist(prompt: str, num_songs) -> bool:
    
    # Get songs from the ChatGPT API
    songs = song_generator(prompt, num_songs)
    
    if songs is None:
        return False

    # Establish connection with Spotify's API
    spotify = spotipy.Spotify(
        auth_manager=spotipy.SpotifyOAuth(
            client_id=config["CLIENT_ID"],  # replace
            client_secret=config["CLIENT_SECRET"],  # replace
            redirect_uri="http://localhost:8080",
            scope="playlist-modify-private"
        )
    )

    # Get detailed profile information about the current user
    user = spotify.current_user()

    if not user:
        return False

    track_ids = set()

    # Search for songs on Spotify
    for song in songs:
        search_query = f"{song['song']} {song['artist']}"
        search_results = spotify.search(q=search_query, type="track", limit=10)
        
        for i in range(10):
            id = search_results["tracks"]["items"][i]["id"]
            if id not in track_ids:
                track_ids.add(id)
                break

    # Create Spotify playlist
    playlist = spotify.user_playlist_create(
        user=user["id"],
        name=prompt,
        public=False,
        description="An AI generated playlist. Enjoy!"
    )

    # Add songs to the playlist
    spotify.user_playlist_add_tracks(
        user=user["id"],
        playlist_id=playlist["id"],
        tracks=list(track_ids)
    )

    return True

