import turtle
import random
from cell_call import matrix

# Windown Display
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Cellular Automata")
wn.setup(1000,1000)  #  window size

# Create a turtle named "drawer"
drawer = turtle.Turtle()
# drawer.speed(400)  # Set the turtle speed to the maximum
drawer.hideturtle()

#print(matrix)

# Function to draw a filled square at a specific position
# It will allow us to draw in the middel of the panel


class Grid:

    def __init__(self, rows, cols) -> None:
        self.rows = rows
        self.cols = cols



    

def draw_filled_square(x, y, size, color):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()

    # print(matrix[row])
  
    drawer.color(color)  
    drawer.begin_fill()
    for i in range(4):
        drawer.forward(size)
        drawer.right(90)
    drawer.end_fill()

# Function to create a grid of filled squares
def create_grid(rows, cols, square_size):
    start_x = -cols * square_size // 2
    start_y = rows * square_size // 2
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * square_size
            y = start_y - row * square_size
            # for i in range(len(colored)): # color need to be change according to the list of 0s and 1s
            #color = ('purple')
            if row_in_matrix[col] == 1:
                row_in_matrix[col] = 'black'
            else:
                row_in_matrix[col] = 'light green'
                color = row_in_matrix[col]
            
            draw_filled_square(x, y, square_size * 0.8, color)


# Parameters for the grid
rows = len(matrix)
cols = len(matrix[0])
square_size = 20

for row in range(rows):
    print(matrix[row])
    row_in_matrix = matrix[row]
    for col in range(cols):
        if row_in_matrix[col] == 1:
            row_in_matrix[col] = 'black'
        else:
            row_in_matrix[col] = 'light green'
        color = row_in_matrix[col]
        #print(color)



wn.tracer(40)
wn.update()

# Create the grid
create_grid(rows, cols, square_size)

# Hide the turtle and keep the window open until it is clicked
drawer.hideturtle()
wn.exitonclick()
