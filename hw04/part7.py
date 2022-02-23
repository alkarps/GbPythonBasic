def factorial(n):
    current = 1
    for i in range(1, n + 1):
        current *= i
        yield current


n = int(input("Please, input N for calculate factorial:"))
for value in factorial(n):
    print(value)
