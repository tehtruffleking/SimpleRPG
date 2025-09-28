import pygame
import random
import sys


from pygame.locals import *
from tkinter import *
from tkinter import filedialog

#initialize game
pygame.init()


# system variables
WINDOW_HEIGHT = 350
WINDOW_WIDTH = 700
FRAMES_PER_SECOND = 60
FRAMES_PER_SECOND_CLOCK = pygame.time.Clock()
COUNT = 0


# physics variables
ACCELERATION_FACTOR = 0.3
FRICTION_FACTOR = -0.10
VECTOR = pygame.math.Vector2


# build and initialize display
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("RPG Game")


# primary classes
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("C:/Users/Christian/PycharmProjects/SimpleRPG/data/images/Background.png")
        self.bgY = 0
        self.bgX = 0

    def render(self):
        display_surface.blit(self.bgimage, (self.bgX, self.bgY))


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Christian/PycharmProjects/SimpleRPG/data/images/Ground.png")
        self.rect = self.image.get_rect(center=(350, 350))

    def render(self):
        display_surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Christian/PycharmProjects/SimpleRPG/data/sprites/Player_Sprite_R.png")
        self.rect = self.image.get_rect()

        self.vx = 0
        self.pos = VECTOR((340, 240))
        self.vel = VECTOR((0, 0))
        self.acc = VECTOR((0, 0))
        self.direction = "RIGHT"

    def move(self):
        pass

    def update(self):
        pass

    def attack(self):
        pass

    def jump(self):
        pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


background = Background()
ground = Ground()
player = Player()

# main game loop
while True:

    for event in pygame.event.get():

        # game quit and system exit code run on mouse click of exit button on screen
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # logic to manage left clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        # logic to manage key presses
        if event.type == pygame.KEYDOWN:
            pass

    background.render()
    ground.render()
    display_surface.blit(player.image, player.rect)

    pygame.display.update()
    FRAMES_PER_SECOND_CLOCK.tick(FRAMES_PER_SECOND)
