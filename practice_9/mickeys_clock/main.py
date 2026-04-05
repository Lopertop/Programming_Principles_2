import pygame
from clock import MickeysClock

pygame.init()

WIDTH, HEIGHT = 800, 800
FPS = 60
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickeey's Clock")
clock = pygame.time.Clock()

def main():
    mickeys_clock = MickeysClock(WIDTH // 2, HEIGHT // 2)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        mickeys_clock.update_time()
    
        screen.fill(WHITE)
        mickeys_clock.draw(screen)
    
        pygame.display.flip()
        clock.tick(FPS)    
    
    pygame.quit()
        
if __name__ == "__main__":
    main()    
