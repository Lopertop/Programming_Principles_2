import os
import pygame
import math
from datetime import datetime

class MickeysClock:
    def __init__(self, x, y):
        self.center = (x, y)
        self.radius = 300
        self._image_library = {}
        
        self.size_minute = (250, 180)
        self.size_second = (400, 100)
        
        self.minute_hand = self.load_image_and_scale('images/minute.png', self.size_minute)
        self.second_hand = self.load_image_and_scale('images/second.png', self.size_second)

        self.min_angle = 0
        self.sec_angle = 0

    def load_image_and_scale(self, path, size):
        try:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path).convert_alpha()
            return pygame.transform.smoothscale(image, size)
        except pygame.error as e:
            print(e)
            surf = pygame.Surface(size, pygame.SRCALPHA)
            pygame.draw.rect(surf, (255, 0, 0), surf.get_rect(), 2)
            return surf
    
    def update_time(self):
         now = datetime.now()
         self.sec_angle = -(now.second * 6) + 90
         self.min_angle = -(now.minute * 6 + now.second * 0.1) + 90
        
    def draw_dial(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.center, self.radius)
        pygame.draw.circle(screen, (0, 0, 0), self.center, self.radius, 6)
        
        font = pygame.font.SysFont('Arial', 32, bold=True)
        
        for i in range(60):
            angle = math.radians(i * 6 - 90)
            
            if i % 5 == 0:
                inner_r = self.radius - 35
                width = 6
                
                txt = font.render(str(i), True, (0, 0, 0))
                txt_rect = txt.get_rect(center=(self.center[0] + (self.radius - 70) * math.cos(angle),
                                                self.center[1] + (self.radius - 70) * math.sin(angle)))
                screen.blit(txt, txt_rect)
            else:
                inner_r = self.radius - 15
                width = 2
            
            start = (self.center[0] + inner_r * math.cos(angle), self.center[1] + inner_r * math.sin(angle))
            end = (self.center[0] + (self.radius - 8) * math.cos(angle), self.center[1] + (self.radius - 8) * math.sin(angle))
            pygame.draw.line(screen, (0, 0, 0), start, end, width)
        
    def blit_rotate_center(self, surf, image, center, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)   
        surf.blit(rotated_image, new_rect) 
    
    def draw(self, screen):
        self.draw_dial(screen)
        self.blit_rotate_center(screen, self.minute_hand, self.center, self.min_angle)
        self.blit_rotate_center(screen, self.second_hand, self.center, self.sec_angle)
        pygame.draw.circle(screen, (0, 0, 0), self.center, 12)