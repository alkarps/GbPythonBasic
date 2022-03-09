import json

avr_name = "average_profit"
profit_list = [{}, {avr_name: 0}]
with open("part7.txt", encoding="utf-8") as file:
    profit_avr = 0
    profit_company_count = 0
    for _company in file.readlines():
        company = _company.split()
        profit = float(company[2]) - float(company[3])
        if profit > 0:
            profit_avr = (profit_avr * profit_company_count + profit) / (profit_company_count + 1)
            profit_company_count += 1
        profit_list[0][company[0]] = profit
    profit_list[1][avr_name] = profit_avr
print(profit_list)
with open("part7.json", "w", encoding="utf-8") as file:
    json.dump(profit_list, file)
