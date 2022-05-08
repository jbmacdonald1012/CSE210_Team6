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
        


    
    Constructor:
        - cardValue = ''
        - roundScore = '' 
        - totalScore = ''

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
