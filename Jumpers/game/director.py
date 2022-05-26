from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.words import Words

class Director:
    def __init__(self):
        self.isPlaying = True
        self.word = Words()
        self.jumper = Jumper()
        self.terminal_service = TerminalService()
        self.gameWord = ""
        self.prompt = ""
        self.displayWord = []#['_' for letter in self.gameWord]
        self.guesses = []


    def startGame(self):
        """ Runs the game loop

        Args:
            self(Director): an instance of Director.
        """
        self.getWord()
        self.wordIndex()
        self.terminal_service.write_text(' '.join(self.displayWord))
        self.jumper.get_start()
        while self.isPlaying:
            self.getInputs()
            self.doUpdates()
            self.doOutputs()
    
    def getWord(self):
        self.gameWord = self.word.selectRandom()
        return self.gameWord

    def showWord(self):
        display = ' '.join(self.displayWord)
        return display
    
    def wordIndex(self):
        for _ in range(0,len(self.gameWord)):
            self.displayWord.append('_')    
        """
        locations = []
        for index, char in enumerate(list(self.gameWord)):
            if char == self.prompt:
                locations.append(index)
        return locations
        """
    def updateWord(self, index):
        for number in index:
            self.display[index] = self.prompt

    def validateGuess(self):
    #    if self.prompt == self.prompt.isalpha():
        if self.prompt in self.guesses:
                print('You already guessed this letter')
        elif self.prompt not in self.gameWord:
                print(self.prompt, 'is not in the word')
                self.jumper.incorrect_guess()
                self.guesses.append(self.prompt)
        else:
                print('Nice!', self.prompt, 'is in the word!')
                self.guesses.append(self.prompt)
                self.displayWord[self.gameWord.index(self.prompt)]=self.prompt
                #letterIndex = self.wordIndex(self)
                #self.updateWord(self, index)

    def checkForWin(self):
        display = ''.join(self.displayWord)
        word = self.gameWord

        if display == word and len(self.jumper._draw_state) > 5:
            self.isPlaying = False
            print('\n')
            print('Nice work! You Win!')
        elif len(self.jumper._draw_state) <= 5:
            self.isPlaying = False
            self.jumper._jumper_dead()
            print('\n')
            print('Sorry, you didn\'t guess the word' )
            print(f'The word was {self.gameWord}')

    def getInputs(self):
        self.prompt = self.terminal_service.read_text('Guess a letter [a-z]: ').upper()

    def doUpdates(self):
        #add self
        self.validateGuess()
        self.checkForWin()

    def doOutputs(self):
        wordState = self.showWord()
        self.terminal_service.write_text(wordState)
        self.terminal_service.write_text("")
        self.jumper.draw()
        
        #self.terminal_service.write_text(jumper)
    