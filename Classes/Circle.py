import pygame
# Create class



def draw_circle():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    col = mouse_x // TTT.cell_width
    row = mouse_y // TTT.cell_height
    TTT.grid[row][col] = pygame.draw.circle(TTT.screen, (255, 255, 255), (TTT.cell_width // 2, TTT.cell_height // 2), 50, 0)


