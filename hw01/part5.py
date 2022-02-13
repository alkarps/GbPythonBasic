income = int(input("Please, input income: "))
outcome = int(input("Please, input outcome: "))
if income < outcome:
    print("You loose money")
elif income == outcome:
    print("Its equals")
else:
    print("You get money")
