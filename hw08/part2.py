class CustomZeroDivisionError(Exception):
    def __init__(self, message="Произошло деление на 0"):
        self.message = message

    def __str__(self):
        return f"{type(self)}: {self.message}"


def division(a, b):
    if b == 0:
        raise CustomZeroDivisionError()
    return a / b


A = int(input("Please, input A: "))
B = int(input("Please, input B: "))
try:
    print(division(A, B))
except CustomZeroDivisionError as e:
    print(e)
