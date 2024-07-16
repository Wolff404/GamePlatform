import pygame


def run():
    pygame.init()

    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Tictactoe")

    clicked = False
    spaces = []
    #mouse_position = []
    player = 1

    for _ in range(3):  # Creating the 3x3 matrice
        row = [0] * 3
        spaces.append(row)

    def draw_grid():
        background_color = (230, 230, 230)
        grid = (100, 100, 100)
        screen.fill(background_color)
        for x in range(1, 3):
            pygame.draw.line(screen, grid, (0, x * 200), (screen_width, x * 200), 3)  # Drawing the horizontal lines
            pygame.draw.line(screen, grid, (x * 200, 0), (x * 200, screen_height), 3)  # Drawing the vertical lines

    def place_space(): #
        black = (0, 0, 0)
        line_thickness = 3
        cell_size = 200  # Size of each cell

        x_position = 0
        for x in spaces:  # Checks for x in the grid
            y_position = 0
            for y in x:  # Checks for y in the grid
                center_x = x_position * cell_size + cell_size // 2  # Calculating x coordinate of the centre of the
                # current cell
                center_y = y_position * cell_size + cell_size // 2  # Calculating y coordinate of the centre of the
                # current cell
                if y == 1:  # Drawing lines to make an X
                    offset = cell_size // 3  # Ensuring that the drawing's size fits the grid cell well enough
                    pygame.draw.line(screen, black, (center_x - offset, center_y - offset),
                                     (center_x + offset, center_y + offset), line_thickness)
                    pygame.draw.line(screen, black, (center_x + offset, center_y - offset),
                                     (center_x - offset, center_y + offset), line_thickness)

                if y == -1:  # Drawing O
                    radius = cell_size // 3  # Ensuring that the drawing's size fits the grid cell well enough
                    pygame.draw.circle(screen, black, (center_x, center_y), radius, line_thickness)

                y_position += 1
            x_position += 1

    running = True
    while running:
        draw_grid()
        place_space()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:  # For checking a mouse click cycle
                clicked = False  # Now implementing logic for when the mouse-button is released.
                mouse_position = pygame.mouse.get_pos()  # Where the mouse-button was released
                cell_x = mouse_position[0] // 200  # Defining x coordinate
                cell_y = mouse_position[1] // 200  # Defining y coordinate
                if spaces[cell_x][cell_y] == 0:  # Checking if anything has been clicked.
                    spaces[cell_x][cell_y] = player  # Player 1 goes first
                    player *= -1  # Changing to player 2 ( Player -1) by multiplying 1 with -1 and vice versa

        pygame.display.update()

    pygame.quit()
