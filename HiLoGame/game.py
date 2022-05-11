import random

class cards:
    """ A set of cards that be drawn to provide a random integer between 1 and 13
    Attributes:
        value (int): The number on the card that is drawn."""

    def __init__(self):
        """Constructs a new instance of cards.
        Args:
            self (cards): An instance of cards.
        """
        
        self.value = 0
        self.roundscore = 0
        self.playerInput = ""
      
    """    
    Constructor:
        -cardvalue = ''
        -roundScore = '' 
        -totalScore = 300
        -previous card = 0

    Methods:
        - drawCard(cardvalue)
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
    
    def drawcard(self):
        """Generates a new random value
        Args:
            self (card): An instance of card.
        """
        self.cardvalue = random.randint(1, 13)
        print(f'The card is {self.cardvalue}')

    def playerGuess (self) :
        self.playerInput = (input("higher or lower? "))

    def updatescore(self):
        if self.cardvalue > self.previouscard and self.playerInput.lower == "h": 
            self.total += 100
        elif self.cardvaule < self.previouscard and self.playerInput.lower == "l":
            self.total += 100
        elif self.cardvaule < self.previouscard and self.playerInput.lower == "h":
            self.total -= 75
        else:
            self.total -= 75

        
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

    def startOver (self) :
        continuegame = input("do you want to start over [y/n]: ")
        self.continueGameChoice = (continuegame == "y")

def main():
    player = Player()



if __main__ == "__main__":
    main()