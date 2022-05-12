import random

class Cards:
    """ A set of cards that be drawn to provide a random integer between 1 and 13
    Attributes:
        value (int): The number on the card that is drawn."""

    def __init__(self):
        """Constructs a new instance of cards.
        Args:
            self (cards): An instance of cards.
        """
        
        self.cardvalue = 0
        self.previouscard = 0
        self.total = 300
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
                if totalScore <= 0
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

    def setPreviousCard(self):
        self.previouscard = self.cardvalue

    def playerGuess (self) :
        self.playerInput = (input("higher or lower? "))

    def updatescore(self):
        if self.cardvalue > self.previouscard:
            if self.playerInput.lower() == "h": 
                self.total += 100
            else:
                self.total -= 75
        elif self.cardvalue < self.previouscard:
            if self.playerInput.lower() == 'l':
                self.total += 100
            else:
                self.total -= 75

        print(f"Your score is: {self.total}")

        
class Player:

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
        self.playerInput = input("continue playing? [y/n]: ")
        return self.playerInput

    def startOver (self) :
        self.playerInput = input("do you want to start over [y/n]: ")
        return self.playerInput

def main():
    
    card = Cards()
    player = Player()

    gameplay(card, player)

def gameplay(card, player):
    card.drawcard()
    card.setPreviousCard()
    card.playerGuess()
    card.drawcard()
    card.updatescore()

    if card.total <= 0: 
        print('Game Over. Your score is less than 0.')
        print()
        restart = player.startOver()
        print()
        
        if restart.lower() == 'y':
            gameplay(card, player)
        elif restart.lower() != 'y':
            exit()
            
    choice = player.keepPlaying()
    print()

    if choice.lower() == 'y': 
        gameplay(card, player)
    else: 
        exit()

if __name__ == "__main__":
    main()