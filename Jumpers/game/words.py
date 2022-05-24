import random

class Words:
    
    def __init__ (self):
        self._wordList = ['sense', 'cause', 'other', 'power', 'point', 'plain', 'union', 'third', 'every', 'local', 'which', 'judge', 'place', 'small', 'grant', 'state', 'among', 'right', 'under', 'great', 'grown']
    
    def selectRandom(self):
        return random.choice(self._wordList).upper()
    
    #this print fucntion was create to check the random words selection
    #print("The word is: ", selectRandom(_wordList))