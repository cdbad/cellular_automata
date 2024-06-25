import turtle
from cell import CellClass


class Grid:

    def __init__(self, rule, rows, cols) -> None:
        # Windown Display
        self.wn = turtle.Screen()
        self.wn.bgcolor("light green")
        self.wn.title("Cellular Automata")
        self.wn.setup(1000, 1000)  # window size

        # Create a turtle named "drawer"
        self.drawer = turtle.Turtle()
        self.drawer.speed(400)
        self.drawer.hideturtle()
        
        self.rule = rule
        self.rows = rows
        self.cols = cols
        celular_automata = CellClass(self.rule, (self.rows, self.cols))
        self.matrix = celular_automata.generate_cells()
        self.create_grid()

        #self.wn.tracer(40)
        #self.wn.update()

        # Hide the turtle and keep the window open until it is clicked
        self.drawer.hideturtle()
        self.wn.exitonclick()


# Function to draw a filled square at a specific position
# It will allow us to draw in the middel of the panel

    def draw_filled_square(self, x, y, size, color):
        self.drawer.penup()
        self.drawer.goto(x, y)
        self.drawer.pendown()
        self.drawer.color(color) 
        self.drawer.begin_fill()
        for i in range(4):
            self.drawer.forward(size)
            self.drawer.right(90)
        self.drawer.end_fill()

    # Function to create a grid of filled squares
    def create_grid(self):
        square_size = 20
        start_x = -self.cols * square_size // 2
        start_y = self.rows * square_size // 2
        for row in range(self.rows):
            row_in_matrix = self.matrix[row]
            for col in range(self.cols):
                x = start_x + col * square_size
                y = start_y - row * square_size
                if row_in_matrix[col] == 1:
                    row_in_matrix[col] = 'purple'
                else:
                    row_in_matrix[col] = 'white'
                color = row_in_matrix[col]
                self.draw_filled_square(x, y, square_size * 0.8, color)