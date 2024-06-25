from cell import CellClass

celular_automata = CellClass(123, (15,15))

print(f'binary rule: {celular_automata.rule} \nsize: {celular_automata.x} x {celular_automata.y}')
matrix = celular_automata.generate_cells()
