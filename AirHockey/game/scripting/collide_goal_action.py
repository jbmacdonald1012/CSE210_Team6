from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideGoalAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(PUCK_GROUP)
        # set constant for goal 
        goal_a,goal_b = cast.get_actors(GOAL_GROUP)
        stat_a, stat_b = cast.get_actors(STATS_GROUP)

        ball_body = ball.get_body()
        goal_a_body = goal_a.get_body()
        goal_b_body = goal_b.get_body()

        if self._physics_service.has_collided(ball_body, goal_a_body):
            #ball.bounce_y()
            # ADD GOAL SOUND
            goal = Sound(GOAL)

            self._audio_service.play_sound(goal)
            #points = goal_a.get_points()
            stat_b.add_points(1)
            print("POINTS")

        if self._physics_service.has_collided(ball_body, goal_b_body):
            #ball.bounce_y()
            # ADD GOAL SOUND
            goal = Sound(GOAL)
            self._audio_service.play_sound(goal)
            #points = goal_b.get_points()
            stat_a.add_points(1)
            print("POINTS")