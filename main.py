import pygame
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

# JUMPING, SPEED and GRAVITY

jumping = False

speed_x = 5
speed_y = 10

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse = pygame.mouse.get_pos()
        #     print(mouse)
    
    # PLAYER MOVEMENT
    player.get_rect.x += speed_x

    keys = pygame.key.get_pressed()

   # JUMPING
    if keys[pygame.K_SPACE]:
        jumping = True

        if jumping:
            player.get_rect.y -= speed_y
            speed_y -= 10
        
        
    
    screen.fill("white")

    # Render Code here
    player.draw_rect(screen)
    platform.draw_rect(screen)
    
    pygame.display.flip()
    
    clock.tick(25)

pygame.quit()
