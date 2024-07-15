import pygame

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tictactoe")

def run():
    running = True
    while running:
        screen.fill((255, 255, 255))  # Temporarly to show that the game is active

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()