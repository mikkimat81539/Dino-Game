import pygame, random
from drawGame import gamePlayDraw_Squares
from drawGame import gamePlayDraw_Trianges

pygame.init()

clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("DINO GAME")

# PLATFORM
platform = gamePlayDraw_Squares(0, 220, 500, 30, "gray")

# ENEMIES

# 190 is the the line that top point should not pass
redTriangle = gamePlayDraw_Trianges(460, 220, 490, 220,"black")

# Physics
speed = 5

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)    
    

    screen.fill("white")

    # Render Code here
    platform.draw_rect(screen)
    redTriangle.draw_polygon(screen)
    
    pygame.display.flip()
    
    clock.tick(40)

    pygame.display.update()

pygame.quit()
