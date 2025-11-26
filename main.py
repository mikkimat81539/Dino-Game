import pygame, sys
from drawGame import gamePlayDraw_Squares

pygame.init()

clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("DINO GAME")

# PLAYER
player = gamePlayDraw_Squares(10, 190, 30, 30, "green")

# PLATFORM
platform = gamePlayDraw_Squares(0, 220, 500, 30, "gray")

# PHYSICS
speed_x = 5
speed_y = 30

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)
    
    # PLAYER MOVEMENT
    player.get_rect.x += speed_x

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        player.get_rect.y -= speed_y


    screen.fill("white")

    # Render Code here
    player.draw_rect(screen)
    platform.draw_rect(screen)
    
    pygame.display.flip()
    
    clock.tick(35)
