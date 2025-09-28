import pygame
import sys
import settings as Settings

from background import Background
from ground import Ground

# main game loop
def main():
    # initialize game
    pygame.init()

    # system variables
    FRAMES_PER_SECOND_CLOCK = pygame.time.Clock()

    # physics variables
    VECTOR = pygame.math.Vector2

    # build and initialize display
    display_surface = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
    pygame.display.set_caption("RPG Game")

    background = Background()
    ground = Ground()

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

        background.render(display_surface)
        ground.render(display_surface)

        pygame.display.update()
        FRAMES_PER_SECOND_CLOCK.tick(Settings.FRAMES_PER_SECOND)

if __name__ == "__main__":
    main()