'''
Celular Automata / draft
'''

# Binary number for rule set in decimal

rule_number = 214  # Rule

rule_in_bin = bin(int(rule_number))[2:]


# if binary convertion dont reach 8 number, we add 0's

if len(rule_in_bin) < 8:
    s = 8 - len(rule_in_bin)
    rule_in_bin = ('0'*s) + rule_in_bin  # returns c string


# defining rule

def calculate_state(left, state, right):
    if left == 1 and state == 1 and right == 1:
        return rule_in_bin[0]
    if left == 1 and state == 1 and right == 0:
        return rule_in_bin[1]
    if left == 1 and state == 0 and right == 1:
        return rule_in_bin[2]
    if left == 1 and state == 0 and right == 0:
        return rule_in_bin[3]
    if left == 0 and state == 1 and right == 1:
        return rule_in_bin[4]
    if left == 0 and state == 1 and right == 0:
        return rule_in_bin[5]
    if left == 0 and state == 0 and right == 1:
        return rule_in_bin[6]
    if left == 0 and state == 0 and right == 0:
        return rule_in_bin[7]


'''#x is the list with generation 0
cells = []
i = 0
while i < len(x):
    left = x[i-1]
    state = x[i]
    if i == len(x)-1:
        right = x[0]
    else:
        right = x[i+1]
    i = i + 1
    cell = str(left)+str(state)+str(right)
    cells.append(cell)
b = cells'''


# Iterating through cells to get the next generation
'''
next_cells = []
next_gen = []
for i in range(len(cells)):
    next_gen.append((calculate_state(int(cells[i][0]), int(cells[i][1]), int(cells[i][2]))))
    new_cells = "".join(next_gen)
    new_cells[i] ='''


# x = init_state

init_state = '010101010100'  # this was determined externally, im not sure if should be a string
cells = []
i = 0

while i < len(init_state):
    left = init_state[i-1]
    state = init_state[i]
    if i == len(init_state)-1:
        right = init_state[0]
    else:
        right = init_state[i+1]
    i = i + 1
    cell = str(left)+str(state)+str(right)
    cells.append(cell)


b = cells
new_state = []

for i in range(10):
    new_cells = []
    next_gen = []
    triples = []
    if i == 0:
      new_cells[0] = cells
      for i in range(len(cells)):
        next_gen.append((calculate_state(int(cells[i][0]), int(cells[i][1]), int(cells[i][2]))))
        next_state = "".join(next_gen)
        next_gen.append(next_state)
        new_cells.append(next_gen)
    else:
        new_cells[i] = next_gen
        while i < len(next_gen):
            left = next_gen[i-1]
            state = next_gen[i]
            if i == len(next_gen)-1:
                right = next_gen[0]
            else:
                right = next_gen[i+1]
            i = i + 1
            gen = str(left)+str(state)+str(right)
            new_cells.append(gen)
            new_cells[i] = new_gen
            for i in range(len(cells)):
                next_gen.append((calculate_state(int(cells[i][0]), int(cells[i][1]), int(cells[i][2]))))
                next_state = "".join(next_gen)
                next_gen.append(next_state)
print()
next_gen = []
next_cells = []