import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction2(Action):
    """
    An input that controls each cyclist.

    ControlActorsAction gets the direction and moves the cyclist. 

    Attributes:
        _keyboard_service(KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """ Constructs a new ControlActorsAction using KeyboardService.

            Args:
                keyboard_service (KeyboardService): An instance of Keyboard Service.

        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE,0)


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        #left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)

        #right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)

        #up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)

        #down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)

        cycle2 = cast.get_first_actor('cycle2')
        cycle2.turn_head(self._direction)