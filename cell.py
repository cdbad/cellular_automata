'''
Cellular Automata
'''

class CellClass:

    # Generating 8bit number for rule
    def __init__(self, rule: str, size: tuple) -> None:
        self.rule = str(bin(int(rule)))[2:]  # Slice the '0b'
        self.x = size[0]
        self.y = size[1]
     
        if len(self.rule) < 8:
            s = 8 - len(self.rule)
            self.rule = ('0'*s) + self.rule

    # Generate the initial state (row)
    def generate_cells(self):
        
        

x = CellClass(22,(40,40))

print(x.rule)
