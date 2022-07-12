from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        puck = cast.get_first_actor(PUCK_GROUP)
        body = puck.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(SLIDE_HIT)
        goal_sound = Sound (GOAL)
        over_sound = Sound(OVER_SOUND)
       
      
        if x < FIELD_LEFT and y < 250 :
            puck.bounce_x(0)
            self._audio_service.play_sound(bounce_sound)
        elif x < FIELD_LEFT and y > (250 + 220 - PUCK_WIDTH) :
            puck.bounce_x(0)
            self._audio_service.play_sound(bounce_sound)
        elif x < FIELD_LEFT and y > 250 and y < (250 + 220 - PUCK_WIDTH):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.add_points_2()
            self._audio_service.play_sound(goal_sound)
            callback.on_next(TRY_AGAIN)
        elif x >= (FIELD_RIGHT - PUCK_WIDTH) and y < 250 :
            puck.bounce_x(0)
            self._audio_service.play_sound(bounce_sound)
        elif x >= (FIELD_RIGHT - PUCK_WIDTH) and y > (250 + 220 - PUCK_WIDTH) :
            puck.bounce_x(0)
            self._audio_service.play_sound(bounce_sound)
        elif x >= (FIELD_RIGHT - PUCK_WIDTH) and y > 250 and y < (250 + 220 - PUCK_WIDTH):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.add_points_1()
            self._audio_service.play_sound(goal_sound)
            callback.on_next(TRY_AGAIN)
        if y < FIELD_TOP:
            puck.bounce_y(0)
            self._audio_service.play_sound(bounce_sound)
        elif y >= (FIELD_BOTTOM - PUCK_HEIGHT):
            puck.bounce_y(0)
            self._audio_service.play_sound(bounce_sound)
            #stats = cast.get_first_actor(STATS_GROUP)
            #stats.lose_life()
            
            # if stats.get_lives() > 0:
            #     callback.on_next(TRY_AGAIN) 
            # else:
            #     callback.on_next(GAME_OVER)
            #     self._audio_service.play_sound(over_sound)