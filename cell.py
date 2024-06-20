class CellClass:
    def __init__(self, rule) -> None:
        self.rule = str(bin(int(rule)))

        if len(self.rule) < 8:
            s = 8 - len(self.rule)
            self.rule = ('0'*s) + self.rule