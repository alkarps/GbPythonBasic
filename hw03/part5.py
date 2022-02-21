def reduce_list_to_sum(values):
    """
    Приведение списка к сумме чисел.

    :param values: список чисел для суммирования.
    :return: сумму чисел списка.
    """
    global result
    for value in values:
        result += int(value)


def print_current_sum(result, need_exit=False):
    """
    Метод вывода текущей суммы
    :param result: текущая сумма.
    :param need_exit: признак вывода текста выхода из программы
    :return: None
    """
    print(f"Текущая сумма: {result}.")
    if need_exit:
        print("Выходим из программы...")


result = 0
try:
    while True:
        print_current_sum(result)
        input_list = input("Введите строку чисел через пробел или что-нибудь другое для выхода: ").split()
        reduce_list_to_sum(input_list)
except ValueError:
    print(f"Текущая сумма: {result}. Выходим из программы")
