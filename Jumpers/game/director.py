from terminal_service import TerminalService

class Director:
    def __init__(self):
        self.isPlaying = True
        self.input = ""


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