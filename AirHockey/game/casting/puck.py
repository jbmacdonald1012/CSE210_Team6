import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point

class Puck(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Puck.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def bounce_x(self, velocity_object):
        """Bounces the puck in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = (velocity.get_x() * rn * -1) + velocity_object
        vy = velocity.get_y()
        if vx > 18 :
            vx = 18
        if vy > 18 :
            vy = 18    
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self, velocity_object):
        """Bounces the puck in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = (velocity.get_y() * rn * -1) + velocity_object 
        if vx > 18 :
            vx = 18
        if vy > 18 :
            vy = 18 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the puck's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the puck's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def release(self):
        """Release the puck in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-PUCK_VELOCITY * rn, PUCK_VELOCITY * rn])
        vy = -PUCK_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)