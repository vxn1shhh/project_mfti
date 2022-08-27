import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
sprite = pygame.image.load("img.png")

# screen.blit(sprite, (20, 20))

# animation_set = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]



clock = pygame.time.Clock()
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    screen.blit(sprite, (20, 20))

    # window.blit(animation_set[i // 12], (100, 20))
    # i += 1
    # if i == 60:
    #     i = 0

    pygame.display.flip()
    # clock.tick(60)