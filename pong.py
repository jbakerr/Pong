import pygame

import game_functions as gf

from settings import Settings

from ball import Ball

from paddle import Paddle


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((1200, 800))

    pygame.display.set_caption("Pong")

    ball = Ball(ai_settings, screen)

    human_paddle = Paddle(ai_settings, screen, 'right')
    ai_paddle = Paddle(ai_settings, screen, 'left')

    game_active = True


    while True:

        gf.check_events(ai_settings, screen, human_paddle)
        human_paddle.update()
        ball.update()
        gf.ai_update(ball, ai_paddle, ai_settings)
        ai_paddle.update()
        gf.update_ball(ai_settings, screen, human_paddle, ai_paddle, ball)
        gf.update_screen(ai_settings, screen, human_paddle, ai_paddle, ball)




run_game()
