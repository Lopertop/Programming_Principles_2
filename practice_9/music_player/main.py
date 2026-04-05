import pygame
import os
from player import Player

pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 30

FOLDER_PATH = "playlist"

def get_playlist(folder):
    if not os.path.exists(folder):
        return []
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.mp3') or f.endswith('.wav')]

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")
    font = pygame.font.SysFont("Arial", 22)
    clock = pygame.time.Clock()
    
    tracks = get_playlist("playlist")
    player = Player(tracks)
    
    if tracks:
        player.play_music()
    
    running = True
    while running:
        screen.fill((20, 20, 20))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player.pause()
                if event.key == pygame.K_n:
                    player.next_track()
                if event.key == pygame.K_b:
                    player.previous_track()
                if event.key == pygame.K_q:
                    running = False
                    
        if player.is_finished():
            player.next_track()
            
        y_offset = 50
        text = [
            f"Now playing... {player.get_current_track()}",
            f"Track: {player.current_index + 1} / {len(player.playlist)}",
            "",
            "Controls: n - next_track | b - previous track | s - pause/unpause track"
        ]
        
        for txt in text:
            text_surf = font.render(txt, True, (255, 255, 255))
            screen.blit(text_surf, (50, y_offset))
            y_offset += 40
                
        pygame.display.update()
        
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == '__main__':
    main()
