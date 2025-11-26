import pygame

pygame.init()

class gamePlayDraw_Squares:
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = str(color)
        self.get_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

    def draw_rect(self, screen):
        return pygame.draw.rect(screen, self.color, self.get_rect)

class gamePlayDraw_Triange:
    def __init__(self, Lx_pos, Ly_pos, Tx_pos, Ty_pos, Rx_pos, Ry_pos, color):
        self.Lx_pos = Lx_pos # Left part of triange on X axis
        self.Ly_pos = Ly_pos # Left part of triange on Y axis
        self.Tx_pos = Tx_pos # Top part of triange on X axis
        self.Ty_pos = Ty_pos # Top part of triange on Y axis
        self.Rx_pos = Rx_pos # Right part of triange on X axis
        self.Ry_pos = Ry_pos # Right part of triange on Y axis
        self.set_points = [(self.Lx_pos, self.Ly_pos), (self.Tx_pos, self.Ty_pos), (self.Rx_pos, self.Ry_pos)]
        self.color = str(color)
    
    def draw_polygon(self, screen):
        return pygame.draw.polygon(screen, self.color, self.set_points)
