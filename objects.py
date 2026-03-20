import pygame
import random
from settings import WIDTH, HEIGHT

class Paddle:
    def __init__(self, x, y, width=12, height=140):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 0

    def update(self):
        # Pomeri paddle po y osi
        self.rect.y += self.speed

        # Ograniči da ne izađe van ekrana
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball:
    def __init__(self, size=24):
        self.rect = pygame.Rect(WIDTH/2 - size/2, HEIGHT/2 - size/2, size, size)
        self.speed_x = 7 * random.choice([1, -1])
        self.speed_y = 7 * random.choice([1, -1])
        self.trail = []  # za neon trail

    def update(self):
        # Pomeri lopticu
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Sudar sa vrhom ili dnom ekrana
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

        # Dodaj trenutnu poziciju u trail
        self.trail.append((self.rect.centerx, self.rect.centery))
        if len(self.trail) > 15:  # maksimalna dužina trail
            self.trail.pop(0)

    def reset(self):
        # Resetuj poziciju i random smer
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speed_x = 7 * random.choice([1, -1])
        self.speed_y = 7 * random.choice([1, -1])
        self.trail.clear()