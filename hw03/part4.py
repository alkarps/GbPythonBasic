def my_func(x, y):
    return x ** y


def my_func_ver2(x, y):
    result = 1
    i = 0
    while i > y:
        result /= x
        i -= 1
    return result


X = int(input("Input X: "))
Y = int(input("Input Y: "))

print(my_func(X, Y))
print(my_func_ver2(X, Y))
