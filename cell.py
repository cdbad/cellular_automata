'''
Cellular Automata
'''

import random


class CellClass:
    
    # Generating 8bit number for rule
    def __init__(self, rule: str, size: tuple) -> None:

        self.rule = str(bin(int(rule)))[2:]  # Slice the '0b'
        self.x = size[0]
        self.y = size[1]
     
        if len(self.rule) < 8:
            s = 8 - len(self.rule)
            self.rule = ('0'*s) + self.rule
        
   # Generate initial state:
    def generate_initial_state(self):
        init_state = [random.randint(0, 1) for width in range(self.x)]
        return init_state
        
    # Generate initial state:
    def generate_cells(self):

        init_state = [random.randint(0, 1) for width in range(self.x)]

        for i in range(self.y):
        
            matrix = [[str(number) for number in init_state]]
            next_row = []

            for state in range(len(init_state)):
            
                left = init_state[state - 1]
                current = init_state[state]

                if state == len(init_state) - 1:
                    right = init_state[0]
                else:
                    right = init_state[state + 1]

                if left == 1 and current == 1 and right == 1:
                    next_row.append(self.rule[0])  # 0
                elif left == 1 and current == 1 and right == 0:
                    next_row.append(self.rule[1])  # 0
                elif left == 1 and current == 0 and right == 1:
                    next_row.append(self.rule[2])  # 0
                elif left == 1 and current == 0 and right == 0:
                    next_row.append(self.rule[3])  # 1
                elif left == 0 and current == 1 and right == 1:
                    next_row.append(self.rule[4])  # 0
                elif left == 0 and current == 1 and right == 0:
                    next_row.append(self.rule[5])  # 1
                elif left == 0 and current == 0 and right == 1:
                    next_row.append(self.rule[6])  # 1
                elif left == 0 and current == 0 and right == 0:
                    next_row.append(self.rule[7])  # 0
        
                matrix.append(next_row)
                # print(next_row)
                
        init_state = next_row
        return matrix


celular_atutomata = CellClass(22,(6,40))

print(f'binary rule: {celular_atutomata.rule} \nsize: {celular_atutomata.x} x {celular_atutomata.y}')
print((celular_atutomata.generate_cells()))
