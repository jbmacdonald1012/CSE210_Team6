import random

class Words:
    __wordList = ['constitucional', 'principles', 'policies', 'obscurity', 'empowers', 'concurrent', 'inquiry', 'constructions', 'visionary', 'probability', 'argument', 'western', 'representatives', 'independence', 'proposed', 'judiciary', 'legislative', 'exigencies', 'amendment']
    
    def selectRandom(__wordList):
        return random.choice(__wordList).upper()
    
    #this print fucntion was create to check the random words selection
    #print("The word is: ", selectRandom(__wordList))