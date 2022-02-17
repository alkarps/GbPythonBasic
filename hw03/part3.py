def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    elif b < a and b < c:
        return a + c
    else:
        return a + b


A = int(input("Input A: "))
B = int(input("Input B: "))
C = int(input("Input C: "))
print(my_func(A, B, C))
