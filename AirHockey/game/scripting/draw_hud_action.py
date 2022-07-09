from constants import *
from game.scripting.action import Action
from game.casting.image import Image
from game.casting.point import Point

class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_actors(STATS_GROUP)
        self._draw_label(cast, SCORE_GROUP, SCORE_FORMAT, stats)

    def _draw_label(self, cast, group, format_str, data):
        labels = cast.get_actors(group)
        for i,label in enumerate(labels):
            text = label.get_text()
            text.set_value(format_str.format(data))
            position = label.get_position()
            self._video_service.draw_text(text, position)