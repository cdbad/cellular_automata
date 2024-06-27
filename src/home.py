import tkinter as tk
import json

from src.grid import Grid

class Home:
    FONT_SIZE = 15

    def __init__(self):
        # make window
        self.root = tk.Tk()
        self.root.geometry('400x400')
        self.root.title('Cellular Automata')

        with open('./src/settings/colors.json', 'r') as f:
            self.colors_list = list(json.load(f).keys())
            self.colors = tk.Variable(value=self.colors_list)

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

        self.size_label : tk.Label = self.__label(
            self.size_entry_frame,
            txt='x'
            )
        self.size_label.grid(row=0, column=1, padx=5)

        self.h_entry : tk.Entry = self.__entry(self.size_entry_frame)
        self.h_entry.grid(row=0, column=2)

        self.size_entry_frame.grid(row=1, column=1)

        self.input_frame.pack(pady=5, fill=tk.X)

        # error label
        self.error_frame = tk.Frame(self.root)

        self.__label(
            self.error_frame,
            txt='',
            l_type='error'
            )

        self.error_frame.pack(padx=5, fill=tk.X)

        # advanced settings
        self.settings_frame = tk.Frame(self.root)
        self.settings_frame.columnconfigure(0, weight=1)
        self.settings_frame.columnconfigure(1, weight=1)
        
        self.colors_label = self.__label(
            self.settings_frame,
            txt='colors',
            )
        self.colors_label.grid(row=0, column=0, sticky=tk.W)

        self.list_box = tk.Listbox(
            self.settings_frame,
            height=len(self.colors_list),
            listvariable=self.colors,
            selectmode=tk.SINGLE
            )
        self.list_box.grid(row=0, column=1)

        self.settings_frame.pack(padx=5, pady=(5,10), fill=tk.X)

        # generate button
        self.button : tk.Button = self.__button(
            self.root,
            txt='Generate',
            func=self.send_data,
            )
        self.button.pack(pady=5)

        self.root.mainloop()

    def __button(self, container, txt, func) -> tk.Button:
        return tk.Button(
            container,
            text=txt,
            font=('Arial', self.FONT_SIZE),
            command=func,
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
            if self.list_box.curselection():
                color_selection = self.colors_list[self.list_box.curselection()[0]]
            else:
                color_selection = 'Default'
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
                Grid(rule, width, height, color_selection)
