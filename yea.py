import pygame

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hei med Checkboxes')

# Define font
font = pygame.font.Font(None, 36)

# Checkbox class
class Checkbox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BLACK
        self.checked = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        if self.checked:
            pygame.draw.line(screen, self.color, (self.rect.left, self.rect.top), (self.rect.right, self.rect.bottom), 2)
            pygame.draw.line(screen, self.color, (self.rect.left, self.rect.bottom), (self.rect.right, self.rect.top), 2)

    def click(self, event):
        if self.rect.collidepoint(event.pos):
            self.checked = not self.checked

# Create checkboxes
checkbox1 = Checkbox(50, 100, 20, 20)
checkbox2 = Checkbox(50, 150, 20, 20)


def start_main_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                checkbox1.click(event)
                checkbox2.click(event)

        # Fill the screen with white
        screen.fill(WHITE)

        # Render the text "Hei"
        text_surface = font.render('Hei', True, BLACK)
        screen.blit(text_surface, (150, 50))

        # Draw checkboxes
        checkbox1.draw(screen)
        checkbox2.draw(screen)

        # Update the display
        pygame.display.flip()

start_main_loop()

# Quit Pygame
pygame.quit()
