n = int(input("Please, input count elements: "))
list_of_elements = []
odd_element = None
for i in range(0, n):
    if i % 2 == 0:
        odd_element = input(f"Please, input {i}'s elements: ")
    else:
        list_of_elements.insert(i - 1, input(f"Please, input {i}'s elements: "))
        list_of_elements.append(odd_element)
if n % 2:
    list_of_elements.append(odd_element)

print(f"result = {list_of_elements}")

list_of_elements = input("Please, input elements separated by spaces:").split()

for i in range(0, len(list_of_elements) - 1, 2):
    list_of_elements[i], list_of_elements[i + 1] = list_of_elements[i + 1], list_of_elements[i]
print(f"result = {list_of_elements}")
