import pygame
from pygame.sprite import Sprite
import math
from random import choice


class Ball(Sprite):
    """A class to manage the main ball"""

    def __init__(self, ai_settings, screen):
        """Create a ball object that starts in the center"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        angle = choice([3, 1.5, 1.75, 0.75])
        self.angle = math.pi / angle

        self.rect = pygame.Rect(
            0, 0, ai_settings.ball_width, ai_settings.ball_height
        )

        self.rect.center = self.screen_rect.center
        # self.rect.centery = screen.rect.centery

        self.color = ai_settings.ball_color

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_ball(self):
        """Draw the ball on the screen"""
        pygame.draw.ellipse(self.screen, self.color, self.rect)

    def update(self):

        self.x += (
            math.sin(self.angle) *
            self.ai_settings.ball_speed *
            self.ai_settings.ball_direction
        )
        self.y -= math.cos(self.angle) * self.ai_settings.ball_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def check_top(self):
        """Return true if alien is at the edge of the screen"""

        if self.rect.y <= self.screen_rect.top:
            return True

    def check_bottom(self):
        """Return true if alien is at the edge of the screen"""

        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def reset_ball(self):
        self.x = self.screen_rect.centerx
        self.y = self.screen_rect.centery
        angle = choice([3, 1.5, 1.75, 0.75])
        self.angle = math.pi / angle
