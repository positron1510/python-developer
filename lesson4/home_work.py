sample_names = ['Anna', 'Andrey', 'Kristina', 'Maxim', 'Svyatoslav', 'Ekaterina', 'Elizaveta', 'Natalya',
         'Svetlana', 'Anatoly', 'Kirill', 'Anton', 'Vladimir', 'Antonina', 'Roman', 'Ludmila', 'Alexsandr', 'Konstantin', 'Victor', 'Polina']


import random

"""
1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка 
(могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
"""

def F(names, count):
    return list(map(lambda x: random.choice(names), range(count)))

if __name__ == '__main__':
    print('Сто случайных имен:')
    print(F(sample_names, 100))

"""
2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
"""

def popular_name(names, count):
    names = F(names, count)
    index = 0
    max_entry = 0

    for i in range(len(names)):
        count = names.count(names[i])
        if count > max_entry:
            max_entry = count
            index = i

    return names[index]

if __name__ == '__main__':
    print()
    print('Самое частое имя: : ', popular_name(sample_names, 100))

"""
3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
"""

def rare_letter(names, count):
    letters = list(map(lambda x: x[0], F(names, count)))
    min_entry = len(letters)
    index = 0

    for i in range(len(letters)):
        count = letters.count(letters[i])
        if count < min_entry:
            min_entry = count
            index = i

    return letters[index]

if __name__ == '__main__':
    print()
    print('Самая редкая буква с которой начинается имя: ', rare_letter(sample_names, 100))

"""
4.  В файле с логами найти дату самого позднего лога (по метке времени): https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
"""

if __name__ == '__main__':
    from datetime import datetime

    with open('logs.txt', mode='r', encoding='utf-8') as f:
        logs = f.readlines()

    dt = []

    for k in range(len(logs)):
        arr = logs[k].split()
        args = list(map(lambda d: int(d), arr[0].split('-'))) + list(map(lambda d: int(d.split(',')[0]), arr[1].split(':')))
        dt.append(datetime(*args))

    print()
    print('Самая поздняя метка времени в логе: ', max(*dt))
