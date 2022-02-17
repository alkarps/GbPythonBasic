def my_func(x, y):
    return x ** y


def my_func_ver2(x, y):
    result = 1 / x
    i = -1
    while i > y:
        result *= result
        i -= 1
    return result


X = int(input("Input X: "))
Y = int(input("Input Y: "))

print(my_func(X, Y))
print(my_func_ver2(X, Y))
