import tkinter as tk
from src.grid import Grid

class Home:
    FONT_SIZE = 15

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
        self.rule_label = self.__label(self.input_frame, txt='rule')
        self.rule_label.grid(row=0, column=0, pady=(20,0))

        self.rule_entry = self.__entry(self.input_frame)
        self.rule_entry.grid(row=0, column=1, pady=(20,0))

        # size
        self.size_label = self.__label(self.input_frame, txt='size')
        self.size_label.grid(row=1, column=0, pady=5)

        # size entry frame
        self.size_entry_frame = tk.Frame(self.input_frame)
        self.size_entry_frame.columnconfigure(0, weight=1)
        self.size_entry_frame.columnconfigure(1, weight=2)
        self.size_entry_frame.columnconfigure(2, weight=1)

        self.w_entry : tk.Entry = self.__entry(self.size_entry_frame)
        self.w_entry.grid(row=0, column=0)

        self.size_label : tk.Label = self.__label(self.size_entry_frame, txt='x')
        self.size_label.grid(row=0, column=1, padx=5)

        self.h_entry : tk.Entry = self.__entry(self.size_entry_frame)
        self.h_entry.grid(row=0, column=2)

        self.size_entry_frame.grid(row=1, column=1)

        self.input_frame.pack(pady=5, fill=tk.X)

        # error label
        self.error_frame = tk.Frame(self.root)

        self.__label(self.error_frame, txt='', l_type='error')

        self.error_frame.pack(padx=5)

        # generate button
        self.button : tk.Button = self.__button(self.root, txt='Generate')
        self.button.pack(pady=5)

        self.root.mainloop()

    def __button(self, container, txt) -> tk.Button:
        return tk.Button(
            container,
            text=txt,
            font=('Arial', self.FONT_SIZE),
            command=self.send_data,
            )

    def __entry(self, container) -> tk.Entry:
        return tk.Entry(
            container,
            width=10,
            font=('Arial', self.FONT_SIZE),
            )

    def __label(self, container='', txt='', l_type='text') -> tk.Label:
        if l_type == 'error':
            self.error_label = tk.Label(
                self.error_frame,
                text=txt,
                font=('Arial', self.FONT_SIZE - 5),
                foreground='red'
                )
            self.error_label.pack(padx=5)
        else:
            return tk.Label(
                container,
                text=txt,
                font=('Arial', self.FONT_SIZE)
                )

    def send_data(self):
        self.error_label.pack_forget()
            
        try:
            rule = int(self.rule_entry.get())
            width = int(self.w_entry.get())
            height = int(self.h_entry.get())
        # input handler
        except ValueError as e:
            if str(e)[-2] == "'":
                self.__label(txt='All the fields must be filled', l_type='error')
            else:
                self.__label(txt='All entries must be numbers', l_type='error')
        else:
            if rule < 1 or rule > 255:
                self.__label(txt="Rule must be between 1 and 255", l_type='error')
            elif width < 2 or height < 2:
                self.__label(txt="Size must be 2x2 or bigger", l_type='error')
            else:
                Grid(rule, width, height)
