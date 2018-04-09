import pygame
import sys

from ball import Ball

from paddle import Paddle


def check_events(ai_settings, screen, paddle):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_events(event, ai_settings, screen, paddle)
        elif event.type == pygame.KEYUP:
            check_up_events(event, ai_settings, screen, paddle)


def check_down_events(event, ai_settings, screen, paddle):
    """Respond to keypresses"""
    if event.key == pygame.K_UP:
        paddle.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddle.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_up_events(event, ai_settings, screen, paddle):
    """Respond to keypresses"""
    if event.key == pygame.K_UP:
        paddle.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle.moving_down = False


def update_screen(ai_settings, screen, human_paddle, ai_paddle, ball):
    screen.fill((0, 0, 0))
    ball.draw_ball()
    ai_paddle.draw_paddle()
    human_paddle.draw_paddle()
    pygame.display.flip()


