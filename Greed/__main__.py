import os
import random

from game.casting.actor import Actor
from game.casting.score import Score
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point



FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_OBJECTS = 60


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Score()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the hero
    x = int(MAX_X / 2)
    #position y in the second line
    y = int(MAX_Y-(CELL_SIZE*2))
    position = Point(x, y)

    hero = Actor()
    hero.set_text("#")
    hero.set_font_size(FONT_SIZE)
    hero.set_color(WHITE)
    hero.set_position(position)
    cast.add_actor("heros", hero)
    
    
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()