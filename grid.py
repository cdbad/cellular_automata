import turtle
from cell import CellClass
import tkinter as tk

def create_grid(rows, cols, matrix, drawer):
    square_size = 20 # size of the cells
    start_x = -rows * square_size // 2
    start_y = cols * square_size // 2
    for col in range(cols):
        for row in range(rows):
            x = start_x + row * square_size
            y = start_y - col * square_size
            if matrix[col][row] == 1:
                color = '#422040'
            else:
                color = '#E9F1F7'

            draw_filled_square(x, y, square_size * 0.8, color, drawer)

def draw_filled_square(x, y, size, color, drawer):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.color(color) 
    drawer.begin_fill()
    for i in range(4):
        drawer.forward(size)
        drawer.right(90)
    drawer.end_fill()

def grid(rule, w, h):
    cellular_automata = CellClass(rule, (w, h))
    matrix = cellular_automata.generate_cells()

    # ROOT
    root = tk.Tk()
    root.title('Turtle Automata')

    canvas = tk.Canvas(
        root,
        width=800,
        height=600
        )
    canvas.pack()

    wn = turtle.TurtleScreen(canvas)

    drawer = turtle.RawTurtle(wn)

    wn.tracer(40, 40)

    create_grid(cellular_automata.x, cellular_automata.y,
                matrix, drawer)

    wn.update()

    root.mainloop()