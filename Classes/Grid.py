import pygame


class Grid:
    def __init__(self, row=3, col=3, screen_width=800, screen_height=800, white=(255, 255, 255), black=(0, 0, 0)):
        self.row = row
        self.col = col
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_width = screen_width // col
        self.cell_height = screen_height // row
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.black = black
        self.white = white
        self.grid = [[white for _ in range(col)] for _ in range(row)]

    def draw_grid(self):
        for row in range(self.row):
            for col in range(self.col):
                rect = pygame.Rect(col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, self.grid[row][col], rect)
                pygame.draw.rect(self.screen, self.black, rect, 1)
