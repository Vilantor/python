class Cell:
    cell1 = int
    cell2 = int

    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        return cell1, cell2

    def __add__(self, other):
        return self.cell1 + self.cell2

    def __sub__(self, other):
        if self.cell1 - self.cell2 > 0:
            return self.cell1 - self.cell2
        else:
            print('Вычесть не получается!')

    def __mul__(self, other):
        return self.cell1 * self.cell2

    def __truediv__(self, other):
        return self.cell1 // self.cell2


c = Cell()
cell1 = 4
cell2 = 8

print(cell1 + cell2)            # не получилось выполнить перегрузку оператора...
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
