Create 2 classes: 

Class 1 - Cards - Shawn Jensen

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
Class 2 - Player - Victor
    
    Constructor:
        - playerInput = ""
        - continueGameChoice = ""

    Methods:
        - keepPlaying(continueGameChoice)
            - print to user 'Play Again'
            evaluate user input
        
        -playerGuess(playerInput)
            - guess = Player()
            guess.playerInput = int(input('Higher or Lower? '))

        -startOver(playerInput)
            -start the game again

Game Functionality - Jason

def main():
    
    code here to play game 

    set class instances
        player = Player()
        card = Cards()
        
    call class functions
        while  player.continueGameChoice
            player.playerGuess()
            card.drawCard()
            card.updateScore()
            if card.updateScore() < 0
                - player.startOver()
                if player.continueGameChoice
                    card.restartvalues
            else
                - player.keepPlaying()



if __name__ = '__main__':
    main()

Testing / Debugging - Alberto