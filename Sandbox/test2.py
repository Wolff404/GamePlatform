import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 800
pygame.display.set_caption('Tic Tac Toe')
screen = pygame.display.set_mode((screen_width, screen_height))

cols = 3
rows = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CIRCLE_COLOR = (0, 0, 255)  # Farge for sirkelen

cell_width = screen_width // cols
cell_height = screen_height // rows

grid = [[WHITE for _ in range(cols)] for _ in range(rows)]


def draw_grid():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, grid[row][col], rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            # Tegn sirkelen hvis grid-indeksen inneholder CIRCLE_COLOR
            if grid[row][col] == CIRCLE_COLOR:
                center_x = col * cell_width + cell_width // 2
                center_y = row * cell_height + cell_height // 2
                radius = min(cell_width, cell_height) // 2 - 10
                pygame.draw.circle(screen, CIRCLE_COLOR, (center_x, center_y), radius, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // cell_width
            row = mouse_y // cell_height
            if 0 <= row < rows and 0 <= col < cols:
                grid[row][col] = CIRCLE_COLOR

    screen.fill(WHITE)
    draw_grid()
    pygame.display.flip()

pygame.quit()
sys.exit()
