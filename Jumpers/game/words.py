import random

class Words:
    _wordList = ['sense', 'cause', 'other', 'power', 'point', 'plain', 'union', 'third', 'every', 'local', 'which', 'judge', 'place', 'small', 'grant', 'state', 'among', 'right', 'under', 'great', 'grown']
    
    def selectRandom(_wordList):
        return random.choice(_wordList).upper()
    
    #this print fucntion was create to check the random words selection
    #print("The word is: ", selectRandom(_wordList))