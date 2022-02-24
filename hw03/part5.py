def reduce_list_to_sum(values):
    """
    Приведение списка к сумме чисел.

    :param values: список чисел для суммирования.
    :return: сумму чисел списка.
    """
    current_sum = 0
    need_stop = True
    for value in values:
        if value.isdigit():
            current_sum += int(value)
        else:
            need_stop = False
            break
    return current_sum, need_stop


result = 0
need_continue = True
while need_continue:
    input_list = input("Введите строку чисел через пробел или что-нибудь другое для выхода: ").split()
    reduce = reduce_list_to_sum(input_list)
    result, need_continue = reduce[0] + result, reduce[1]
    print(f"Текущая сумма: {result}.")
