'''
Introduction to Programming
2018-19 First Trimester
Lab 3 - Lists

Objective
The objective of this lab is to code the Connect 4 game. You can see an example
in the followin link: https://c4arena.com/

The aim is to get 4 pieces in a row, in horizontal, vertical or diagonal. The
first player in getting 4 in a row, wins the game.
'''
import turtle
from random import randint

# Function to draw the board with empty circles
def print_board_circles(height, width, x, y, cursor, radius):
  cursor.penup()
  cursor.setpos(x, y)
  cursor.pendown()
  for i in range(height): 
    for j in range(width):
      cursor.circle(radius)
      cursor.penup()
      cursor.forward(radius*2)
      cursor.pendown()
    cursor.penup()
    cursor.setpos(x, y+radius*2*(i+1))
    cursor.pendown()
  # Writes the column numbers
  cursor.penup()
  cursor.setpos(x-radius*2, y-radius*1.5)
  cursor.pendown()
  cursor.pencolor('green')
  for i in range(width):
    cursor.penup()
    cursor.forward(radius*2)
    cursor.write(i+1, align='center', font=('Arial', 20, 'bold'))

# Draws a circle at the given point of the given color
def print_circle(x, y, cursor, radius, row, col, color):
  cursor.penup()
  cursor.setpos(x+radius*2*col, y+radius*2*row)
  cursor.pendown()
  cursor.pencolor('gray')
  cursor.fillcolor(color)
  cursor.begin_fill()
  cursor.circle(radius)
  cursor.end_fill()

# Draws a green circle at each position of the given sequence
def draw_sequence(x, y, cursor, radius, sequence):
  cursor.pensize(7)
  for row, col in sequence:
    cursor.penup()
    cursor.setpos(x+radius*2*col, y+radius*2*row)
    cursor.pendown()
    cursor.pencolor('green')
    cursor.circle(radius)

# Returns an integer from the user input
def get_int_from_input(msg):
  while True:
    try:
      return int(input(msg))
    except ValueError:
      print('Please enter a valid integer value')

# Returns an integer betwen a and b (included) from the user input
def get_option(a, b, msg='Select an option: '):
  option = get_int_from_input(msg)
  while option < a or option > b:
    option = get_int_from_input('Invalid input! Try again: ')
  return option

# Returns the values and de coordinates of the row at the position r and c
def get_row(mat, r, c):
  row = mat[r]
  coords = [(r, i) for i in range(len(row))]
  return row, coords

# Returns the values and de coordinates of the column at the position r and c
def get_col(mat, r, c):
  col = [row[c] for row in mat]
  coords = [(i, c) for i in range(len(mat))]
  return col, coords

# Returns the values and de coordinates of the diagonal at the position r and c
def get_dig(mat, r, c):
  off = c - r
  coords = [(i, i+off) for i in range(len(mat)) if 0 <= i+off < len(mat[i])]
  dig = [mat[row][col] for row, col in coords]
  return dig, coords

# Returns the values and de coordinates of the counter diagonal at r and c
def get_cdg(mat, r, c):
  flip_horizontal_mat = [row[::-1] for row in mat]
  width = len(mat[0]) - 1
  new_c = width - c
  cdg, coords = get_dig(flip_horizontal_mat, r, new_c)
  # Flip de column coordinates back
  coords = [(row, width-col) for row, col in coords]
  return cdg, coords

# Converts and array into a string joining all the elements
def list_stringify(list):
  return ''.join([str(ele) for ele in list])

# Returns the list of the coordinates that corresponds to the values that maches
# the sequence. Returns an empty list if the sequence is not present in the
# values
def check_sequence(values, coords, sequence):
  try:
    index = list_stringify(values).index(sequence)
    return coords[index:index + len(sequence)]
  except ValueError:
    return []

# Returns if there is a combination of 4-on-line 'player' codes in any of the
# four directions 
def check_winner(mat, r, c, player, on_line=4):
  sequence = str(player) * on_line
  # Check the four directions, if there is a sequence in any of them return a
  # list containing the coordinates of the positions that make the sequence
  row = check_sequence(*get_row(mat, r, c), sequence)
  if row: return row
  col = check_sequence(*get_col(mat, r, c), sequence)
  if col: return col
  dig = check_sequence(*get_dig(mat, r, c), sequence)
  if dig: return dig
  cdg = check_sequence(*get_cdg(mat, r, c), sequence)
  if cdg: return cdg
  # Return an empty list otherwise
  return []

# Plays in the given column, updates de board and the marker vector, and returns
# accordingly to the result:
# -1 (Error): If the given column is full
#  0 (Nothing): If is a valid play but doesn't connect 4-on-line
#  1 (Winner): If the play connects 4-on-line
#  2 (Draw): If the board is full and no player connected 4-on-line
def play(height, width, x, y, cursor, radius, mat, top, col, player):
  # Player colors
  colors = ('Yellow', 'Red')
  # Get the row where the coin will fall
  row = top[col]
  # If the column is full return -1
  if not row < len(mat):
    return -1
  # Put the coin on the board
  mat[row][col] = player
  # Prints the move to the board
  print_circle(x, y, cursor, radius, row, col, colors[player])
  # Check if there is a winner sequence, if there is draw the sequence and
  # return 1
  sequence = check_winner(mat, row, col, player)
  if sequence:
    draw_sequence(x, y, cursor, radius, sequence)
    return 1
  # Substract one from the index that points to the next free spot
  top[col] += 1
  # Check if there still is space to play
  for i in top:
    if i < len(mat):
      return 0
  # If there is no space left to play return 2 (Draw)
  return 2

# Ask the user for a column to play and returns its value
def player_play(mat, top):
  move = get_option(1, len(mat[0]), msg='Select a column: ') - 1
  while not top[move] < len(mat):
    print('The column {} is full, try another one.'.format(move+1))
    move = get_option(1, len(mat[0]), msg='Select a column: ') - 1
  return move

# A.I. Given a state matrix and the player code calculates the best next move
def computer_play(mat, top, player):
  # Try making 4-on-line for each of the columns possible
  for col, row in enumerate(top):
    if row < len(mat):
      mat[row][col] = player
      winner = check_winner(mat, row, col, player)
      mat[row][col] = 2
      if winner:
        return col
  # Switch the player
  player ^= 1
  # See if the enemy could make 4-on-line for each of the columns possible
  for col, row in enumerate(top):
    if row < len(mat):
      mat[row][col] = player
      winner = check_winner(mat, row, col, player)
      mat[row][col] = 2
      if winner:
        return col
  # If doesn't find any of the previous combinations play a random move
  move = randint(0, len(mat[0])-1)
  while not top[move] < len(mat):
    move = randint(0, len(mat[0])-1)
  return move

# Game logic of 2 players mode (0), player against machine mode (1) and machine
# agains machine mode (2)
def play_game(height, width, x, y, cursor, radius, mode=0):
  # Player colors
  colors = ('Yellow', 'Red')
  # Inicial player is choosed randomly
  player = randint(0, 1)
  # Game matrix
  mat = [[2] * width for _ in range(height)]
  # Vector of de indices of the next free position of each column, the initial
  # value will be height-1 since the bottom most positions are the last in the
  # matrix
  top = [0] * width
  # Prints the board in turtle
  print_board_circles(height, width, x, y, cursor, radius)
  # Infinite game loop
  while True:
    print('{}\'s turn.'.format(colors[player]))
    # Get the column to play depending of the mode and the player turn
    if mode == 2 or mode == 1 and player == 1:
      move = computer_play(mat, top, player)
      print('Machine plays on column {}'.format(move+1))
    else:
      move = player_play(mat, top)
    # Plays on the column chosen and saves the result
    result = play(height, width, x, y, cursor, radius, mat, top, move, player)
    # If the result is OK switch the current player's turn
    if result == 0:
      player ^= 1
    # If the result is Winner sequence then print it and end the game loop
    if result == 1:
      print('Player {} connects 4-on-line and wins the game!'
        .format(colors[player]))
      break
    # If the result is Draw print it and end the game loop
    if result == 2:
      print('No player connects 4-on-line. The game ends in a draw!')
      break

# Main menu function
def main_menu(height, width, x, y, cursor, radius):
  options = ('Player vs Player', 'Player vs Machine', 'Machine vs Machine')
  for i in range(len(options)):
    print('{}. {}'.format(i+1, options[i]))
  option = get_option(1, len(options), msg='Choose an option: ')
  play_game(height, width, x, y, cursor, radius, mode=option-1)

# Creates the window and performs some settings
window = turtle.Screen()
window.bgcolor('white')
window.title('Connect 4')
window.setup(500, 500)
window.reset()

cursor = turtle.Turtle()
cursor.hideturtle()
cursor.pensize(3)
cursor.pencolor('gray')
cursor.speed(0)

# Board Properties
height = 6
width = 7
x = -150
y = -150
radius = 25

# Calls the main menu function
main_menu(height, width, x, y, cursor, radius)

turtle.done()
try:
  turtle.bye()
except:
  print('Game Over!')
