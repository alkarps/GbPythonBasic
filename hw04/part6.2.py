from itertools import cycle

generator = cycle([1, 4, 2, 3, 5, 1, 87])

sum = 0
while sum < 1000:
    sum += next(generator)
    print(sum)
