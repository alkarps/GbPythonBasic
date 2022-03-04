from itertools import count

generator = count(3)
print(generator)
i = 0
while i < 10:
    i = next(generator)
    print(i)
