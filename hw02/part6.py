characters = ("название", "цена", "количество", "единица измерения")
goods = []

while True:
    if "y" == input("Хотите добавить новый товар? Введите плз Y, N: ").lower():
        good_name = input("Введите название товара: ")
        good_price = int(input("Введите цену товара: "))
        good_count = int(input("Введите количество товара: "))
        good_unit = input("Введите единицу измерения товара товара: ")
        goods.append((
            len(goods) + 1,
            {characters[0]: good_name, characters[1]: good_price, characters[2]: good_count, characters[3]: good_unit}
        ))
    else:
        break

print(f"Текущие товары: {goods}. Формируем аналитику...")

analytics_name = {good[1][characters[0]] for good in goods}
analytics_price = {good[1][characters[1]] for good in goods}
analytics_count = {good[1][characters[2]] for good in goods}
analytics_unit = {good[1][characters[3]] for good in goods}

analytics = {
    characters[0]: list(analytics_name),
    characters[1]: list(analytics_price),
    characters[2]: list(analytics_count),
    characters[3]: list(analytics_unit)
}

print(f"Аналитика сохраненных товаров: {analytics}")