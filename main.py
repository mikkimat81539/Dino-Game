import pygame, sys

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("DINO GAME")

# PLAYER

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill("white")

    # Render Code here
    
    pygame.display.flip()