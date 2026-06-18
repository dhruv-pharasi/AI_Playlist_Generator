"""
AI Playlist Generator - Frontend Module

This module provides the user interface for the AI Playlist Generator application.
It uses Tkinter to create a simple GUI with input fields for:
  - A natural language prompt describing the desired songs (e.g., "party music")
  - The number of songs to generate (1-50)

When the user clicks "Generate Playlist", the module validates inputs and calls
the spotify_playlist() function to create a Spotify playlist with AI-recommended songs.
"""

import tkinter as tk
from tkinter import messagebox
from spotifyPlaylistGenerator import spotify_playlist


def submit_data():
    """
    Handle the "Generate Playlist" button click event.

    This function:
    1. Retrieves and validates user inputs (prompt and song count)
    2. Calls spotify_playlist() to generate and create the playlist
    3. Displays appropriate success or error messages to the user

    Validation rules:
    - Prompt: must not be empty
    - Song count: must be a valid integer between 1 and 50
    """
    # Retrieve the song prompt from the text entry field
    prompt = prompt_entry.get()

    # Validate that the prompt is not empty
    if not prompt:
        messagebox.showerror("Missing Input", "Please enter a song prompt!")
        return

    # Attempt to convert the song count input to an integer
    try:
        song_count = int(song_count_entry.get())
    except ValueError:
        # Display error if the input is not a valid integer
        messagebox.showerror("Invalid Input", "Song count must be an integer!")
        return

    # Validate that the song count is within the acceptable range (1-50)
    if song_count not in set(range(1, 51)):
        messagebox.showerror("Invalid Input", "Song count must between 1 and 50!")
        return

    # Attempt to create the Spotify playlist with the validated inputs
    # spotify_playlist() returns True on success, False on failure
    if not spotify_playlist(prompt, song_count):
        messagebox.showerror("Error", "An error occurred, please try again!")
        return

    # Notify user that the playlist was successfully created
    messagebox.showinfo("Message", "Playlist created successfully!")


# ============================================================================
# GUI WINDOW SETUP
# ============================================================================

# Create the main Tkinter window
root = tk.Tk()

# Prevent users from resizing the window (maintains consistent layout)
root.resizable(False, False)

# Set the title displayed in the window's title bar
root.title("Spotify Playlist Generator")

# ============================================================================
# INPUT FIELDS AND LABELS
# ============================================================================

# Label and text entry field for the song prompt (row 0, column 0)
# The prompt describes what type of songs the user wants
tk.Label(root, text="What songs do you want?").grid(row=0, column=0, padx=10, pady=10)
prompt_entry = tk.Entry(root, width=40)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

# Label and numeric entry field for the number of songs (row 1, column 0)
# Users can request between 1 and 50 songs
tk.Label(root, text="How many songs?").grid(row=1, column=0, padx=10, pady=10)
song_count_entry = tk.Entry(root, width=10)
song_count_entry.grid(row=1, column=1, padx=10, pady=10)

# ============================================================================
# SUBMIT BUTTON
# ============================================================================

# Button that triggers the submit_data() function when clicked
# This button initiates the playlist generation process
submit_button = tk.Button(root, text="Generate Playlist", command=submit_data)
submit_button.grid(row=2, column=1, padx=10, pady=10)

# ============================================================================
# MAIN APPLICATION LOOP
# ============================================================================

# Start the Tkinter event loop, which keeps the window open and responsive
# to user interactions (button clicks, text input, etc.)
root.mainloop()