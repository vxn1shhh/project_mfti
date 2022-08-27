import sys
import pygame

pygame.init()

animation_set = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]

window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-40, 0

            elif event.key == pygame.K_RIGHT:
                rect.move_ip(40, 0)
    window.fill((0,0,0))
    window.blit(animation_set[i // 12], (100, 20))
    i += 1
    if i == 60:
        i = 0

    pygame.display.flip()
    clock.tick(60)
