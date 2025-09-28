import pygame
import settings as Settings
from asset_loader import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image(Settings.DEFAULT_SPRITE_PATH)
        self.rect = self.image.get_rect()

        self.vx = 0
        self.pos = pygame.math.Vector2((340, 240))
        self.vel = pygame.math.Vector2((0, 0))
        self.acc = pygame.math.Vector2((0, 0))
        self.direction = "RIGHT"