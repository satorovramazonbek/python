import tkinter as tk
import pygame
import os

# Initialize pygame
pygame.init()

# List of music files
playlist = ['music.mp3', 'ding.mp3', 'button.wav']  # Add the paths to your music files here
current_music_index = 0

# Function to start playing music
def play_music():
    if playlist:
        pygame.mixer.music.load(playlist[current_music_index])
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Set an event for when the music ends

# Function to handle music playback
def next_song():
    global current_music_index
    if playlist:
        current_music_index = (current_music_index + 1) % len(playlist)
        play_music()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to pause or unpause music
def pause_music():
    if pygame.mixer.music.get_busy():
        if pygame.mixer.music.get_pos() != -1:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

# Start playing the first song
play_music()

# Main application
def main():
    window = tk.Tk()
    window.title("Music Player")

    # Buttons
    play_button = tk.Button(window, text="Play", command=play_music)
    play_button.pack(pady=10)

    next_button = tk.Button(window, text="Next", command=next_song)
    next_button.pack(pady=10)

    stop_button = tk.Button(window, text="Stop", command=stop_music)
    stop_button.pack(pady=10)

    pause_button = tk.Button(window, text="Pause/Unpause", command=pause_music)
    pause_button.pack(pady=10)

    # Volume control slider
    def set_volume(volume):
        pygame.mixer.music.set_volume(float(volume) / 100)

    volume_scale = tk.Scale(window, from_=100, to=0, orient="vertical", command=set_volume, label="Volume")
    volume_scale.set(50)  # Set initial volume to 50%
    volume_scale.pack(pady=10)

    # Main loop to check for pygame events
    def check_music_end():
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:  # Music finished playing
                next_song()
        window.after(100, check_music_end)

    check_music_end()
    window.mainloop()

if __name__ == "__main__":
    main()

# Quit pygame properly
pygame.quit()
