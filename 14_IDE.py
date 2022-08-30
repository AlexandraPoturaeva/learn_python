# 14.3 Командная строка и интерпретатор
# Задача 1. Таблица умножения: возвращение

# for i in range(1, 11):
#     for num in range(1, 11):
#         print(i*num, end = '\t')
#     print('')

# Задача 2. Калькулятор

# while True:
#     operation = str(input('Введите операцию: '))
#     if operation != '+' and operation != '-' and operation != '*' and operation != '/':
#         print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
#     else:
#         num1 = int(input('Введите первое число: '))
#         num2 = int(input('Введите второе число: '))
#         if operation == '+':
#             print(num1, '+', num2, '=', num1+num2)
#         elif operation == '-':
#             print(num1, '-', num2, '=', num1 - num2)
#         elif operation == '*':
#             print(num1, '*', num2, '=', num1 * num2)
#         elif operation == '/':
#             print(num1, '/', num2, '=', num1 / num2)

# Задача 3. Калькулятор 2

# result = 0
# result_text = ''
#
# while True:
#     operation = str(input('Введите операцию: '))
#     operand_count = int(input('Сколько операндов? '))
#     if operation != '+' and operation != '-' and operation != '*' and operation != '/':
#         print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
#     else:
#         num1 = int(input('Введите операнд 1: '))
#         result = num1
#         result_text += (str(num1) + ' ')
#         for operand in range(2, operand_count + 1):
#             num = int(input('Введите операнд ' + str(operand) + ': '))
#             result_text += (operation + ' ' + str(num) + ' ')
#             if operation == '+':
#                 result += num
#             elif operation == '-':
#                 result -= num
#             elif operation == '*':
#                 result *= num
#             elif operation == '/':
#                 result /= num
#     result_text += ('= ' + str(result))
#     print(result_text)
#     result = 0
#     result_text = ''
#     print()

# 14.4 Работа в PyCharm. Отладка программ
# Задача 2. НОД

# def gcd(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     print('Наибольший общий делитель:', a + b)
#
#
# gcd(4782, 698)

# Задача 3. Сессия

# print("Введите первую точку")
# x1 = float(input('X: '))
# y1 = float(input('Y: '))
# print("\nВведите вторую точку")
# x2 = float(input('X: '))
# y2 = float(input('Y: '))
#
#
# x_diff = x1 - x2
# y_diff = y1 - y2
#
# print("\nУравнение прямой, проходящей через эти точки:")
# if x_diff == 0:
#     print('x =', x1)
# elif y_diff == 0:
#     print('y =', y1)
# else:
#     k = y_diff / x_diff
#     b = y2 - k * x2
#     print("y = ", k, " * x + ", b)

# 14.8 Практическая работа
# Задача 3. Сумма и разность

import random

# number = random.randint(0, 1000000)
# print('Число:', number)
#
# def summ_figures(number):
#     sum = 0
#     while number != 0:
#         sum += number % 10
#         number //= 10
#     return sum
#
# def count_figures(number):
#     count = 0
#     for figure in str(number):
#         count += 1
#     return count
#
#
# print('Сумма чисел:', summ_figures(number))
# print('Количество цифр в числе:', count_figures(number))
# print('Разность суммы и количества цифр:', summ_figures(number) - count_figures(number))

# Задача 4. Число наоборот 3

# number_1 = round(random.uniform(0, 1000), 3)
# number_2 = round(random.uniform(0, 1000), 3)
#
# print('Первое число:', number_1, '\nВторое число:', number_2)
#
# def reverse_number(number):
#     whole_part_reversed = str(int(number // 1))[::-1]
#     decimal_part_reversed = str(int(number % 1 * 1000))[::-1]
#     number_reversed = float(whole_part_reversed + '.' + decimal_part_reversed)
#     return number_reversed
#
# print('Первое число наоборот:', reverse_number(number_1), '\nВторое число наоборот:', reverse_number(number_2),
#       '\nСумма:', reverse_number(number_1) + reverse_number(number_2))

# Задача 5. Наименьший делитель

from random import randint
#
# number = randint(1, 1000)
# print('Число:', number)
#
#
# def smallest_divisor(number):
#     divisor = 2
#     while True:
#         remains = number % divisor
#         divisor += 1
#         if remains == 0:
#             break
#     return divisor - 1
#
# print('Наименьший делитель, отличный от единицы:', smallest_divisor(number))

# Задача 6. Монетка 2
# x = random.uniform(-100, 100)
# y = random.uniform(-100, 100)
# radius = randint(0, 100)
# print('X:', x, '\nY:', y, '\nРадиус:', radius)
#
#
# def check_point(x, y, radius):
#     if (abs(x) <= radius) and (abs(y) <= radius):
#         return 'Монетка где-то рядом'
#     else:
#         return 'Монетки в области нет'
#
# print(check_point(x, y, radius))

# Задача 7. Годы

year_1 = randint(1000, 2022)
year_2 = year_1 + randint(0, 1500)
print('Первый год:', year_1, '\nВторой год:', year_2)
print('Годы от', year_1, 'до', year_2, 'с тремя одинаковыми цифрами:')


def three_same_figures(year):
    fig_1 = year // 1000
    fig_2 = year // 100 % 10
    fig_3 = year // 10 % 10
    fig_4 = year % 10
    if (fig_1 == fig_2 == fig_3 and fig_3 != fig_4) or (fig_1 == fig_3 == fig_4 and fig_4 != fig_2) or (fig_1 == fig_2 == fig_4 and fig_4 != fig_3) or (fig_2 == fig_3 == fig_4 and fig_4 != fig_1):
        return str(year) + '\n'
    else:
        return ''


def bad_years(year_1, year_2):
    bad_years = ''
    for year in range(year_1, year_2 + 1):
        bad_years += three_same_figures(year)
    print(bad_years)

bad_years(year_1, year_2)
