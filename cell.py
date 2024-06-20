class CellClass:
    def __init__(self, rule: str) -> None:
        self.rule = str(bin(int(rule)))[2:]
      
        if len(self.rule) < 8:
            s = 8 - len(self.rule)
            self.rule = ('0'*s) + self.rule


x = CellClass('22')
