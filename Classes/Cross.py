import pygame
import Tictactoe as TTT


def draw_cross():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // TTT.cell_width
    row = mouse_y // TTT.cell_height
    TTT.grid[row][col] = pygame.draw.line(TTT.screen, TTT.RANDOM_COLOR,(100,100),(200,200))
    print("HEY")
