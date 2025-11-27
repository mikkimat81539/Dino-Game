import pygame, random
from drawGame import gamePlayDraw_Squares
from drawGame import gamePlayDraw_Trianges

pygame.init()

clock = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("DINO GAME")

# PLAYER
player = gamePlayDraw_Squares(10, 190, 30, 30, "green")

# PLATFORM
platform = gamePlayDraw_Squares(0, 220, 500, 30, "gray")

# PLAYER PHYSICS
speed_x = 5
y_gravity = 1
jump_height = 15
speed_y = jump_height

jumping = False # store whether or not player is jumping

# ENEMIES

# 190 is the the line that top point should not pass
redTriangle = gamePlayDraw_Trianges(190, 220, 214, 194, 241, 220, "black")

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)

    # PLAYER MOVEMENT
    player.get_rect.x += speed_x 

    if player.get_rect.x >= 150:
        player.get_rect.x = 150

    keys =pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        jumping = True

    if jumping:
        player.get_rect.y -= speed_y # moving upwards
        speed_y -= y_gravity # coming down

        if speed_y < -jump_height:  # check to see if jump is finished (it goes to jump height and then once it reaches it goes to negative jump height)
            jumping = False
            speed_y = jump_height
    
    screen.fill("white")

    # Render Code here
    player.draw_rect(screen)
    platform.draw_rect(screen)
    redTriangle.draw_polygon(screen)
    
    pygame.display.flip()
    
    clock.tick(40)

    pygame.display.update()

pygame.quit()
