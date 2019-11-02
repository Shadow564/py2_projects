from random import randint

board = []

print "Welcome To Battleship! There are two ships, a battleship and a carrier. Good luck!"

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

alt_ship_row = random_row(board)
alt_ship_col = random_col(board)

while alt_ship_row == ship_row and alt_ship_col == ship_col:
  alt_ship_row = random_row(board)
  alt_ship_col = random_col(board)

# Everything from here on should be in your for loop
# don't forget to properly indent!
done = 0
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    board[ship_row][ship_col] = "*"
    print_board(board)
    if turn == 3:
        print "Game Over."
        board[ship_row][ship_col] = "*"
        board[alt_ship_row][alt_ship_col] = "&"
  elif guess_row == alt_ship_row and guess_col == alt_ship_col:
    print "Congratulations! You sank my carrier!"
    board[alt_ship_row][alt_ship_col] = "&"
    print_board(board)
    if turn == 3:
        print "Game Over."
        board[ship_row][ship_col] = "*"
        board[alt_ship_row][alt_ship_col] = "&"
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
      if turn == 3:
        print "Game Over."
        board[ship_row][ship_col] = "*"
        board[alt_ship_row][alt_ship_col] = "&"
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
      if turn == 3:
        print "Game Over."
        board[ship_row][ship_col] = "*"
        board[alt_ship_row][alt_ship_col] = "&"
    else:
      print "You missed my ships!"
      board[guess_row][guess_col] = "X"
      if turn == 3:
        print "Game Over."
        board[ship_row][ship_col] = "*"
        board[alt_ship_row][alt_ship_col] = "&"
    print_board(board)
