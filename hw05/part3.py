avr = 0.0
low_salary_person = []
with open("part3.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        salary = float(line.split()[1])
        if salary < 20000:
            low_salary_person.append(line.split()[0])
        avr += salary
    print(f"Средняя зарплата: {avr / len(lines)}. Сотрудники с ЗП < 20000: {low_salary_person}")
