import tkinter as tk
from grid import Grid

class Home:
    
    def __init__(self):
        # make window
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title('Cellular Automata')

        # entries frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.columnconfigure(0, weight=1)
        self.input_frame.columnconfigure(1, weight=1)

        # rule
        self.rule_label = tk.Label(self.input_frame, text='rule', font=('Arial', 15))
        self.rule_label.grid(row=0, column=0, pady=(20,0))

        self.rule_entry = tk.Entry(self.input_frame, width=10, font=('Arial', 12))
        self.rule_entry.grid(row=0, column=1, pady=(20,0))

        # size
        self.size_label = tk.Label(self.input_frame, text='size', font=('Arial', 15))
        self.size_label.grid(row=1, column=0, pady=5)

        # size entry frame
        self.size_entry_frame = tk.Frame(self.input_frame)
        self.size_entry_frame.columnconfigure(0, weight=1)
        self.size_entry_frame.columnconfigure(1, weight=2)
        self.size_entry_frame.columnconfigure(2, weight=1)

        self.w_entry = tk.Entry(self.size_entry_frame, width=10, font=('Arial', 12))
        self.w_entry.grid(row=0, column=0)

        self.size_label = tk.Label(self.size_entry_frame, text='x', font=('Arial', 12))
        self.size_label.grid(row=0, column=1, padx=5)

        self.h_entry = tk.Entry(self.size_entry_frame, width=10, font=('Arial', 12))
        self.h_entry.grid(row=0, column=2)

        self.size_entry_frame.grid(row=1, column=1)

        self.input_frame.pack(pady=5, fill=tk.X)

        # error label
        self.error_frame = tk.Frame(self.root)

        self.__error_label('')

        self.error_frame.pack(padx=5)

        # generate button
        self.button = tk.Button(
            self.root,
            text='Generate',
            font=('Arial', 14),
            command=self.send_data)
        self.button.pack(pady=5)

        self.root.mainloop()

    def __error_label(self, txt=''):
        self.error_label = tk.Label(
            self.error_frame,
            text=txt,
            font=('Arial', 10),
            foreground='red')
        self.error_label.pack(padx=5)

    def send_data(self):
        self.error_label.pack_forget()

        rule = self.rule_entry.get()
        width = self.w_entry.get()
        height = self.h_entry.get()

        if not rule or not width or not height:
            self.__error_label('All the fields must be filled')
        elif type(rule) == str and type(width) == str and type(height) == str:
            try:
                rule = int(rule)
                width = int(width)
                height = int(height)
                Grid(rule, width, height)
            except ValueError:
                self.__error_label('All entries must be numbers')
