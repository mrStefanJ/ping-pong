# main.py
import pygame, sys
from settings import *
from game import Game
from ui import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEON PONG")
clock = pygame.time.Clock()

game = Game()
paused = False  # pauza

while True:
    keys = pygame.key.get_pressed()

    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # Pauza
            if event.key == pygame.K_ESCAPE and game.state == "play":
                paused = not paused

            if paused:
                if event.key == pygame.K_q:  # Q -> quit pauza i vrati u menu
                    game.state = "menu"
                    paused = False
                    game.player_score = 0
                    game.opponent_score = 0
                    game.ball.reset()

            # Restart posle gameover
            if game.state == "gameover" and event.key == pygame.K_r:
                game = Game()
                paused = False

            # Player movement
            if event.key == pygame.K_UP:
                game.player.speed -= 7
            if event.key == pygame.K_DOWN:
                game.player.speed += 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                game.player.speed += 7
            if event.key == pygame.K_DOWN:
                game.player.speed -= 7

    # --- MENU INPUT ---
    if game.state == "menu":
        draw_menu(screen)
        if keys[pygame.K_1]:
            game.state = "play"
            game.mode = "single"
        elif keys[pygame.K_2]:
            game.state = "play"
            game.mode = "multi"
        elif keys[pygame.K_3]:
            pygame.quit()
            sys.exit()

    # --- UPDATE GAME ---
    if game.state == "play" and not paused:
        game.update(keys)  # prosledi keys ako želiš za multiplayer kontrolu

    # --- DRAW ---
    screen.fill(BG)

    if game.state == "menu":
        draw_menu(screen)

    elif game.state == "play":
        draw_center_line(screen)
        draw_glow_rect(screen, game.player.rect, NEON_BLUE)
        draw_glow_rect(screen, game.opponent.rect, NEON_PINK)
        draw_ball(screen, game.ball, NEON_BLUE)
        draw_score(screen, game.player_score, game.opponent_score)

        if paused:
            draw_pause(screen)  # crta pause meni

    elif game.state == "gameover":
        draw_gameover(screen, game.player_score, game.opponent_score)

    pygame.display.flip()
    clock.tick(FPS)