game_board = [
  [2, 7, 3, 1, 0, 0, 0, 5, 0],
  [5, 0, 0, 0, 0, 9, 3, 0, 1],
  [0, 0, 8, 0, 0, 0, 2, 6, 7],
  [7, 0, 0, 0, 0, 0, 0, 0, 0],
  [9, 0, 1, 5, 2, 7, 8, 0, 6],
  [0, 0, 0, 0, 0, 0, 0, 0, 5],
  [3, 4, 9, 0, 0, 0, 5, 0, 0],
  [6, 0, 7, 8, 0, 0, 0, 0, 3],
  [0, 2, 0, 0, 0, 3, 6, 1, 9]
]

empty_cell_locs_array = []

def standard_input():
  yield 'Danny'

def findEmptyCell(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return (i, j)
  
  return None

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

def validCell(row, col, board, cell_value): 
  # Check if the row is valid
  for i in range(9):
    if i != col:
      if board[row][i] == cell_value:
        return False

  # Check if the column is valid
  for i in range(9):
    if i != row:
      if board[i][col] == cell_value:
        return False

  # Check if the subgrid is valid
  sub_grid_no = getSubgrid(row, col)

  if sub_grid_no == 1:
    for i in range(3):
      for k in range(3):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False
  elif sub_grid_no == 2:
    for i in range(3):
      for k in range(3, 6):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False
  elif sub_grid_no == 3:
    for i in range(3):
      for k in range(6, 9):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False
  elif sub_grid_no == 4:
    for i in range(3, 6):
      for k in range(3):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False
  elif sub_grid_no == 5:
    for i in range(3, 6):
      for k in range(3, 6):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False
  elif sub_grid_no == 6:
    for i in range(3, 6):
      for k in range(6, 9):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False
  elif sub_grid_no == 7:
    for i in range(6, 9):
      for k in range(3):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False
  elif sub_grid_no == 8:
    for i in range(6, 9):
      for k in range(3, 6):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False
  elif sub_grid_no == 9:
    for i in range(6, 9):
      for k in range(6, 9):
        if (i == row and col == k) == False:
          if board[i][k] == cell_value:
            return False

  # Return if the cell is valid
  return True

def solveBoard(board):
  found = findEmptyCell(board)
  if not found:
    return True
  else:
    row, col = found

  # Assign a value to the specified cell and validate it
  for i in range(1, 10):
    if validCell(row, col, board, i):   
      board[row][col] = i  
      if solveBoard(board):
        return True
      
      board[row][col] = 0
        
  return False

def startGame(board):
  name = input('What is your name sudoku master? ')

  while name.isalpha() == False:
    name = input('Please enter a valid name: ')

  print(f'Hello Sudoku Master {name}!')

  print('Here is today\'s sudoku board: ')

  print("\n")
  for r in range(9):
    for c in range(9):
      print(board[r][c], end="   ")
    print('\n')

  solveBoard(board)

  print('\nYour solved puzzle!: \n')

  for r in range(9):
    for c in range(9):
      print(board[r][c], end="   ")
    print('\n')
  
def main():
  startGame(game_board)

main()