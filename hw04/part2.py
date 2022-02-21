income_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([income_list[i] for i in range(1, len(income_list)) if income_list[i - 1] < income_list[i]])
