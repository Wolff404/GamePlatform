import pygame

from Classes import Grid


class Circle:
    def __init__(self, col, row, cell_width, cell_height, screen):
        self.grid.col = col
        self.grid.row = row
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.screen = screen

    def draw_circle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = mouse_x // self.cell_width
        row = mouse_y // self.cell_height
        # Grid.grid[row][col] = pygame.draw.circle(self.screen, (255, 255, 255),
        #                                        (self.cell_width // 2, self.cell_height // 2), 50, 0)


