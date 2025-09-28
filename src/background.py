import pygame
import settings as Settings
from asset_loader import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = load_image(Settings.BACKGROUND_PATH)
        self.bgY = 0
        self.bgX = 0

    def render(self, display_surface: pygame.Surface):
        display_surface.blit(self.bgimage, (self.bgX, self.bgY))