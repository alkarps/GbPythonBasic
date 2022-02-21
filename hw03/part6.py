def int_func(values):
    """
    Функция, принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
    :param values: слова из маленьких латинских букв.
    :return: слова из маленьких латинских букв, но с прописной первой буквой.
    """
    return " ".join([x.capitalize() for x in values.split()])


print(int_func(input("Введите через пробел слова из маленьких латинских букв: ")))