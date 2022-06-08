from game.shared.point import Point
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.frame_create=0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of actors.
        """
        hero = cast.get_first_actor("heros")
        velocity = self._keyboard_service.get_direction()
        hero.set_velocity(velocity)  

        if self.frame_create == 6:
            cast.add_rock()   
            self.frame_create = 0
        else: 
            self.frame_create += 1

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with gems or rocks.
        
        Args:
            cast (Cast): The cast of actors.
        """       
        

        banner = cast.get_first_actor("banners")
        hero = cast.get_first_actor("heros")
        artifacts = cast.get_actors("artifacts")

        # banner.set_text("")
        banner.set_text(f"Score: {banner.get_score()}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        hero.move_next(max_x, max_y)

        
        for artifact in artifacts:
                # for when hero hits the artifact
            if hero.get_position().equals(artifact.get_position()):
                #message = artifact.get_message()
                #banner.set_text(message)   
                
                if artifact.get_text() == "*":
                # update points 
                    score = banner.get_score()
                    score += 1
                    banner.set_score(score) 
                elif artifact.get_text() == "0":
                # update points 
                    score = banner.get_score()
                    score -= 1
                    banner.set_score(score) 

                cast.remove_actor("artifacts", artifact) 

            # makes artifact move 
            if artifact.get_time() == 6:
                artifact.move_next(max_x, max_y)   
                artifact.change_time(-6)
            else: 
                artifact.change_time(1)
           
            if artifact.get_position().get_y()>= 585:
                cast.remove_actor("artifacts", artifact) 
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()