import pygame

from pygame.sprite import Sprite



class Ball(Sprite):
    """A class to manage the main ball"""

    def __init__(self, ai_settings, screen):
        """Create a ball object that starts in the center"""
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()


        self.rect = pygame.Rect(
            0, 0, ai_settings.ball_width, ai_settings.ball_height
        )

        self.rect.center = self.screen_rect.center
        # self.rect.centery = screen.rect.centery

        self.color = ai_settings.ball_color

    def draw_ball(self):
        """Draw the ball on the screen"""
        pygame.draw.ellipse(self.screen, self.color, self.rect)
