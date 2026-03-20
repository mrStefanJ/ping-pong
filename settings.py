import pygame

WIDTH, HEIGHT = 880, 760
FPS = 60
WIN_SCORE = 5

# Colors
BG = pygame.Color('grey12')
WHITE = (200, 200, 200)
NEON_BLUE = (0, 255, 255)
NEON_PINK = (255, 20, 147)

# Fonts (inicijalizovati u main.py)
pygame.font.init()
title_font = pygame.font.SysFont("Arial", 100)
score_font = pygame.font.SysFont("Arial", 80)
ui_font = pygame.font.SysFont("Arial", 40)