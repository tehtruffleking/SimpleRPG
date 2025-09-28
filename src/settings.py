from pathlib import Path

# system variables
WINDOW_HEIGHT = 350
WINDOW_WIDTH = 700
FRAMES_PER_SECOND = 60
COUNT = 0


# physics variables
ACCELERATION_FACTOR = 0.3
FRICTION_FACTOR = -0.10

# data root
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "data"
IMAGE_PATH = ASSETS / "images"
SPRITE_PATH = ASSETS / "sprites"
GROUND_PATH = IMAGE_PATH / "Ground.png"
BACKGROUND_PATH = IMAGE_PATH / "Background.png"
DEFAULT_SPRITE_PATH = SPRITE_PATH / "Player_Sprite_R.png"