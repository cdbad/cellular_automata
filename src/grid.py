import turtle
from src.cell import CellClass
import tkinter as tk
import json

class Grid:
    def __init__(self, rule, w, h, color='Black White'):
        self.rule = rule
        self.w = w
        self.h = h
        self.square_size = 20 # size of the cells

        with open('./src/settings/colors.json', 'r') as f:
            self.colors = json.load(f)[color]

        cellular_automata = CellClass(self.rule, (self.w, self.h))
        self.matrix = cellular_automata.generate_cells()

        # ROOT
        root = tk.Tk()
        root.title('Turtle Automata')
        root.config(bg=self.colors['Background'])

        canvas = tk.Canvas(
            root,
            width= (self.square_size * self.w + 20),
            height= (self.square_size * self.h + 20)
            )
        canvas.pack(padx=20, pady=20)

        wn = turtle.TurtleScreen(canvas)
        wn.bgcolor(self.colors['Background'])
        

        self.drawer = turtle.RawTurtle(wn)
        self.drawer.hideturtle()

        wn.tracer(40, 40)

        self.create_grid(self.w, self.h,
                    self.matrix)

        wn.update()

        root.mainloop()

    def create_grid(self, rows, cols, matrix):
        start_x = -rows * self.square_size // 2
        start_y = cols * self.square_size // 2
        for col in range(cols):
            for row in range(rows):
                x = start_x + row * self.square_size
                y = start_y - col * self.square_size
                if matrix[col][row] == 1:
                    color = self.colors['Ones']
                else:
                    color = self.colors['Zeros']

                self.draw_filled_square(x, y, self.square_size * 0.8, color)

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

    