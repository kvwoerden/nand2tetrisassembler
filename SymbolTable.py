class SymbolTable:
    def __init__(self):
        tableone = { 'SP': 0,
        'LCL': '1',
        'ARG': '2',
        'THIS': '3',
        'THAT': '4',
        'SCREEN': '16384',
        'KBD': '24576' }
        tabletwo = { 'R' + str(i): i for i in range(0, 16) }
        self.table = { **tableone, **tabletwo }
    
    def addEntry(self, symbol, address):
        self.table[symbol] = address
    
    def contains(self, symbol):
        return symbol in self.table

    def GetAddress(self, symbol):
        return self.table[symbol]