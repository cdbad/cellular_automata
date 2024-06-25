import turtle
from cell import CellClass


class Grid:

    
    def __init__(self, rule, rows, cols) -> None:
        # try:
        # Windown Display
        self.rule = rule
        self.rows = rows
        self.cols = cols

        cellular_automata = CellClass(self.rule, (self.rows, self.cols))
        self.matrix = cellular_automata.generate_cells()

    def make_screen(self):
        self.wn = turtle.Screen()
        self.wn.bgcolor("#F2E86D")
        self.wn.title("Cellular Automata")
        self.wn.setup(1000, 1000)  # window size

        # Create a turtle named "drawer"
        self.drawer = turtle.Turtle()
        self.drawer.hideturtle()
        self.wn.tracer(40, 40)

        self.rule = rule
        self.rows = rows
        self.cols = cols
        celular_automata = CellClass(self.rule, (self.rows, self.cols))
        self.matrix = celular_automata.generate_cells()
        self.create_grid()

        self.wn.update()

        # Hide the turtle and keep the window open until it is clicked
        self.wn.exitonclick()
        # turtle.TurtleScreen._RUNNING = True
        # except turtle.Terminator:
        #     pass

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
        square_size = 20 # size of the cells
        start_x = -self.cols * square_size // 2
        start_y = self.rows * square_size // 2
        for col in range(self.cols):
            for row in range(self.rows):
                x = start_x + col * square_size
                y = start_y - row * square_size
                if self.matrix[col][row] == 1:
                    color = '#422040'
                else:
                    color = '#E9F1F7'

                self.draw_filled_square(x, y, square_size * 0.8, color)

        
#window = Grid(124, 21, 42) 