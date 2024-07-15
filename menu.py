import pygame
from games.TicTacToe import tictactoe

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game platform menu')

battleships_logo = pygame.image.load('assets/images/battleshipslogo.png')
chess_logo = pygame.image.load('assets/images/chesslogo.png')
tictactoe_logo = pygame.image.load('assets/images/tictactoelogo.png')
welcome_logo = pygame.image.load('assets/images/welcomeinstructions.png')


class Menu:
    def __init__(self, x, y, image):  # TODO: Add scaling?
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):

        action = False

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:  # With this button can be pressed several times. Useless, I know.
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


welcome_button = Menu(230, 10, welcome_logo)
battleships_button = Menu(250, 200, battleships_logo)
chess_button = Menu(250, 400, chess_logo)
tictactoe_button = Menu(250, 600, tictactoe_logo)


def display_menu():
    running = True
    while running:

        screen.fill((127, 127, 127))

        welcome_button.draw()

        if battleships_button.draw() == True:
            print("Battleships")  # TODO: Add run game function when it's been made.

        if chess_button.draw() == True:
            print("Chess")  # TODO: Add run game function when it's been made.

        if tictactoe_button.draw() == True:
            tictactoe.run()
            print("Tictactoe")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


display_menu()

