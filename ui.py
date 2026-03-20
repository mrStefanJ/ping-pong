import pygame
from settings import *

def draw_center_line(screen):
    for y in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (WIDTH/2 - 2, y, 4, 20))

def draw_glow_rect(screen, rect, color):
    for i in range(8, 0, -2):
        glow = pygame.Surface((rect.width + i*2, rect.height + i*2), pygame.SRCALPHA)
        pygame.draw.rect(glow, (*color, 20), glow.get_rect(), border_radius=6)
        screen.blit(glow, (rect.x - i, rect.y - i))
    pygame.draw.rect(screen, color, rect, border_radius=6)

def draw_ball(screen, ball, color):
    for i, pos in enumerate(ball.trail):
        alpha = int(255 * (i / len(ball.trail)))
        surf = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*color, alpha), (10, 10), 10)
        screen.blit(surf, (pos[0]-10, pos[1]-10))
    pygame.draw.ellipse(screen, color, ball.rect)

def draw_score(screen, player_score, opponent_score):
    p_text = score_font.render(str(player_score), True, NEON_BLUE)
    o_text = score_font.render(str(opponent_score), True, NEON_PINK)
    screen.blit(o_text, (WIDTH/4 - o_text.get_width()/2, 20))
    screen.blit(p_text, (WIDTH*3/4 - p_text.get_width()/2, 20))

def draw_gameover(screen, player_score, opponent_score):
    winner = "PLAYER WINS!" if player_score > opponent_score else "AI WINS!"
    text1 = title_font.render("GAME OVER", True, NEON_PINK)
    text2 = score_font.render(winner, True, NEON_BLUE)
    text3 = ui_font.render("PRESS R TO RESTART", True, WHITE)
    screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT/3))
    screen.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2))
    screen.blit(text3, (WIDTH/2 - text3.get_width()/2, HEIGHT*0.7))

def draw_menu(screen):
    title = title_font.render("NEON PONG", True, NEON_PINK)
    option1 = ui_font.render("1 - Singleplayer (AI)", True, WHITE)
    option2 = ui_font.render("2 - Multiplayer (2 Players)", True, WHITE)
    option3 = ui_font.render("3 - Exit", True, WHITE)
    screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/4))
    screen.blit(option1, (WIDTH/2 - option1.get_width()/2, HEIGHT/2))
    screen.blit(option2, (WIDTH/2 - option2.get_width()/2, HEIGHT/2 + 50))
    screen.blit(option3, (WIDTH / 2 - option3.get_width() / 2, HEIGHT / 2 + 150))

def draw_pause(screen):
    # Poluprovidna pozadina
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # RGBA, A=180 znači poluprovidno
    screen.blit(overlay, (0, 0))

    # Tekst pauze
    title = title_font.render("PAUSED", True, NEON_PINK)
    option1 = ui_font.render("ESC - Resume", True, WHITE)
    option2 = ui_font.render("Q - Quit to Menu", True, WHITE)

    screen.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT/3))
    screen.blit(option1, (WIDTH/2 - option1.get_width()/2, HEIGHT/2))
    screen.blit(option2, (WIDTH/2 - option2.get_width()/2, HEIGHT/2 + 50))