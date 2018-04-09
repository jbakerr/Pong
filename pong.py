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

    screen.fill((0, 0, 0))

    ball = Ball(ai_settings, screen)

    human_paddle = Paddle(ai_settings, screen, 'right')
    ai_paddle = Paddle(ai_settings, screen, 'left')

    while True:

        pygame.display.flip()
        gf.check_events()
        ball.draw_ball()
        human_paddle.draw_paddle()
        ai_paddle.draw_paddle()




run_game()
