from functools import reduce

with open("part5.txt", "w") as file:
    file.write(" ".join([str(x) for x in range(1, 1001)]))
with open("part5.txt", "r") as file:
    print(reduce(lambda x, y: x + y, map(lambda x: int(x), file.readline().split())))
