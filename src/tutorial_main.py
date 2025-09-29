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
        # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
        # self.acc = vec(0,0.5)

        # Will set running to False if the player has slowed down to a certain extent
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        # Returns the current key presses
        pressed_keys = pygame.key.get_pressed()

        # Accelerates the player in the direction of the key press
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACCELERATION_FACTOR
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACCELERATION_FACTOR

            # Formulas to calculate velocity while accounting for friction
        self.acc.x += self.vel.x * FRICTION_FACTOR
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values

        # This causes character warping from one point of the screen to the other
        if self.pos.x > WINDOW_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WINDOW_WIDTH

        self.rect.midbottom = self.pos  # Update rect with new pos

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
    player.move()
    display_surface.blit(player.image, player.rect)

    pygame.display.update()
    FRAMES_PER_SECOND_CLOCK.tick(FRAMES_PER_SECOND)
