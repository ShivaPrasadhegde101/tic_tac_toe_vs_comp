import random


def draw(board):

    print("-----------------------------")
    print()
    print("%c  | %c |%c"%(board[1],board[2],board[3]))
    print("___|___|___")
    print("%c  | %c |%c"%(board[4],board[5],board[6]))
    print("___|___|___")
    print("%c  | %c |%c"%(board[7],board[8],board[9]))
    print("   |   |   ")
    print()
    print("-----------------------------")


def inputletter():

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def choose():
    
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play(board, letter, move):
    board[move] = letter


def check(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 


def newBoard(board):

    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def checkFree(board, move):
    return board[move] == ' '


def getPlayerMove(board):

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not checkFree(board, int(move)):
        print('What is ur next move? (1-9)')
        move = input()
    return int(move) 
    


def chooseRandomMoveFromList(board, movesList):

    possibleMoves = []
    for i in movesList:
        if checkFree(board, i):
            possibleMoves.append(i)


    if len(possibleMoves) != 0:
     return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'


    for i in range(1, 10):
        boardCopy = newBoard(board)
        if checkFree(boardCopy, i):
            play(boardCopy, computerLetter, i)
            if check(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = newBoard(board)
        if checkFree(boardCopy, i):
            play(boardCopy, playerLetter, i)
            if check(boardCopy, playerLetter):
                return i 


    move = chooseRandomMoveFromList(board, [1,3,7,9])

    if move != None:
        return move

    if checkFree(board, 5):
        return 5


    return chooseRandomMoveFromList(board, [2,4,6,8])


def checkFull(board):

    for i in range(1, 10):
        if checkFree(board, i):
            return False
    return True
    

print('Welcome to tic-tac-toe')


while True:

    t = [' '] * 10
    playerLetter, computerLetter = inputletter()
    turn = choose()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            draw(t)
            move = getPlayerMove(t)
            play(t, playerLetter, move)

            if check(t, playerLetter):
                draw(t)
                print('Yey! You have won the game!')
                gameIsPlaying = False
            else:
                if checkFull(t):
                    draw(t)
                    print('Tie game!')
                    break
                else:
                    turn = 'computer'

        else:

            move = getComputerMove(t, computerLetter)
            play(t, computerLetter, move)

            if check(t, computerLetter):
                draw(t)
                print('Computer has defeated you!')
                gameIsPlaying = False
            else:
                if checkFull(t):
                    draw(t)
                    print('Tie game!')
                    break
                else:
                    turn = 'player'

    print('Play again? (yes or no)')
    if not input().lower().startswith('y'):
        break 
