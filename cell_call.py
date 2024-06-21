from cell import CellClass

celular_atutomata = CellClass(42, (6,10))

print(f'binary rule: {celular_atutomata.rule} \nsize: {celular_atutomata.x} x {celular_atutomata.y}')
print(celular_atutomata.generate_cells())
