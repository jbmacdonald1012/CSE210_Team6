from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

"""
    Now let's modify the paddle's movement. Also the images and let us get the body
"""

class Paddle(Actor):
    """A implement used to hit and bounce the paddle in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the bat to the left."""
        velocity = Point(-PADDLE_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the bat to the right."""
        velocity = Point(PADDLE_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def swing_up(self):
        """Steers the bat to the right."""
        velocity = Point(0, -PADDLE_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_down(self):
        """Steers the bat to the right."""
        velocity = Point(0, PADDLE_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_upright(self):
        """Steers the bat to the right."""
        velocity = Point(PADDLE_VELOCITY/2, -PADDLE_VELOCITY/2)
        self._body.set_velocity(velocity)

    def swing_upleft(self):
        """Steers the bat to the right."""
        velocity = Point(-PADDLE_VELOCITY/2, -PADDLE_VELOCITY/2)
        self._body.set_velocity(velocity)

    def swing_downright(self):
        """Steers the bat to the right."""
        velocity = Point(PADDLE_VELOCITY/2, PADDLE_VELOCITY/2)
        self._body.set_velocity(velocity)

    def swing_downleft(self):
        """Steers the bat to the right."""
        velocity = Point(-PADDLE_VELOCITY/2, PADDLE_VELOCITY/2)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)
    
    def get_image(self):
        """Gets the PADDLE's image.
        
        Returns:
            An instance of Image.
        """
        return self._image