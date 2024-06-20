import pygame
import sys

# Initialiser Pygame
pygame.init()

# Sett opp skjermens bredde og høyde
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Sett opp et vindusnavn
pygame.display.set_caption('Mitt Pygame Vindue')

# Hovedløkken
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fyll skjermen med en bakgrunnsfarge
    screen.fill((255, 255, 255))

    # Tegn en hvit sirkel midt på skjermen
    pygame.draw.circle(screen, (25, 255, 255), (width // 2, height // 2), 50, 0)

    # Oppdater skjermen
    pygame.display.flip()

# Avslutt Pygame
pygame.quit()
sys.exit()
