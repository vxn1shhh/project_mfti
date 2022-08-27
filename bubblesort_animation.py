import pygame
import random
import sys

pygame.init()

WIDTH = 640
HEIGHT = 480
count = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))

a = [i * 48 for i in range(1, 11)]
random.shuffle(a)

rects = []

for index, elem in enumerate(a):
    r = pygame.Rect(64 * index, 480 - elem, 64, elem)
    rects.append(r)

for x in rects:
    pygame.draw.rect(screen, (200, 50, 125), x, 0)

for bubble in range(len(rects)):
    for bubble2 in range(0, len(rects) - 1):
        if rects[bubble2].height > rects[bubble2 + 1].height:
            rects[bubble2 + 1].height, rects[bubble2].height = rects[bubble2].height, rects[bubble2 + 1].height
            print(rects)

# a = [420, 4242, 2, 4, 0, 1]
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# print(a)
# for t in rects:
#     pygame.draw.rect(screen, (200, 50, 125), t, 0)
while True:
    for t in rects:
        pygame.draw.rect(screen, (200, 50, 125), t, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
