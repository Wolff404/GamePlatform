# Create class
import pygame


class Pregame_Screen: # Problems may occur because mindset was making a pregame screen, but actually made checkboxes.
    def __init__(self, x, y, width, height, screen):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 0)
        self.checked = False
        self.screen = (400, 400)

    def draw(self, screen):
        screen = pygame.display.set_mode((self.screen))
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.display.set_caption("Welcome to Tic Tac Toe")

        font = pygame.font.Font(None, 40)
        if self.checked:
            pygame.draw.line(screen, self.color,(self.rect.left, self.rect.top), (self.rect.right, self.rect.bottom), 2)
            pygame.draw.line(screen, self.color,(self.rect.left, self.rect.bottom), (self.rect.right, self.rect.top), 2)



    # def click(self, event): To manage player settings.

    # Like which player gets to go first and chosing the cirlce and X.
