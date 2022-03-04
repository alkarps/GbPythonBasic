from sys import argv

if len(argv) == 4:
    print(float(argv[1]) * float(argv[2]) + float(argv[3]))
else:
    print('Ошибка ввода данных. Укажите, пожалуйста, все параметры в следующем порядке:'
          ' "выработка в часах", "ставка в час" и "премия"')
