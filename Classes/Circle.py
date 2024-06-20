import pygame

class Circle: # Maybe it's easier to use an image with the pygame. Surface than drawing the circles and X maunally
    def __init__(self, x, y, col, row, mouse_x, mouse_y, cell_width, cell_height):
        self.x = x
        self.y = y
        self.col = col
        self.row = row
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.cell_width = cell_width
        self.cell_height = cell_height

    def draw_circle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        col = mouse_x // self.cell_width
        row = mouse_y // self.cell_height
        self.grid[row][col] = pygame.draw.circle(self.screen, (255, 255, 255), (self.cell_width // 2, self.cell_height // 2), 50, 0)


