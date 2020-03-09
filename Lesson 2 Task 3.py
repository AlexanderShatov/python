# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


seasons_list = ['Это зимний месяц', 'Это весенний месяц', 'Это летний месяц', 'Это осенний месяц']
seasons_dict = {1 : 'Это зимний месяц', 2 : 'Это весенний месяц', 3 : 'Это летний месяц', 4 : 'Это осенний месяц'}
month = int(input("Укажите месяц по номеру: "))

if month ==1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")