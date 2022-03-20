class Matrix:
    def __init__(self, elements):
        def check_type(values):
            if type(values) != list:
                raise ValueError(f"Expected list type but has {values}")

        check_type(elements)
        n = len(elements)
        if n == 0:
            raise ValueError("Empty input elements")
        m = -1
        for column in elements:
            check_type(column)
            if m == -1:
                m = len(column)
                if m == 0:
                    raise ValueError("Empty input elements")
            elif m != len(column):
                raise ValueError("Column has different size")
        self.dimensions = (n, m)
        self.elements = elements

    def __str__(self):
        elements_print = "\n".join(["\t" + " ".join([str(s) for s in x]) for x in self.elements])
        return f"""Matrix {self.dimensions[0]}x{self.dimensions[1]} with elements:\n{elements_print}"""

    def __add__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Expected Matrix but has {type(other)}")
        if self.dimensions == other.dimensions:
            new_elements = [[self.elements[i][j] + other.elements[i][j] for j in range(self.dimensions[1])] for i in
                            range(self.dimensions[0])]
            return Matrix(new_elements)
        else:
            raise ValueError("Matrix has different dimensions")


matrix_1 = Matrix([[1], [3]])
matrix_2 = Matrix([[2], [6]])
matrix_3 = matrix_1 + matrix_2 + Matrix([[2], [7]])
print(matrix_1)
print(matrix_2)
print(matrix_3)
