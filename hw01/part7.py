day = 1
current_dist = start_dist = int(input("Пожалуйста, введите начальную дистанцию: "))
expected_dist = int(input("Пожалуйста, введите ожидаемую дистанцию: "))
print(f"Начальная дистанция: {start_dist} км, ожидаемая дистанция: {expected_dist} км. Начинаем вычислять...")
while current_dist < expected_dist:
    print(f"{day}-й день: {current_dist}")
    current_dist = round(current_dist * 1.1, 2)
    day += 1
print(f"{day}-й день: {current_dist}")
print(f"На {day}-й день спортсмен достиг результата - не менее {expected_dist} км.")
