import pygame
from pygame import Surface
from pathlib import Path

def load_image(path: Path, alpha=True) -> Surface:
    img = pygame.image.load(str(path))
    return img.convert_alpha() if alpha else img.convert()

def load_sound(path: Path) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(str(path))
