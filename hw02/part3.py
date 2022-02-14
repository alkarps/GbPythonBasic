list_of_month = ["зима", "весна", "лето", "осень"]
map_of_month = {1: "зима", 2: "зима", 12: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето",
                9: "осень", 10: "осень", 11: "осень"}
month = -1
while not 1 <= month <= 12:
    month = int(input("Please, input month in range of 1 to 12 include: "))

print(f"Using dict: {map_of_month[month]}")
print(f"Using list: {list_of_month[(month // 3) % 4]}")
