import tkinter as tk
from tkinter import messagebox
from spotifyPlaylistGenerator import spotify_playlist

def submit_data():
    # Get data; verify format and constraints
    prompt = prompt_entry.get()
    
    if not prompt:
        messagebox.showerror("Missing Input", "Please enter a song prompt!")
        return
    
    try:
        song_count = int(song_count_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Song count must be an integer!")
        return
    
    if song_count not in set(range(1,51)):
        messagebox.showerror("Invalid Input", "Song count must between 1 and 50!")
        return
    
    # Create spotify playlist
    if not spotify_playlist(prompt, song_count):
        messagebox.showerror("Error", "An error occurred, please try again!")
        return
    
    messagebox.showinfo("Message", "Playlist created successfully!")


# Initialize the Tkinter window
root = tk.Tk()
root.resizable(False, False)
root.title("Spotify Playlist Generator")

# Create and place labels and entry fields
tk.Label(root, text="What songs do you want?").grid(row=0, column=0, padx=10, pady=10)
prompt_entry = tk.Entry(root, width=40)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="How many songs?").grid(row=1, column=0, padx=10, pady=10)
song_count_entry = tk.Entry(root, width=10)
song_count_entry.grid(row=1, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Generate Playlist", command=submit_data)
submit_button.grid(row=2, column=1, padx=10, pady=10)

# Start the Tkinter loop
root.mainloop()