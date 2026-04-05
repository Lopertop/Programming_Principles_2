import pygame
import os

class Player:
    def __init__(self, playlist):
        pygame.mixer.init()
        self.playlist = playlist
        self.current_index = 0
        self.is_paused = False
        
    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.is_paused = False
        
    def pause(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.is_paused = not self.is_paused
    
    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_music()
    
    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_music()
    
    def get_current_track(self):
        if self.playlist:
            return os.path.basename(self.playlist[self.current_index])
        return "No track available"
    
    def is_finished(self):
        return not pygame.mixer.music.get_busy() and not self.is_paused
