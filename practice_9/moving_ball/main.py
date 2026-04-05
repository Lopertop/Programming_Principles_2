import pygame
from ball import Ball

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Moving Ball")
    clock = pygame.time.Clock()
    
    WHITE = (255, 255, 255)
    FPS = 60
    
    ball = Ball(400, 400, (255, 0, 0))
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ball.x - ball.radius > 0:
            ball.x -= ball.speed_x
        if keys[pygame.K_RIGHT] and ball.x + ball.radius < 800:
            ball.x += ball.speed_x
        if keys[pygame.K_UP] and ball.y - ball.radius > 0:
            ball.y -= ball.speed_y
        if keys[pygame.K_DOWN] and ball.y + ball.radius < 600:
            ball.y += ball.speed_y
        
        screen.fill(WHITE)
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
        
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()