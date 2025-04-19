import os
import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

class SpotifyClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify Clone")
        self.root.geometry("400x300")

        self.song_path = None

        # Buttons
        self.load_button = tk.Button(root, text="Load Song", command=self.load_song)
        self.load_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_song)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_song)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=5)

        self.volume_label = tk.Label(root, text="Volume")
        self.volume_label.pack()

        self.volume_scale = tk.Scale(root, from_=0, to=1, resolution=0.1, orient="horizontal", command=self.set_volume)
        self.volume_scale.set(0.5)  # Default volume
        self.volume_scale.pack()

        self.song_label = tk.Label(root, text="No song loaded", wraplength=300)
        self.song_label.pack(pady=10)

    def load_song(self):
        """Load a song from file dialog"""
        self.song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if self.song_path:
            self.song_label.config(text=os.path.basename(self.song_path))

    def play_song(self):
        """Play the loaded song"""
        if self.song_path:
            pygame.mixer.music.load(self.song_path)
            pygame.mixer.music.play()

    def pause_song(self):
        """Pause the currently playing song"""
        pygame.mixer.music.pause()

    def stop_song(self):
        """Stop the song"""
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        """Adjust volume"""
        pygame.mixer.music.set_volume(float(volume))

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SpotifyClone(root)
    root.mainloop()
