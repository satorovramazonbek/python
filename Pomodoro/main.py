# import tkinter as tk
# import math
# import pygame
# import os
# from tkinter import simpledialog
# WORK_MIN=simpledialog.askinteger("Study Time" , "Enter a study time you want in minutes: ")

# image_path = os.path.join(os.path.dirname(__file__), 'tomato.png')
# current_music_index = 0
# # Constants
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None
# paused=False
# paused_time=0

# # Initialize pygame mixer
# pygame.init()



# # ---------------------------- TIMER RESET ------------------------------- #
# def reset_timer():
#     global reps, paused, paused_time
#     reps = 0
#     paused = False
#     paused_time = 0
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text="00:00")
#     title_label.config(text="Timer", fg=GREEN)
#     check_marks.config(text="")
#     play_sound(reset_sound)


# # ---------------------------- TIMER MECHANISM ------------------------------- #
# def start_timer():
#     global reps, paused
#     if not paused:
#         reps += 1

#     work_sec = WORK_MIN * 60
#     short_break_sec = SHORT_BREAK_MIN * 60
#     long_break_sec = LONG_BREAK_MIN * 60

#     if reps % 8 == 0:
#         count_down(long_break_sec)
#         title_label.config(text="Break", fg=RED)
#         play_sound(break_sound)
#     elif reps % 2 == 0:
#         count_down(short_break_sec)
#         title_label.config(text="Break", fg=PINK)
#         play_sound(break_sound)
#     else:
#         count_down(work_sec)
#         title_label.config(text="Study", fg=GREEN)
#         play_sound(study_sound)



# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def count_down(count):
#     global timer, paused, paused_time
#     if paused:
#         paused_time = count
#         return
#     count_min = math.floor(count / 60)
#     count_sec = count % 60
#     if count_sec < 10:
#         count_sec = f"0{count_sec}"
#     canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
#     if count > 0:
#         timer = window.after(1000, count_down, count - 1)
#     else:
#         start_timer()
#         marks = ""
#         work_sessions = math.floor(reps / 2)
#         for _ in range(work_sessions):
#             marks += "✓"
#         check_marks.config(text=marks)


# def pause_resume():
#     global paused
#     if not paused:
#         paused = True
#         pygame.mixer.music.pause()
#     else:
#         paused = False
#         count_down(paused_time)
#         pygame.mixer.music.unpause()
#     play_sound(button_sound)

# # ---------------------------- PLAY SOUND ------------------------------- #


# background_music="perfect_music.mp3"
# playlist = [
#     "ding.mp3",
#     "perfect_music.mp3",
#     "forest_music.mp3",
#     "relaxed_music.mp3",
#     "study_music.mp3",
#     "music.mp3",
#     "Moments.mp3",
#     "Lookingup.mp3",
#     "Evening.mp3",
#     "Arnor.mp3",
#     "Stormy.mp3"
# ]

# def play_sound(sound_file):
#     try:
#         pygame.mixer.music.load(sound_file)
#         pygame.mixer.music.play()
#     except pygame.error as e:
#         print(f"Error playing sound: {e}")

# def play_music():
#     if playlist:
#         pygame.mixer.music.load(playlist[current_music_index])
#         pygame.mixer.music.play()
#         pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Set an event for when the music ends

# # Function to handle music playback
# def next_song():
#     global current_music_index
#     if playlist:
#         current_music_index = (current_music_index + 1) % len(playlist)
#         play_music()

# # # Music background
# # def music():
# #         pygame.mixer.music.load(background_music)
# #         pygame.mixer.music.play(-1)  # Loop the music

# # Function to stop background music
# def music_stop():
#     if pygame.mixer.music.get_busy():  # Check if music is currently playing
#         pygame.mixer.music.pause()  # Pause music if it's playing
#     else:
#         pygame.mixer.music.unpause()  # Resume music if it's paused

# pygame.mixer.music.load(playlist[current_music_index])

# def change_music():
#     global current_music_index
#     current_music_index = (current_music_index + 1) % len(playlist)
#     pygame.mixer.music.load(playlist[current_music_index])
#     pygame.mixer.music.play(-1)


# def set_volume(volume):
#     pygame.mixer.music.set_volume(float(volume) / 100)

# # ---------------------------- UI SETUP ------------------------------- #
# window = tk.Tk()
# window.title("Pomodoro")
# window.config(padx=80, pady=20, bg=YELLOW)
# title_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
# title_label.grid(row=0, column=1, padx=(0, 20))
# canvas = tk.Canvas(width=260, height=230, bg=YELLOW, highlightthickness=0)
# tomato_img = tk.PhotoImage(file="tomato.png")
# canvas.create_image(100, 115, image=tomato_img)
# timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=1)

# start_button = tk.Button(
#     text="Start",
#     command=start_timer,
#     bg="green",   # Background color
#     fg="white",     # Text color
#     font=("Verdana", 12, "bold"),  # Font settings
#     relief=tk.RAISED  
#     )
# start_button.grid(column=0, row=2)

# reset_button = tk.Button(
#     text="Reset", 
#     command= reset_timer,
#     bg="red",   # Background color
#     fg="white",     # Text color
#     font=("Verdana", 12, "bold"),  # Font settings
#     relief=tk.RAISED  
#     )
# reset_button.place(relx=1.1, rely=0.85, anchor='se')

# pause_button = tk.Button(
#     text="Pause/Resume",
#     command=pause_resume,
#     bg="magenta",   # Background color
#     fg="white",     # Text color
#     font=("Verdana", 12, "bold"),  # Font settings
#     relief=tk.RAISED  
#     )
# pause_button.place(relx=0.5, rely=0.85, anchor='s')

# background_music_button=tk.Button(
#     text="Music", 
#     command=play_music,
#     bg="blue",   # Background color
#     fg="white",     # Text color
#     font=("Century Gothic", 12, "bold"),  # Font settings
#     relief=tk.RAISED  
#     )

# background_music_button.grid(row=5, column=0)

# music_stop_button = tk.Button(
#     text="Music Pause/Resume",
#     command=music_stop,
#     width=18,
#     bg="dark violet",   # Background color
#     fg="white",     # Text color
#     font=("Century Gothic", 12, "bold"),  # Font settings
#     relief=tk.RAISED             # Border width
# )
# music_stop_button.place(relx=0.48, rely=1, anchor='s')

# change_music_button = tk.Button(
#     text="Change music",
#     command=change_music,
#     bg="teal",  # Background color
#     fg="white",    # Text color
#     font=("Century Gothic", 12, "bold"),  # Font settings
#     relief=tk.RAISED,  # Border style             # Border width            # Padding in y-direction
# )
# change_music_button.place(relx=1.2, rely=1, anchor='se')


# # Volume control slider
# volume_scale = tk.Scale(
#     window, from_=100, to=0, orient="vertical", command=set_volume, label="Volume", bg=YELLOW, fg="teal",
#     font=(FONT_NAME, 12, "bold"),
#     highlightthickness=0
# )
# volume_scale.set(50)  # Set initial volume to 50%
# volume_scale.place(relx=-0.24, rely=0.48)

# def check_music_end():
#         for event in pygame.event.get():
#             if event.type == pygame.USEREVENT:  # Music finished playing
#                 next_song()
#         window.after(100, check_music_end)

# check_music_end()


# check_marks = tk.Label(font=(FONT_NAME,15, "bold"), fg="green", bg=YELLOW)
# check_marks.grid(column=1, row=4)

# window.mainloop()


import tkinter as tk
import math
import pygame
from tkinter import simpledialog

# Prompt user for study time
WORK_MIN = simpledialog.askinteger("Study Time", "Enter a study time you want in minutes: ")

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
paused = False
paused_time = 0

# Initialize pygame
pygame.init()

# Music playlist and initial index
playlist = [
    "perfect_music.mp3",
    "forest_music.mp3",
    "relaxed_music.mp3",
    "study_music.mp3",
    "music.mp3",
    "Moments.mp3",
    "Lookingup.mp3",
    "Evening.mp3",
    "Arnor.mp3",
    "Stormy.mp3"
]
current_music_index = 0

# # Music sounds
study_sound = "ding.mp3"  
break_sound = "Alarm05.wav" 
reset_sound= "sound.wav"
button_sound="button.wav"

# Function to play sound effects
def play_sound(sound_file):
    try:
        pygame.mixer.Sound(sound_file).play()
    except pygame.error as e:
        print(f"Error playing sound: {e}")

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
def music_stop():
    if pygame.mixer.music.get_busy():  # Check if music is currently playing
        pygame.mixer.music.pause()  # Pause music if it's playing
    else:
        pygame.mixer.music.unpause()  # Resume music if it's paused

# Function to change music
def change_music():
    next_song()

# Function to set music volume
def set_volume(volume):
    pygame.mixer.music.set_volume(float(volume) / 100)

# Timer reset function
def reset_timer():
    global reps, paused, paused_time
    reps = 0
    paused = False
    paused_time = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    play_sound(reset_sound)

# Timer start function
def start_timer():
    global reps, paused
    if not paused:
        reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        play_sound(break_sound)
        music_stop()
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        play_sound(break_sound)
        music_stop()
    else:
        count_down(work_sec)
        title_label.config(text="Study", fg=GREEN)
        play_sound(study_sound)

# Countdown mechanism
def count_down(count):
    global timer, paused, paused_time
    if paused:
        paused_time = count
        return
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# Pause/Resume function
def pause_resume():
    global paused
    if not paused:
        paused = True
        pygame.mixer.music.pause()
    else:
        paused = False
        count_down(paused_time)
        pygame.mixer.music.unpause()
    play_sound(button_sound)

# UI Setup
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=80, pady=20, bg=YELLOW)

title_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1, padx=(0, 20))

canvas = tk.Canvas(width=260, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(
    text="Start",
    command=start_timer,
    bg="green",   # Background color
    fg="white",     # Text color
    font=("Verdana", 12, "bold"),  # Font settings
    relief=tk.RAISED  
)
start_button.grid(column=0, row=2)

reset_button = tk.Button(
    text="Reset", 
    command=reset_timer,
    bg="red",   # Background color
    fg="white",     # Text color
    font=("Verdana", 12, "bold"),  # Font settings
    relief=tk.RAISED  
)
reset_button.place(relx=1.1, rely=0.85, anchor='se')

pause_button = tk.Button(
    text="Pause/Resume",
    command=pause_resume,
    bg="magenta",   # Background color
    fg="white",     # Text color
    font=("Verdana", 12, "bold"),  # Font settings
    relief=tk.RAISED  
)
pause_button.place(relx=0.5, rely=0.85, anchor='s')

background_music_button = tk.Button(
    text="Music", 
    command=play_music,
    bg="blue",   # Background color
    fg="white",     # Text color
    font=("Century Gothic", 12, "bold"),  # Font settings
    relief=tk.RAISED  
)
background_music_button.grid(row=5, column=0)

music_stop_button = tk.Button(
    text="Music Pause/Resume",
    command=music_stop,
    width=18,
    bg="dark violet",   # Background color
    fg="white",     # Text color
    font=("Century Gothic", 12, "bold"),  # Font settings
    relief=tk.RAISED             # Border width
)
music_stop_button.place(relx=0.48, rely=1, anchor='s')

change_music_button = tk.Button(
    text="Change music",
    command=change_music,
    bg="teal",  # Background color
    fg="white",    # Text color
    font=("Century Gothic", 12, "bold"),  # Font settings
    relief=tk.RAISED,  # Border style
)
change_music_button.place(relx=1.2, rely=1, anchor='se')

# Volume control slider
volume_scale = tk.Scale(
    window, from_=100, to=0, orient="vertical", command=set_volume, label="Volume", bg=YELLOW, fg="teal",
    font=(FONT_NAME, 12, "bold"),
    highlightthickness=0
)
volume_scale.set(50)  # Set initial volume to 50%
volume_scale.place(relx=-0.24, rely=0.48)

# Check for music end event
def check_music_end():
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:  # Music finished playing
            next_song()
    window.after(100, check_music_end)

check_music_end()

check_marks = tk.Label(font=(FONT_NAME, 15, "bold"), fg="green", bg=YELLOW)
check_marks.grid(column=1, row=4)

window.mainloop()
