rating = [7, 4, 2, 1, 1, 1]
current_input = None
while True:
    current_input = input("Please, input new rating as number or something another for stop program: ")
    if current_input.isdecimal():
        current_input = int(current_input)
        index = len(rating)
        for i in range(len(rating)):
            if rating[i] <= current_input:
                index = i
                break
        rating.insert(index, current_input)
        print(f"Пользователь ввёл число {current_input}. Результат: {rating}.")
    else:
        print(f"Пользователь ввёл {current_input}. Выходим")
        break
