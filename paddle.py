import pygame

from pygame.sprite import Sprite


class Paddle(Sprite):
    """A class to manage both paddles"""

    def __init__(self, ai_settings, screen, position):
        """Initialize the paddle"""

        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = ai_settings.paddle_color
        self.ai_settings = ai_settings

        if position == 'right':
            self.x = self.screen_rect.right - ai_settings.paddle_width
        else:
            self.x = self.screen_rect.left

        self.y = self.screen_rect.centery - (ai_settings.paddle_height / 2)

        self.rect = pygame.Rect(
            self.x, self.y,
            ai_settings.paddle_width,
            ai_settings.paddle_height
        )

        self.center = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up:
            self.center -= self.ai_settings.paddle_speed
        elif self.moving_down:
            self.center += self.ai_settings.paddle_speed

        self.rect.y = self.center

    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
