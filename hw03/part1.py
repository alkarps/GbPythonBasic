def div(a_value, b_value):
    if b_value == 0 or b_value == 0.0:
        return float('NaN')
    return a_value / b_value


a = float(input("Input value A: "))
b = float(input("Input value B: "))
print(div(a, b))
