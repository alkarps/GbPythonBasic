list_of_elements = ["", None, 1.0, "asd", 1, True, False, Exception, Exception(), oct(1), hex(1), bin(1),
                    complex(1, 12)]

print(f"list is {type(list_of_elements)}")
for element in list_of_elements:
    print(f'element {element} with type of {type(element)}')
