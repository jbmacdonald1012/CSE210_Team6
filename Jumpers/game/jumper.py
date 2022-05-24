from terminal_service import TerminalService
class jumper :
    """The person who jump. 
    
    The responsibility of Jumper is to show the jumper and parachute 
    
    Attributes:
        _draw_start [list(string)]: initial state of jumper.
        _draw_state [List[string]]: Actual state of jumper.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._draw_start = []
        self._draw_state = []
        self._terminal_service = TerminalService()
    
    def draw(self):
            for item in self._draw_state :
                self._terminal_service.write_text(item)


    def get_start(self):
        self._draw_start= [
            '  _____  ',
            ' /_____\ ',
            ' \     / ',
            '  \   /  ',
            '    o    ',
            '   /|\   ',
            '   / \   ',
            '         ',
            '^^^^^^^^^'
        ]
        self._draw_state = self._draw_start
        self.draw()

    

    def delete_parachute(self, letter_guessed):
        if not letter_guessed :
            self._draw_state.pop(0)
        self.draw()

    def jumper_dead(self):
        self._draw_state[0] = "    x    "
        self.draw()    




