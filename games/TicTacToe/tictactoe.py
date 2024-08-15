import pygame
from pygame.locals import *


def run():
    pygame.init()

    font = pygame.font.SysFont(None, 52)

    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Tictactoe")

    clicked = False
    spaces = []
    player = 1

    winner = 0
    game_over = False

    play_again_rectangle = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

    for _ in range(3):  # Creating the 3x3 list
        row = [0] * 3
        spaces.append(row)

    def draw_grid():
        background_color = (230, 230, 230)
        grid = (100, 100, 100)
        screen.fill(background_color)
        for x in range(1, 3):
            pygame.draw.line(screen, grid, (0, x * 200), (screen_width, x * 200), 3)  # Drawing the horizontal lines
            pygame.draw.line(screen, grid, (x * 200, 0), (x * 200, screen_height), 3)  # Drawing the vertical lines

    def place_space():

        blueish = (100, 125, 255)
        greenish = (154, 161, 15)
        greenish2 = (161, 154, 50)
        line_thickness = 20
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
                    pygame.draw.line(screen, greenish, (center_x - offset, center_y - offset),
                                     (center_x + offset, center_y + offset), line_thickness)

                    pygame.draw.line(screen, greenish2, (center_x + offset, center_y - offset),
                                     (center_x - offset, center_y + offset), line_thickness)

                if y == -1:  # Drawing O
                    radius = cell_size // 3  # Ensuring that the drawing's size fits the grid cell well enough
                    pygame.draw.circle(screen, blueish, (center_x, center_y), radius, line_thickness)

                y_position += 1
            x_position += 1

    def check_winner():
        nonlocal winner, game_over

        x_position = 0

        for x in spaces:
            # Checking for columns

            if sum(x) == 3:  # Checking if player 1 won
                winner = 1
                game_over = True

            if sum(x) == -3:  # Checking if player 2 won
                winner = 2
                game_over = True

            # Checking for rows

            if spaces[0][x_position] + spaces[1][x_position] + spaces[2][x_position] == 3:
                winner = 1
                game_over = True

            if spaces[0][x_position] + spaces[1][x_position] + spaces[2][x_position] == -3:
                winner = 2
                game_over = True

            x_position += 1

        # Checking for cross
        if spaces[0][0] + spaces[1][1] + spaces[2][2] == 3 or spaces[0][2] + spaces[1][1] + spaces[2][0] == 3:
            winner = 1
            game_over = True

        if spaces[0][0] + spaces[1][1] + spaces[2][2] == -3 or spaces[0][2] + spaces[1][1] + spaces[2][0] == -3:
            winner = 2
            game_over = True

        # Checking if the game ends in a tie
        if game_over == False:
            tie = True
            for rows in spaces:
                for x in rows:
                    if x == 0:
                        tie = False

            if tie == True:
                game_over = True
                winner = 0


    def display_game_over(winner):

        if winner != 0:
            display_ending_text = "Player " + str(winner) + " is the winner."

        elif winner == 0:
            display_ending_text = "The game ends in a tie."

        end_screen_display = font.render(display_ending_text, True, (255, 250, 0))
        pygame.draw.rect(screen, (25, 255, 20), (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
        screen.blit(end_screen_display, (screen_width // 2 - 100, screen_height // 2 - 50))

        play_again_text = 'Play Again?'
        play_again_display = font.render(play_again_text, True, (25, 25, 200))
        pygame.draw.rect(screen, (255, 255, 40), play_again_rectangle)
        screen.blit(play_again_display, (screen_width // 2 - 80, screen_height // 2 + 10))

    running = True
    while running:
        draw_grid()
        place_space()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_over == False:   # The error occurs here.

                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
                if event.type == pygame.MOUSEBUTTONUP and clicked == True:  # For checking a mouse click cycle
                    clicked = False  # Now implementing logic for when the mouse-button is released.
                    mouse_position = pygame.mouse.get_pos()  # Where the mouse-button was released
                    cell_x = mouse_position[0] // 200  # Defining x coordinate
                    cell_y = mouse_position[1] // 200  # Defining y coordinate
                    if spaces[cell_x][cell_y] == 0:  # Checking if anything has been clicked.
                        spaces[cell_x][cell_y] = player  # Player 1 go first
                        player *= -1  # Changing to player 2 ( Player -1) by multiplying 1 with -1 and vice versa
                        check_winner()

        if game_over == True:
            display_game_over(winner)

            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if play_again_rectangle.collidepoint(pos):

                    game_over = False
                    player = 1
                    spaces = []
                    winner = 0

                    for x in range(3):
                        row = [0] * 3
                        spaces.append(row)

        pygame.display.update()

    pygame.quit()
