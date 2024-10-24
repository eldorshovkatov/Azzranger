import pygame
from pygame import Rect


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 8, 12)
        self.color = 255, 194, 14
        self.speed = 8
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):

        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
