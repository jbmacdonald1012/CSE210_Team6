# Week 2 - Tic Tac Toe 
# Author: Jason Macdonald

def main():
    
    welcome()

    game = buildGameboard()
    player = nextTurn('')
    
    while not (winner(game) or stalemate(game)):
        showGameboard(game)
        claimSpot(player, game)
        player = nextTurn(player)

    showGameboard(game)
    closingMessage()

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

def winner(game):
    return(
        game[0] == game[1] == game[2] or
        game[3] == game[4] == game[5] or
        game[6] == game[7] == game[8] or
        game[0] == game[3] == game[6] or
        game[1] == game[4] == game[7] or
        game[2] == game[5] == game[8] or
        game[0] == game[4] == game[8] or
        game[2] == game[4] == game[6]
)

def stalemate(game):
    for area in range(9):
        if game[area] != 'X' and game[area] != 'O':
            return False
    return True

def claimSpot(player, game):
    spot = int(input(f'Player {player}\'s turn. Please select where you want to place your piece (Areas 1 - 9): '))

    if player == 1:
        game[area - 1] = 'X'
    elif player == 2:
        game[area -1] = 'O'

def nextTurn(turn):
    if turn == '' or turn == 2:
        return 1
    elif turn == 1:
        return 2

def closingMessage():
    print()
    print('Your session is over. Good game well played. Have a good one!')

if __name__ == "__main__":
    main()

    