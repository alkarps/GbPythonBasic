maxChar = 0
number = input("Input number please: ")
n = len(number)
if n <= 0:
    exit(0)
i = 0
while i < n:
    current = int(number[i])
    if current > maxChar:
        maxChar = current
    i += 1
print(maxChar)
