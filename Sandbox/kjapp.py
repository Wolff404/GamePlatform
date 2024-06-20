import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Battleships")

# Define grid properties
rows = 10
cols = 10

cell_width = screen_width // cols
cell_height = screen_height // rows

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Color to paint the tiles

# Create a grid to keep track of painted tiles
grid = [[WHITE for _ in range(cols)] for _ in range(rows)]

def draw_grid():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, grid[row][col], rect)  # Fill the cell with the color in the grid
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw rectangle outlines in black

# Main game loop
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
                grid[row][col] = RED  # Paint the clicked tile red
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // cell_width
            row = mouse_y // cell_height
            if 0 <= row < rows and 0 <= col < cols:
                grid[row][col] = BLACK


    # Fill the screen with a background color
    screen.fill(WHITE)

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()

###########################
pygame.quit()
sys.exit()
