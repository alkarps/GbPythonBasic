class Cell:
    def __init__(self, count):
        if count < 1:
            raise ValueError("Cells has wrong count")
        self.count = count

    def __check_type(self, other):
        if type(other) != Cell:
            raise ValueError(f"Expected object with type Cell, but has {type(other)}")

    def __add__(self, other):
        self.__check_type(other)
        return Cell(self.count + other.count)

    def __sub__(self, other):
        self.__check_type(other)
        return Cell(self.count - other.count)

    def __mul__(self, other):
        self.__check_type(other)
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        self.__check_type(other)
        return Cell(self.count // other.count)

    def make_order(self, row_len):
        return ("*" * row_len + "\n") * (self.count // row_len) + "*" * (self.count % row_len)


print((Cell(1) + Cell(3) * Cell(2)).make_order(4))

print(Cell.make_order(Cell(10) / Cell(2), 3))
