class CustomComplex:
    def __init__(self, real, imaginary):
        if type(real) == int and type(imaginary) == int:
            self.real = real
            self.imaginary = imaginary
        else:
            raise ValueError()

    def __str__(self):
        if self.imaginary == 0:
            return f"{self.real}"
        if self.real == 0:
            return f"{self.imaginary}i"
        sign = "+"
        if self.imaginary < 0:
            sign = "-"
        return f"{self.real}{sign}{abs(self.imaginary)}i"

    @staticmethod
    def __validate_input(other):
        if type(other) != CustomComplex:
            raise ValueError()

    def __add__(self, other):
        self.__validate_input(other)
        return CustomComplex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        self.__validate_input(other)
        return CustomComplex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        self.__validate_input(other)
        return CustomComplex(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)


print(CustomComplex(0, 0))
print(CustomComplex(0, -1))
print(CustomComplex(0, 1))
print(CustomComplex(-1, 0))
print(CustomComplex(1, 0))
print(CustomComplex(1, 1))
print(CustomComplex(1, -1))
try:
    CustomComplex("1", 1)
except ValueError:
    print("Получена ошибка формирования комплексного числа")
print(CustomComplex(2, 3) + CustomComplex(3, -2))
print(CustomComplex(2, 3) - CustomComplex(3, -2))
print(CustomComplex(2, 3) * CustomComplex(3, -2))
