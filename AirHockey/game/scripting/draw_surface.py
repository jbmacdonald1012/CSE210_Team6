from constants import *
from game.scripting.action import Action

class DrawSurface(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        surface = cast.get_first_actor(SURFACE_GROUP)
        body = surface.get_body()

        if surface.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = surface.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)