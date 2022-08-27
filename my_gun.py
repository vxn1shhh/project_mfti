import random
import sys

import pygame
from pygame.color import THECOLORS

pygame.init()

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Cannon:
    def __init__(self):
        self.color = (125, 125, 125)
        self.pointlist = [(0, 0), (100, 0), (0, 100)]
        # TODO(1.1): создайте атрибуты пушки:
        #  * Цвет
        #  * Список точек
        #  Пусть пушка отображается как равнобедренный треугольник с высотой
        #  и основанием по 50px. Отображается в середине окна
        #  на нижней границе, см. схему в начале файла.

    def draw(self):
        pygame.draw.polygon(screen, color=self.color, points=self.pointlist)
        # TODO(1.2): отобразите созданную в __init__ последовательность точек
        #  заданным цветом.


class Bullet:
    def __init__(self):
        self.centre = 320
        self.rad = 5
        self.color_bullet = 'white'
        self.speed_bullet = 3
        # TODO(2.1): создайте атрибуты снаряда.
        #  * Центр окружности снаряда
        #  * Радиус
        #  * Цвет
        #  * Скорость (для тестов использовать значение 3)
        ...

    def draw(self):
        # pygame.draw.circle(screen, color_bullet, (centre), radius, 0)
        # pygame.display.flip()
        # TODO(2.2): отобразите снаряд.

    def move(self):
        # pygame.draw.circle(screen, color_bullet, centre - 3, radius, 0)
        # TODO(2.3): реализуйте перемещение снаряда.
        #  Для этого нужно создать его новый центр со смещением speed по оси OY
        #  к началу коориднат.
        ...


class Target:
    def __init__(self):
        # self.color_target = color_target
        # self.speed_target = speed_target
        # self.rect = rect
        # TODO(3.1): создайте атрибуты мишени.
        #  * Цвет
        #  * Скорость
        #  * Прямоугольник
        ...

    def draw(self):
        # TODO(3.2): отобразите мишень.
        ...

    def move(self):
        # TODO(3.3): реализуйте движение мишени.
        #  При достижении края окна мишень должна менять направление движения
        #  на противположное. Это можно реализовать сменой знака сокрости.
        ...


colors = list(THECOLORS.values())


def get_random_color():
    return random.choice(colors)


cannon = Cannon()
target = Target()
bullet = Bullet()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(THECOLORS['black'])

    target.move()
    bullet.move()

    # TODO(2.4): если снаряд достиг верхней границы окна, создать новый снаряд.

    # TODO(4.1): если мишень и снаряд пересеклись, сменить цвет мишени на
    #  случайный, создать новй снаряд.
    #  Для определения пересечения используйте метод прямоугольника:
    #    Rect.collidepoint(point)

    cannon.draw()
    target.draw()
    bullet.draw()

    pygame.display.flip()
    pygame.time.wait(33)
