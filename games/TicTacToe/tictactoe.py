import pygame

def run():
    pygame.init()

    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Tictactoe")
    cross_drawing = 'assets/images/tictactoeCROSS.png'

    clicked = False
    spaces = []
    mouse_position = []
    player = 1

    class TicTacToe:  # Stealing constructor and draw function from menu.py
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self,x,y,image):
            action = False
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            screen.blit(self.image, (self.rect.x, self.rect.y))
            return action


    TicTacToe.draw(200,200,cross_drawing)
    def draw_grid():
        background_color = (230, 230, 230)
        grid = (100, 100, 100)
        screen.fill(background_color)
        for x in range(1, 3):
            pygame.draw.line(screen, grid, (0, x*200), (screen_width, x*200), 3)  # Drawing the horizontal lines
            pygame.draw.line(screen, grid, (x*200, 0), (x*200, screen_height), 3)  # Drawing the vertical lines

        for _ in range(3):  # Creating the 3x3 matrice
            row = [0] * 3
            spaces.append(row)

    def place_space():
        x_position = 0
        for x in spaces:
            y_position = 0

    draw_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:  # For checking a mouse click cycle
                clicked = False  # Now implementing logic for when the mousebutton is released.
                mouse_position = pygame.mouse.get_pos()  # Where the mousebutton was released
                cell_x = mouse_position[0]  # Defining x coordinate
                cell_y = mouse_position[1]  # Defining y coordinate
                if spaces[cell_x // 200][cell_y // 200] == 0:  # Checking if anything has been clicked.
                    spaces[cell_x // 200][cell_y // 200] = player  # Player 1 goes first
                    player *= -1  # Changing to player 2 ( Player -1) by multiplying 1 with -1 and vice versa
        pygame.display.update()

    pygame.quit()


