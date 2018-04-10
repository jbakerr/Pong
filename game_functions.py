import pygame
import sys

from ball import Ball

from paddle import Paddle

import math


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


def update_ball(ai_settings, screen, human_paddle, ai_paddle, ball):
    if ball.rect.collidelist([human_paddle, ai_paddle]) > -1:
        paddle_bounce(ball)
    if ball.check_top() or ball.check_bottom():
        top_bouce(ball)



def paddle_bounce(ball):
        ball.angle = - ball.angle

def top_bouce(ball):
    if ball.check_top:
        ball.angle = math.pi - ball.angle


def ai_update(ball, ai_paddle, ai_settings):
    if ai_paddle.rect.y < ball.rect.y:
        ai_paddle.moving_down = True
    else:
        ai_paddle.moving_down = False
    if ai_paddle.rect.y > ball.rect.y:
        ai_paddle.moving_up = True
    else:
        ai_paddle.moving_up = False
