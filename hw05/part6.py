from functools import reduce

subjects = {}
with open("part6.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        subject = line.split(": ")[0]
        hours = [int(x.split("(")[0]) for x in line.split(": ")[1].split() if x != "—"]
        subjects[subject] = reduce(lambda x, y: x + y, hours)
print(subjects)
