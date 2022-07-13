from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        if stats.get_score_1() == 5 or stats.get_score_2() == 5 :
            callback.on_next(GAME_OVER)