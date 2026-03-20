def opponent_ai(opponent, ball):
    if opponent.rect.centery < ball.rect.centery:
        opponent.speed = 7
    elif opponent.rect.centery > ball.rect.centery:
        opponent.speed = -7
    else:
        opponent.speed = 0
    opponent.update()