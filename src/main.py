import pygame
import sys
import settings as Settings

from background import Background
from ground import Ground
from player import Player

# main game loop
def main():
    # initialize game
    pygame.init()

    # system variables
    clock = pygame.time.Clock()

    # physics variables
    # VECTOR = pygame.math.Vector2

    # build and initialize display
    display_surface = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    pygame.display.set_caption("RPG Game")

    background = Background()
    ground = Ground()
    player = Player()

    game_running = True
    while game_running:
        dt = clock.tick(Settings.FRAMES_PER_SECOND) / 1000.0

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

        player.move(dt)
        background.render(display_surface)
        ground.render(display_surface)
        display_surface.blit(player.image, player.rect)

        pygame.display.update()
        # clock.tick(Settings.FRAMES_PER_SECOND)

if __name__ == "__main__":
    main()