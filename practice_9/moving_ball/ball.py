import pygame

class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = 50
        self.color = color
        self.speed_x = 8
        self.speed_y = 8
            