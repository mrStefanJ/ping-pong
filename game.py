import pygame
from objects import Paddle, Ball
from settings import WIDTH, HEIGHT, WIN_SCORE
from ai import opponent_ai

class Game:
    def __init__(self):
        self.player = Paddle(WIDTH - 30, HEIGHT/2 - 70)
        self.opponent = Paddle(18, HEIGHT/2 - 70)
        self.ball = Ball()
        self.player_score = 0
        self.opponent_score = 0
        self.state = "menu"
        self.mode = None  # "single" ili "multi"

    def update(self, keys=None):
        if self.state != "play":
            return

        self.player.update()
        self.ball.update()

        if self.mode == "single":
            opponent_ai(self.opponent, self.ball)
        elif self.mode == "multi" and keys:
            if keys[pygame.K_w]:
                self.opponent.speed = -7
            elif keys[pygame.K_s]:
                self.opponent.speed = 7
            else:
                self.opponent.speed = 0
            self.opponent.update()

        # Paddle collision
        if self.ball.rect.colliderect(self.player.rect) or self.ball.rect.colliderect(self.opponent.rect):
            self.ball.speed_x *= -1

        # Scoring
        if self.ball.rect.right >= WIDTH:
            self.opponent_score += 1
            self.ball.reset()
        if self.ball.rect.left <= 0:
            self.player_score += 1
            self.ball.reset()

        # Win condition
        if self.player_score >= WIN_SCORE or self.opponent_score >= WIN_SCORE:
            self.state = "gameover"