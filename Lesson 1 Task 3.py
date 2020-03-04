# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.

n = int(input('Введите число: '))
print(n + int(str(n) + str (n)) + int(str(n) + str(n) + str(n)))