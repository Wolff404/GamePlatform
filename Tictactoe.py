import pygame
from Classes.Grid import Grid

pygame.init()

pygame.display.set_caption('Tic Tac Toe')

grid_object = Grid()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid_object.draw_grid()
    pygame.display.flip()
#test
pygame.quit()

# elif event.type == pygame.MOUSEBUTTONDOWN:
# CR.draw_cross()
