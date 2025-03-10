# services/media_player.py
import os
import random
import pygame
from config.settings import Config


class MediaPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.music_dir = Config.MUSIC_DIR

    def play_music(self):
        try:
            songs = [
                song
                for song in os.listdir(self.music_dir)
                if song.endswith((".mp3", ".wav"))
            ]
            if songs:
                song = random.choice(songs)
                song_path = os.path.join(self.music_dir, song)
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
                return f"Playing {song}"
            else:
                return "No music files found in the directory"
        except Exception as e:
            return f"Error playing music: {str(e)}"

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            return "Music stopped"
        return "No music is currently playing"
