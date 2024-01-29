#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Update the game board with the user input
def markBoard(position, mark):
    board.update({position:mark})


# Print the game board as described at the top of this code skeleton
def printBoard():
  def boardFiller(board):
    a = [1,2,3,4,5,6,7,8,9]
    for k in board.keys():
      if board[k] != ' ':
        a.pop(k-1)
        a.insert(k-1,board[k])
    return a 
    
  b = boardFiller(board)
  
  print()
  print(' ' + str(b[0]) + ' | ' + str(b[1]) + ' | ' + str(b[2]) +\
       '       ' +\
        board[1] + ' | ' + board[2] + ' | ' + board[3])
  
  print(' ---------       --+---+--')
  
  print(' ' + str(b[3]) + ' | ' + str(b[4]) + ' | ' + str(b[5]) +\
       '       ' +\
        board[4] + ' | ' + board[5] + ' | ' + board[6])
  
  print(' ---------       --+---+--')
  
  print(' ' + str(b[6]) + ' | ' + str(b[7]) + ' | ' + str(b[8]) +\
       '       ' +\
        board[7] + ' | ' + board[8] + ' | ' + board[9])
  
  print()  


# check for wrong input, this function should return True or False.
# True denoting that the user input is correct
def validateMove(position):
    try: 
        position = int(position)
        if position not in range(len(board)+1):
            return False
        elif board[position] != ' ':
            print("Box number [{}] is occupied".format(position))
            return False
    except:
        return False
    else:
        return True


# List of all the winning combinations
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# Implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    for a in winCombinations:
        if board[a[0]] == board[a[1]] == board[a[2]] == player:
            print("Player {} Wins!".format(player))
            return True
    return False


# Implement a function to check if the game board is already full
# For tic-tac-toe, tie basically means the whole board is already occupied
# This function should return with boolean
def checkFull():
    count = 0
    for k in board.keys():
        if board[k] == 'X' or board[k] == 'O':
            count +=1
        if count == 9:
            print('Board is full, the game ends in a Tie\n')
            return True
    return False
    

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# The game play logic
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while not gameEnded:
    move = input(currentTurnPlayer + "'s turn, input: ")
    if validateMove(move) == False:
        print('Please try again\n')
        continue
    move = int(move)
    markBoard(move,currentTurnPlayer)
    printBoard()
    if checkWin(currentTurnPlayer) == True or checkFull() == True:
        if input('Play again? Yes (Y/y) / No (Any key): ').upper() == 'Y':
            for k in board.keys():
                board[k] = ' '
            print('\nGame started:')
            printBoard()
            continue
        else:
            print('Thank you for playing')
            break
    if currentTurnPlayer == 'X':
      currentTurnPlayer = 'O'
    else:
      currentTurnPlayer = 'X'

