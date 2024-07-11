import pygame

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Game platform menu')

battleships_logo = pygame.image.load('assets/images/battleshipslogo.png')
chess_logo = pygame.image.load('assets/images/chesslogo.png')
tictactoe_logo = pygame.image.load('assets/images/tictactoelogo.png')

class Menu:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
'''

    def launch_game(self):
        pass
'''


battleships_button = Menu(250,200,battleships_logo)
chess_button = Menu(250,400,chess_logo)
tictactoe_button = Menu(250,600,tictactoe_logo)

def display_menu():
    running = True
    while running:

        screen.fill((127, 127, 127))
        battleships_button.draw()
        chess_button.draw()
        tictactoe_button.draw()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

display_menu()
pygame.quit()