class cards:
    """ A set of cards that be drawn to provide a random integer between 1 and 13
    The resonsibilty of the cards is to keep track of the cards drawn and calculate 
    the points for it

    Attributes:
        value (int): The number on the card that is drawn."""

    def __init__(self):
        """Constructs a new instance of cards.

        Args:
            self (cards): An instance of cards.
        """
        
        self.value = 0
        self.roundscore = 0
        
"""    
    Constructor:
        - cardValue = ''
        - roundScore = '' 
        - totalScore = 300

    Methods:
        - drawCard(cardValue)
            -Random integer from 1 - 13
            -display card
        
        - updateScore(roundScore, totalScore)
            - calculate 
            - evaluateScore
                if totalScore < 0
                    print Game Over
                else
                    -display score
                    
        -restartValues (roundScore, totalScore)
            -totalScore: 300
            -roundScore: 0                    
"""

class player:

    """A person who play the game. 
    
    The responsibility of a player is to control the sequence of play.

    Attributes:
        - playerInput (string): choice of user, "higher" or "lower"
        - continueGameChoice (boolean) = whether or not the game continue
    """
    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self.playerInput = ""
        self.continueGameChoice = True
    
    def keepPlaying (self) :
        continuegame = input("continue playing? [y/n]: ")
        self.continueGameChoice = (continuegame == "y")

    def playerGuess (self) :
        self.playerInput = int(input("higher or lower? "))

    def startOver (self) :
        continuegame = input("do you want to start over [y/n]: ")
        self.continueGameChoice = (continuegame == "y")
