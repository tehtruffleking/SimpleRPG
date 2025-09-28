import pygame
import settings as Settings
from asset_loader import load_image


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image(Settings.GROUND_PATH)
        self.rect = self.image.get_rect(center=(350, 350))

    def render(self, display_surface: pygame.Surface):
        display_surface.blit(self.image, (self.rect.x, self.rect.y))