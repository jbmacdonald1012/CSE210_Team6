from terminal_service import TerminalService
from jumper import Jumper
from words import Words

class Director:
    def __init__(self):
        self.isPlaying = True
        self._word = Words()
        self._jumper = Jumper()
        self._terminal_service = TerminalService()


    def startGame(self):
        """ Runs the game loop

        Args:
            self(Director): an instance of Director.
        """
        gameWord = setWord(self)
        
        while self.isPlaying:
            self.getInputs()
            self.doUpdates()
            self.doOutputs()


    def getInputs(self):
        prompt = self._terminal_service.letter_guess('Guess a letter [a-z]: ')


    def doUpdates(self, gameWord):
        self._jumper.validate_guess(prompt)



    def doOutputs(self):
        self._jumper.get_start()

    def setWord(self):
        word = self._word.selectRandom()







    