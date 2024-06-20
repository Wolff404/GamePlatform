import pygame
from Classes.Grid import Grid
from Classes.Circle import Circle

pygame.init()

pygame.display.set_caption('Tic Tac Toe')

grid_object = Grid()
circle_object = Circle()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    grid_object.draw_grid()
    circle_object.draw_circle()
    pygame.display.flip()


pygame.quit()

# elif event.type == pygame.MOUSEBUTTONDOWN:
# CR.draw_cross()
