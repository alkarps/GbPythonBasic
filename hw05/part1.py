with open("part1.txt", "w") as file:
    input_line = None
    while input_line != "":
        input_line = input("Введите текст для сохранения в файл или пустую строку для выхода:")
        file.writelines(input_line + "\n")
