from lesson5.divisor_master import *


def valid_num(f):
    global num
    while True:
        num = input('Введите целое число от 1 до 1000: ')
        if not num.isdigit():
            print('Ожидается целое число')
            continue
        else:
            num = int(num)
            if num < 1 or num > 1000:
                print('Число должно быть в диапазоне от 1 до 1000')
                continue
        break
    return f

@valid_num
def get_result():
    # список простых чисел от 2 до num
    simple_numbers = simple_numbers_list(num)
    # список делителей числа num
    divs = dividers(num, simple_numbers)

    print('Число ', num)
    print('Простое' if num in simple_numbers else 'Составное')
    print('Делители: ', divs)
    print('Наибольший простой делитель: ', max_simple_divider(simple_numbers, divs))
    print('Каноническое разложение на множители: ', simple_multipliers(num, simple_numbers))
    print('Наибольший делитель: ', max_divider(divs))


if __name__ == '__main__':
    get_result()