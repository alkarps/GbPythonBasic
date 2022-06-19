class IncorrectInput(ValueError):
    def __init__(self, input_value):
        self.message = f"Введенное значение {input_value} не является числом."

    def __str__(self):
        return self.message

    @staticmethod
    def to_int(input_value):
        if input_value.isdigit():
            return int(input_value)
        raise IncorrectInput(input_value)


class ValidatingInput:
    @staticmethod
    def get_next_input():
        input_value = None
        while input_value != "STOP":
            input_value = input("Введите следующее числовое значение или слово \"STOP\" для остановки ввода: ")
            try:
                yield IncorrectInput.to_int(input_value)
            except IncorrectInput as ii:
                print(ii)


print([x for x in ValidatingInput.get_next_input()])
