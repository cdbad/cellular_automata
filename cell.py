'''
Cellular Automata
'''

import random
import numpy as np


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
    def generate_cells(self):
        init_state = [random.randint(0, 1) for width in range(self.x)]
        self.matrix = [init_state]

        for j in range(self.y - 1):
        
            # matrix = [[str(number) for number in init_state]]
            next_row = []
            
            for i in range(self.x):
                left = init_state[i - 1]
                current = init_state[i]

                if i == len(init_state) - 1:
                    right = init_state[0]
                else:
                    right = init_state[i + 1]

                if left == 1 and current == 1 and right == 1:
                    next_row.append(int(self.rule[0]))  # 0
                elif left == 1 and current == 1 and right == 0:
                    next_row.append(int(self.rule[1]))  # 0
                elif left == 1 and current == 0 and right == 1:
                    next_row.append(int(self.rule[2]))  # 0
                elif left == 1 and current == 0 and right == 0:
                    next_row.append(int(self.rule[3]))  # 1
                elif left == 0 and current == 1 and right == 1:
                    next_row.append(int(self.rule[4]))  # 0
                elif left == 0 and current == 1 and right == 0:
                    next_row.append(int(self.rule[5]))  # 1
                elif left == 0 and current == 0 and right == 1:
                    next_row.append(int(self.rule[6]))  # 1
                elif left == 0 and current == 0 and right == 0:
                    next_row.append(int(self.rule[7]))  # 0

            self.matrix.append(next_row)
            init_state = self.matrix[-1]
        #self.matrix = np.array(self.matrix)
        return self.matrix

