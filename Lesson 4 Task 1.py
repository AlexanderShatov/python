# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

def res(work_time, salary, bonus):
    return (work_time * salary) + bonus

work_time, salary, bonus = sys.argv

try:
    time = int(work_time)
    salary = int(salary)
    bonus = int(bonus)

except ValueError:
    print('Ошибка')

print(res(work_time, salary, bonus))