import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))

from pygame.color import THECOLORS
screen.fill(THECOLORS['grey'])
#домик
r = pygame.Rect(200, 200, 200, 200)
pygame.draw.rect(screen, (210, 0, 150), r, 10)
y = pygame.Rect(250, 250, 100, 100)
pygame.draw.polygon(screen, ('black'), [(200, 200), (400, 200), (300, 130)], 7)
pygame.draw.rect(screen, ('white'), y, 10)

#флаг
pygame.draw.polygon(screen, ('white'), [(500, 400), (500, 200)], 5)
pygame.draw.polygon(screen, ('white'), [(500, 200), (660, 200), (660, 300), (500, 300)], 3)

#круги
pygame.draw.circle(screen, ('blue'), (540, 244), 20, 5)
pygame.draw.circle(screen, ('black'), (580, 244), 20, 5)
pygame.draw.circle(screen, ('red'), (620, 244), 20, 5)
pygame.draw.circle(screen, ('yellow'), (560, 265), 20, 5)
pygame.draw.circle(screen, ('green'), (600, 265), 20, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()
