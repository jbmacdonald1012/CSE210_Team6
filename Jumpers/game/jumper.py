from terminal_service import TerminalService
from words import Words
class Jumper :
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
        self._word = Words()
        self._word_chose = ""
        self.words_space = []

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
        self._word_chose = self._word.selectRandom()
        for _ in range(0,len(self._word_chose)):
            self.words_space.append('_')    

    def validate_guess(self):
        if self._terminal_service.letter_guessed in self._word_chose:
            self.words_space[self._word_chose.index(self._terminal_service.letter_guessed)] = self._terminal_service.letter_guessed
        elif len(self._draw_state) <= 4 :
            self.jumper_dead()
        else:
            self._draw_state.pop(0)          

    def jumper_dead(self):
        self._draw_state[0] = "    x    "
        self.draw()    

