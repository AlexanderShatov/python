# Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = ['a', 'b', 'c', 'd', 'e']
if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        my_list2 = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = my_list2
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        my_list2 = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = my_list2
        i += 2
print(my_list)