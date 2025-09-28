import pygame
import settings as Settings
from asset_loader import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image(Settings.BACKGROUND_PATH, alpha=False)
        self.rect = self.image.get_rect(topleft=(0, 0))

    def render(self, display_surface: pygame.Surface):
        display_surface.blit(self.image, self.rect)