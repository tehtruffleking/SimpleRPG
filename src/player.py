import pygame
import settings as Settings
from asset_loader import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image(Settings.DEFAULT_SPRITE_PATH)
        self.rect = self.image.get_rect()

        self.pos = pygame.math.Vector2((340, 240))
        self.vel = pygame.math.Vector2((0, 0))
        self.acc = pygame.math.Vector2((0, 0))
        self.direction = "RIGHT"

    def move(self, dt):
        if abs(self.vel.x) > Settings.RUN_THRESHOLD:
            self.running = True
        else:
            self.running = False

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -Settings.ACCELERATION_FACTOR

        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = Settings.ACCELERATION_FACTOR

        self.acc.x += self.vel.x * Settings.FRICTION_FACTOR
        self.vel += self.acc * dt
        self.pos += self.vel * dt

        if self.pos.x > Settings.WINDOW_WIDTH:
            self.pos.x = 0

        if self.pos.x < 0:
            self.pos.x = Settings.WINDOW_WIDTH

        self.rect.midbottom = self.pos
        self.acc = pygame.math.Vector2(0, 0)