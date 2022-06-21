import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle1 import Cycle1
from game.casting.cycle2 import Cycle2
from game.scripting.script import Script
from game.scripting.controlActorsAction import ControlActorsAction
from game.scripting.moveActorsAction import MoveActorsAction
from game.scripting.handleCollisionsAction import HandleCollisionsAction
from game.scripting.drawActorsAction import DrawActorsAction
from game.directing.director import Director
from game.services.keyboardServices import KeyboardService
from game.services.videoServices import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cycle1", Cycle1())
    cast.add_actor("cycle2", Cycle2())
    cast.add_actor("score1", Score(1))
    cast.add_actor("score2", Score(2))

   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()