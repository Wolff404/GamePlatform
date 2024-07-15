import pygame


def run():
    pygame.init()

    screen_width = 600
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tictactoe")

    def draw_grid():
        background_color = (230, 230, 230)
        grid = (100, 100, 100)
        screen.fill(background_color)
        for x in range(1, 3):
            pygame.draw.line(screen,grid,(0, x*200),(screen_width, x*200))
            pygame.draw.line(screen,grid,(x*200, 0),(x*200, screen_height))



    running = True
    while running:

        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
