from sys import argv

if len(argv) == 4:
    print(int(argv[1])*int(argv[2]) + int(argv[3]))
else:
    print("Ошибка ввода данных")
