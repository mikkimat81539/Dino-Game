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
init_Triangle = gamePlayDraw_Trianges(400, 220, 430, 220,"black")  # this will be the starting triangle

random_Triangle = gamePlayDraw_Trianges(random.randint(460, 490), 220, random.randint(480, 495), 220, "red")

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


    init_Triangle.updateTriangle(speed)

    random_Triangle.updateTriangle(speed)

    screen.fill("white")

    # Render Code here
    platform.draw_rect(screen)
    init_Triangle.draw_polygon(screen)
    random_Triangle.draw_polygon(screen)
    
    pygame.display.flip()
    
    clock.tick(40)

    pygame.display.update()

pygame.quit()
