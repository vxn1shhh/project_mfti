import sys
import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 120, 120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-40, 0)
                pygame.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(40, 0)
                pygame.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -40)
                pygame.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect, 0)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 40)
                pygame.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect, 0)
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255, 0, 0), rect, 0)
            pygame.display.flip()

    pygame.draw.rect(screen, (255, 0, 0), rect, 0)

    pygame.display.flip()

