from terminal_service import TerminalService
from jumper import Jumper

class Director:
    def __init__(self):
        self.isPlaying = True
        self.input = ""
        self.update = ""


    def startGame(self):
        """ Runs the game loop

        Args:
            self(Director): an instance of Director.
        """
        while self.isPlaying:
            self.getInputs()
            self.doUpdates()
            self.doOutputs()

    def getInputs(self):
        service = TerminalService()
        self.input = service.read_text(prompt)


    