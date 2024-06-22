import random
from random import randrange
import pygame
from pygame.locals import *

size = 1000, 700
width, height = size                    # Screen diamentions
RED = (255,0,0)                         # Color

R_color1 = random.randrange(255)
R_color2 = random.randrange(255)
R_color3 = random.randrange(255)
R_colors = (R_color1, R_color2, R_color3)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

ball = pygame.image.load("ball.gif")
rect = ball.get_rect()
speed = [1, 1]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(R_colors)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()

pygame.quit()