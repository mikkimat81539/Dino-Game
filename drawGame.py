import pygame

pygame.init()

class gamePlayDraw:
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = str(color)
        self.get_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
    
    def draw_rect(self, screen):
        return pygame.draw.rect(screen, self.color, self.get_rect)