"""
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
"""

for i in range(1, 6):
    print(i, ':', 0)


"""
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
"""

step = 0
count_fives = 0
while step < 10:
    num = input('Введите целое число: ')
    if not num.isdigit():
        print('Это не целое число!')
        continue
    if num == '5':
        count_fives += 1
    step += 1
print('Количество пятёрок: ', count_fives)


"""
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
"""

comp = 1
for k in range(1, 11):
    comp *= k
print('Произведение ряда чисел от 0 до 10 равно: ', comp)


"""
Задача 6
Найти сумму цифр числа.
"""

integer_number = 62535
sum = 0
while integer_number > 0:
    sum += integer_number % 10
    integer_number = integer_number // 10
print('Сумма цифр равна: ', sum)


"""
Задача 7
Найти произведение цифр числа.
"""

integer_number = 625
comp = 1
while integer_number > 0:
    comp *= integer_number % 10
    integer_number = integer_number // 10
print('Произведение цифр равно: ', comp)


"""
Задача 9
Найти максимальную цифру в числе
"""

integer_number = 6925
max = 0
while integer_number > 0:
    num = integer_number % 10
    if num > max:
        max = num
    integer_number = integer_number // 10
print('Максимальная цифра в числе: ', max)


"""
Задача 10
Найти количество цифр 5 в числе
"""

integer_number = 69525
count_fives = 0
while integer_number > 0:
    num = integer_number % 10
    if num == 5:
        count_fives += 1
    integer_number = integer_number // 10
print('Количество пятёрок в числе: ', count_fives)