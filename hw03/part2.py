def print_personal(first_name, second_name, birthday, city, email, phone):
    print(
        f"Имя: {first_name}, фамилия: {second_name}, год рождения: {birthday}, город проживания: {city}, email: {email}, телефон: {phone}")


p_fname = input("Введите имя: ")
p_sname = input("Введите фамилию: ")
p_birthday = input("Введите дату рождения: ")
p_city = input("Введите город: ")
p_email = input("Введите email: ")
p_phone = input("Введите телефон: ")
print_personal(first_name=p_fname, second_name=p_sname, birthday=p_birthday, city=p_city, email=p_email, phone=p_phone)
