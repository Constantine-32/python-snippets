'''
Introduction to Programming
2018-19 First Trimester
Lab 2 - Functions

Final program
'''
import turtle
import random
import math

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

# Returns a color choosed by the user
def get_color():
  colors = ('White', 'Yellow', 'Orange', 'Red', 'Purple', 'Blue', 'Green', 'Black')
  for i in range(len(colors)):
    print('{:d}) {}'.format(i+1, colors[i]))
  option = get_option(1, len(colors), msg='Choose a color: ')
  return colors[option - 1]

# Shows the menu options
def show_menu():
  print(' 1) Show the options menu')
  print(' 2) Change the color of the window')
  print(' 3) Change the color of the cursor')
  print(' 4) Change the speed of the cursor')
  print(' 5) Change the thickness of the cursor')
  print(' 6) Toggle the cursor visible/invisible')
  print(' 7) Move the cursor to the center of the window')
  print(' 8) Move the cursor forward')
  print(' 9) Rotate the cursor clockwise')
  print('10) Clear the window')
  print('11) Draw a polygon')
  print('12) Draw a star (odd number of sides)')
  print('13) Draw a circle')
  print('14) Draw a point')
  print('15) Create a \'sky\' of random points')
  print('16) Create a \'sky\' of random stars')
  print('17) Draw a spiral')
  print('18) Draw a fractal')
  print('19) Exit')

# Sets de window background color
def set_window_color():
  color = get_color()
  window.bgcolor(color)
  print(color + ' color set')

# Sets de cursor color
def set_cursor_color():
  color = get_color()
  cursor.pencolor(color)
  print(color + ' color set')

# Sets de cursor speed
def set_cursor_speed():
  speed = get_option(1, 10, msg='Choose the speed between 1 and 10: ')
  cursor.speed(speed)

# Sets de cursor thickness
def set_cursor_thickness():
  thickness = get_option(1, 100, msg='Choose the thickness between 1 and 100: ')
  cursor.pensize(thickness)

# Toggles de cursor visibility
def set_cursor_visibility():
  if cursor.isdown():
    cursor.penup()
  else:
    cursor.pendown()

# Moves the cursor to the center without drawing
def move_cursor_home():
  cursor.penup()
  cursor.home()
  cursor.pendown()

# Moves the cursor forward
def move_cursor_forward():
  distance = get_option(0, 400, msg='Choose the distance [0-400]: ')
  cursor.forward(distance)

# Rotates the cursor clockwise
def rotate_cursor():
  grades = get_option(0, 360, msg='Choose the grades to rotate [0-360]: ')
  cursor.right(grades)

# Draws a polygon
def polygon(sides, radius):
  # the angle of the isosceles triangle that evenly divides the circumference
  # where the polygon is inscribed
  theta = 360 / sides
  # the length of the edges of the triangle. We have to convert (theta / 2) from
  # grades to radians.
  size = 2 * radius * math.sin(math.radians(theta / 2))
  # draw the edge and then turn theta grades to the left as many times as sides
  for _ in range(sides):
    cursor.forward(size)
    cursor.left(theta)

# Draws a polygon, other approach, divides a circumference evenly getting the
# polar coordinates of each vertex of the polygon. This is differen of the other
# aproach in the sense that not only the polygon is inscribed inside an
# imaginary circumference of the asked radius, but it is also centered at the
# current position of the cursor
def polygon2(sides, radius, alpha=math.pi/2):
  # Alpha this is the rotation of the whole polygon
  # those are the angles of every line that goes from the center of the
  # circumference to each vertex of the polygon
  thetas = [(2 * math.pi / sides * k + alpha) for k in range(sides + 1)]
  cursor.penup()
  # for each angle theta we convert from polar coordinates to cartesian and move
  # the cursor to each one in order
  for theta in thetas:
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    cursor.setpos(x, y)
    cursor.pendown()

# Asks de user for parameters and draws a polygon
def draw_polygon():
  sides = get_option(3, 100, msg='Choose the sides [3-100]: ')
  radius = get_option(0, 400, msg='Choose the radius [0-400]: ')
  polygon(sides, radius)

# Draws an odd pointed star
def odd_star(points, size):
  theta = 180 - 180 / points
  for _ in range(points):
    cursor.forward(size)
    cursor.right(theta)

# Asks de user for parameters and draws an odd pointed star
def draw_star_odd():
  points = get_option(5, 99, msg='Choose the number of points [5-99] only odd values: ')
  while points % 2 == 0:
    print('The number of points must be odd')
    points = get_option(5, 99, msg='Choose the number of points [5-99] only odd values: ')
  size = get_option(0, 400, msg='Choose the size [0-400]: ')
  odd_star(points, size)

# Draws a circle with the current position of the cursor as the center
def draw_circle():
  radius = get_option(0, 400, msg='Choose the radius [0-400]: ')
  # Saves the current coordinates and orientation to restore them later
  x = cursor.xcor()
  y = cursor.ycor()
  g = cursor.heading()
  # Moves from the center to the top of the circle and resets the orientation
  cursor.penup()
  cursor.setpos(x, y - radius)
  cursor.pendown()
  cursor.left(360 - g)
  # Draws the circle
  cursor.circle(radius)
  # Restores the previous orientation and moves to the center of the circle
  cursor.left(g)
  cursor.penup()
  cursor.setpos(x, y)
  cursor.pendown()

# Draws a point
def draw_point():
  diameter = get_option(0, 400, msg='Choose the diameter [0-400]: ')
  cursor.dot(diameter)

# Draws "number" number of points randomly placed on the window
def sky_points(number):
  colors = ('Yellow', 'Orange', 'Red', 'Pink', 'Purple', 'Blue', 'Green', 'Brown')
  for _ in range(number):
    x = random.randint(-width // 2, width // 2)
    y = random.randint(-height // 2, height // 2)
    diameter = random.randint(3, 23)
    color = colors[random.randint(0, len(colors) -1)]
    cursor.penup()
    cursor.setpos(x, y)
    cursor.pendown()
    cursor.pencolor(color)
    cursor.dot(diameter)

# Asks de user for parameters and draws a sky of points
def draw_sky_points():
  number = get_option(0, 100, msg='Choose the number of points [0-100]: ')
  sky_points(number)

# Draws "number" number of stars randomly placed on the window
def sky_stars(number):
  colors = ('Yellow', 'Orange', 'Red', 'Pink', 'Purple', 'Blue', 'Green', 'Brown')
  for _ in range(number):
    x = random.randint(-width//2, width//2)
    y = random.randint(-height//2, height//2)
    # chooses a random number of points between 5 and 11 only odd values
    points = random.randint(2, 5) * 2 + 1
    size = random.randint(10, 30)
    color = colors[random.randint(0, len(colors)-1)]
    cursor.penup()
    cursor.setpos(x, y)
    cursor.pendown()
    cursor.pencolor(color)
    odd_star(points, size)

# Asks de user for parameters and draws a sky of stars
def draw_sky_stars():
  number = get_option(0, 20, msg='Choose the number of stars [0-20]: ')
  sky_stars(number)

# Draws a spiral
def spiral(sides, iterations, off_set=3):
  move_cursor_home()
  for i in range(iterations):
    cursor.forward(i)
    cursor.left(360 / sides + off_set)

# Asks de user for parameters and draws a spiral
def draw_spiral():
  sides = get_option(3, 11, msg='Choose the number of vertex [3-11]: ')
  iters = get_option(50, 500, msg='Choose the number of iterations [50-500]: ')
  spiral(sides, iters)

# Draws a fractal of triangles
def fractal(x, y, radius, iterations):
  # If the recursion counter reaches 0 return and do nothing
  if iterations == 0:
    return
  # Divides the circumference in 6 points, the even ones for drawing the
  # triangle and the odd ones as the center of the next iteration of triangles
  thetas = [(2 * math.pi / 6 * k + math.pi / 6) for k in range(7)]
  # Draws the triangle
  cursor.penup()
  for theta in thetas[::2]:
    x1 = radius * math.cos(theta) + x
    y1 = radius * math.sin(theta) + y
    cursor.setpos(x1, y1)
    cursor.pendown()
  # Calls the same function recursively for the odd points havling the radius
  # and decreasing the iteration counter
  for theta in thetas[1::2]:
    x1 = radius * math.cos(theta) + x
    y1 = radius * math.sin(theta) + y
    fractal(x1, y1, radius/2, iterations-1)

# Asks de user for parameters and draws a fractal of triangles
def draw_fractal():
  iterations = get_option(1, 6, msg='Choose the number of iterations [1-6]: ')
  fractal(0, 0, 100, iterations)

# Define also the main_loop() function 
def main_loop():
  # Put all the functions callable by the menu in a list
  functions = (
    show_menu, set_window_color, set_cursor_color, set_cursor_speed,
    set_cursor_thickness, set_cursor_visibility, move_cursor_home,
    move_cursor_forward, rotate_cursor, window.reset, draw_polygon,
    draw_star_odd, draw_circle, draw_point, draw_sky_points, draw_sky_stars,
    draw_spiral, draw_fractal
  )
  option = 1
  while option != 19:
    # Get the function out of the list and call it
    functions[option - 1]()
    option = get_option(1, 19)
  print('Close the window to exit')

# Creates the window and performs some settings
window = turtle.Screen()
window.bgcolor('white')
window.title('Lab 2 - Functions')
height = 400
width = 600
# We add 40 pixels of margin so the drawings stay inside the window
window.setup(width + 40, height + 40)

cursor = turtle.Turtle()
cursor.pensize(1)
cursor.pencolor('black')
cursor.speed(6)

# It will keep running the main loop till the user asks for exiting
main_loop()

# Closing and exit
turtle.done() 
try:
  turtle.bye()
except:
  print('Program finished!')
