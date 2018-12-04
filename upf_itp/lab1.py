'''
Introduction to Programming
2018-19 First Trimester
Lab 1 - Control Structures

1. Banknote breakdown - 2.5 points
Write a program that calculates the minimum breakdown into bills and coins of an
exact amount of euros. There are 500, 200, 100, 50, 20, 10 and 5 euro bills and
2 and 1 euro coins.

For example, if we want to know the breakdown of 434 euros, the program will
display the following result on the screen:   

2 200 euro banknotes 

1 20 euro banknote 

1 10 euro banknote 

2 2 euro banknotes

Make the program request quantities until the user enters a negative amount, in
which case the program will finish.
'''
def inputInt(msg):
  while True:
    try:
      return int(input(msg))
    except ValueError:
      print('please enter a valid integer value')

bank_notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
money = inputInt('money: ')
while money >= 0:
  for bank_note in bank_notes:
    if money >= bank_note:
      quantity = money // bank_note
      money -= bank_note * quantity
      print('{:d} {:d} euro banknote{}'
        .format(quantity, bank_note, 's' if quantity > 1 else ''))
  money = inputInt('money: ')


'''
2. Secret number (with limit number of attempts) - 2.5 points
Implement a program to play to guess the secret number against the computer.

*The computer "thinks" a random number between 0 and N (this limit is decided by
you - we suggest that it be 20 to not waste too much time guessing it).

*The computer asks the user for a number (between 0 and N).

*The computer communicates to the user if the number that he has entered is
greater, less or equal to the secret number, as well as the attempts that he has
left.

*In case it is not the same, it gives another opportunity, and so on, until the
user guesses, or until it has consumed M attempts (if N = 20, a reasonable
number of attempts would be M = 5).

*In the end, if we have guessed it, the computer will communicate us on how many
attempts we have made. Otherwise, it will tell us that we have consumed the M
attempts.
'''
from random import randint

def inputInt(msg):
  while True:
    try:
      return int(input(msg))
    except ValueError:
      print('please enter a valid integer value')

number_range = 20
number_attempts = int(number_range * 0.25)
secret_number = randint(0, number_range)
attempts = number_attempts

print('Hi, I\'m your computer, do you want to play with me?')
print('I thought of a number between 0 and {:d}, can you guess it? :)'
  .format(number_range))
print('I\'ll give you {:d} attempts'.format(number_attempts))

while attempts:
  guess = inputInt('make a guess: ')
  attempts -= 1

  if guess > secret_number: print('your guess is GREATER than my secret number')
  elif guess < secret_number: print('your guess is LESS than my secret number')
  else: break

  if attempts: print('you have {:d} attempt{} left'
    .format(attempts, 's' if attempts > 1 else ''))
  else: print('you have no attempts left')

if guess == secret_number:
  print('You got it RIGTH!! Congratulations :D')
  print('You used {:d} out of {:d} attempts'.
    format(number_attempts - attempts, number_attempts))
else:
  print('You used all your {:d} attempts and didn\'t get the number :('
    .format(number_attempts))
  print('The secret number I thought was {:d}'.format(secret_number))


'''
3. Vector calculation program with menu - 5 points
A vector in a three-dimensional space is a triplet of real values ​​(x, y, z). We
wish to create a program that allows to operate with two vectors. The user will
see a menu with the following options: 
  1) Enter vector A
  2) Enter vector B
  3) Calculate the sum
  4) Calculate the difference
  5) Calculate the scalar product
  6) Calculate the vector product
  7) Calculate the angle (in degrees) between them
  8) Calculate the length
  9) Finish

After the execution of each one of the actions of the menu, this will reappear
on the screen, unless the chosen option is number 9. If the user chooses a
different option, the program will warn the user of its error and the menu will
reappear.

Options 4 and 6 of the menu can provide different results depending on the order
of the operands, so, if any of them is chosen, a new menu must be shown that
allows to select the order of the operands. For example, option 4 will show the
following menu: 
  a) Vector A minus vector B
  b) Vector B minus vector A

Again, if the user makes a mistake, he will be warned of the error and will be
allowed to correct it. 
Option 8 of the main menu will also lead to a submenu for the user to decide
which of the two vectors the length calculation applies.

Keep in mind that your program should contemplate and control any possible
exceptional situation: divisions by zero, roots with negative argument, and so
on.
'''
import math

def inputInt(msg):
  while True:
    try:
      return int(input(msg))
    except ValueError:
      print('Please enter a valid integer value')

def get_option(a, b):
  option = inputInt('Select an option: ')
  while option < a or option > b:
    option = inputInt('Invalid option! Select an option: ')
  return option

def vector_diff_menu():
  print('1) Vector A minus vector B')
  print('2) Vector B minus vector A')
  if get_option(1, 2) == 1:
    print('The difference of {} minus {} is {}'.format(A, B, vector_diff(A, B)))
  else:
    print('The difference of {} minus {} is {}'.format(B, A, vector_diff(B, A)))

def vector_prod_menu():
  print('1) Vector A times vector B')
  print('2) Vector B times vector A')
  if get_option(1, 2) == 1:
    print('The product of {} and {} is {}'.format(A, B, vector_prod(A, B)))
  else:
    print('The product of {} and {} is {}'.format(B, A, vector_prod(B, A)))

def vector_length_menu():
  print('1) Vector A length')
  print('2) Vector B length')
  if get_option(1, 2) == 1:
    print('The length of {} is {}'.format(A, vector_length(A)))
  else:
    print('The length of {} is {}'.format(B, vector_length(B)))

def enter_vector(msg='Introduce the x, y and z values separated by comas:'):
  return [float(i) for i in input(msg).split(',')]

def vector_sum(A, B):
  return [A[0] + B[0], A[1] + B[1], A[2] + B[2]]

def vector_diff(A, B):
  return [A[0] - B[0], A[1] - B[1], A[2] - B[2]]

def vector_scalar_prod(A, B):
  return A[0]*B[0] + A[1]*B[1] + A[2]*B[2]

def vector_prod(A, B):
  return [A[1]*B[2] - A[2]*B[1], A[2]*B[0] - A[0]*B[2], A[0]*B[1] - A[1]*B[0]]

def vector_angle_between(A, B):
  divident = vector_length(A) * vector_length(B)
  if divident == 0: return 'Error! Division by Zero'
  quotien = vector_scalar_prod(A, B) / divident
  if not -1 <= quotien <= 1: return 'Error! Arccosine out of range'
  return '{:.2f} degrees'.format((180 / math.pi) * math.acos(quotien))

def vector_length(A):
  return math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)

A = None
B = None
option = -1

while option != 9:
  print('1) Enter vector A{}'
    .format(' (A = {})'.format(A) if A != None else ''))
  print('2) Enter vector B{}'
    .format(' (B = {})'.format(B) if B != None else ''))
  print('3) Calculate the sum')
  print('4) Calculate the difference')
  print('5) Calculate the scalar product')
  print('6) Calculate the vector product')
  print('7) Calculate the angle (in degrees) between them')
  print('8) Calculate the length')
  print('9) Finish')
  option = get_option(1, 9)
  if   option == 1:
    A = enter_vector()
  elif option == 2:
    B = enter_vector()
  elif option == 3:
    print('The sum of {} plus {} is {}'.format(A, B, vector_sum(A, B)))
  elif option == 4:
    vector_diff_menu()
  elif option == 5:
    print('The scalar product of {} and {} is {}'
      .format(A, B, vector_scalar_prod(A, B)))
  elif option == 6:
    vector_prod_menu()
  elif option == 7:
    print('The angle between {} and {} is {}'
      .format(A, B, vector_angle_between(A, B)))
  elif option == 8:
    vector_length_menu()
