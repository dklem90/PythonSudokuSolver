game_board = [
  [1, 0, 0, 2, 4, 7, 0, 0, 0], 
  [0, 0, 0, 9, 0, 0, 5, 0, 1], 
  [0, 8, 0, 5, 0, 0, 7, 0, 0], 
  [8, 4, 5, 0, 0, 2, 9, 3, 0], 
  [0, 0, 9, 0, 0, 0, 1, 0, 0], 
  [0, 7, 1, 6, 0, 0, 2, 5, 4], 
  [0, 7, 1, 6, 0, 0, 2, 5, 4], 
  [0, 0, 8, 0, 0, 4, 0, 9, 0], 
  [0, 0, 0, 3, 1, 9, 0, 0, 5]
]

def getSubgrid(row, col):
  sub_grid_no = 0

  if row < 3:
    if col < 3:
      sub_grid_no = 1
    elif col < 6:
      sub_grid_no = 2
    else:
      sub_grid_no = 3
  
  if row >= 3 and row < 6:
    if col < 3:
      sub_grid_no = 4
    elif col < 6:
      sub_grid_no = 5
    else:
      sub_grid_no = 6

  if row >= 6:
    if col < 3:
      sub_grid_no = 7
    elif col < 6:
      sub_grid_no = 8
    else:
      sub_grid_no = 9

  return sub_grid_no

def validCell(row, col, board):
  cell_value = board[row][col]
  is_valid = True

  # Check if the row is valid
  for i in range(9):
    if i != col:
      if board[row][i] == cell_value:
        is_valid = False

  # Check if the column is valid
  for i in range(9):
    if i != row:
      if board[i][col] == cell_value:
        is_valid = False

  # Check if the subgrid is valid
  sub_grid_no = getSubgrid(row, col)

  if sub_grid_no == 1:
    for i in range(3):
      for k in range(3):
        if i != row and col != k:
          if board[i][k] == cell_value:
            is_valid = False

  # Return if the cell is valid
  return is_valid

def solveBoard(row, col, board):
  if(len(board[row]) == col):
    row = row + 1
    col = 0

  if(board[row][col] != 0):
    col = col + 1  

  for i in range(1, 10):
    board[row][col] = i
    if(validCell(row, col, board)):
      print("\n")
      for row in board:
        print(row)
      solveBoard(row, col + 1, board)

  board[row][col] = 0

def startGame(board):
  name = input('What is your name sudoku master? ')

  while name.isalpha() == False:
    name = input('Please enter a valid name: ')

  print(f'Hello Sudoku Master {name}!')

  print('Here is today\'s sudoku board: ')

  for row in board:
    print(row)

  solveBoard(0, 0, game_board)
  
def main():
  startGame(game_board)

main()