income = int(input("Please, input income: "))
outcome = int(input("Please, input outcome: "))
if income < outcome:
    print("You loose money")
elif income == outcome:
    print("Its equals")
else:
    print("You get money")
    clear_income = income - outcome
    rental_income = clear_income / income
    print(f"rental income: {rental_income}")
    personal_count = int(input("Please, input personal count: "))
    rental_income_on_one_personal = rental_income / personal_count
    clear_income_on_one_personal = clear_income / personal_count
    print(f"rental income on one personal: {rental_income_on_one_personal}")
    print(f"clear income on one personal: {clear_income_on_one_personal}")
