# Week 2 - Tic Tac Toe 
# Author: Jason Macdonald

def main():
    
    welcome()
    game = buildGameboard()

    showGameboard(game)


def welcome():
    print('Let\'s play Tic Tac Toe!')
    print()

def buildGameboard():
    gameboard = []

    for area in range(9):
        gameboard.append(area + 1)
    return gameboard

def showGameboard(game):
    print()
    print()
    print(f'{game[0]} | {game[1]} | {game[2]}')
    print('---------')
    print(f'{game[3]} | {game[4]} | {game[5]}')
    print('---------')
    print(f'{game[6]} | {game[7]} | {game[8]}')
    print()
    print()



if __name__ == "__main__":
    main()

    