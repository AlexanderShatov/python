# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.

goods = []
while input("Добавить новый товар? Введите yes/no: ") == 'yes':
    number = int(input("Введите номер товара: "))
    features = {}
    while input("Добавить характеристики товара? Введите yes/no: ") == 'yes':
        feature_key = input("Введите характеристику товара: ")
        feature_value = input("Введите цену товара: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)

analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)