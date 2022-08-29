# 13.2 Возврат значений из функций. Оператор return

# Задача 1. Сумма чисел 2
import math
import random
from random import randint


# def sum_count(number):
#     summ = number * (number + 1) / 2
#     return summ
#
#
# number = randint(1, 100)
# summ = sum_count(number)
#
# print('Cумма от 1 до ', number, '=', summ)
# print('Сумма чисел от 1 до', summ, '=', sum_count(summ))

# Задача 2. «Назад в будущее»

# def gcd(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#
#     return a + b
#
#
# a = randint(0, 10000)
# b = randint(0, 10000)
# gcd = gcd(a, b)
#
#
# print('Числа', a, 'и', b)
# print('НОД =', gcd)

# Задача 3. Приоритет задач

# def get_numeral_count(number):
#     count = 0
#     while number > 0:
#         number //= 10
#         count += 1
#
#     return count
#
# task_number = randint(1, 10)
# print('Количество задач:', task_number)
#
# max_numeral_count = 0
# max_task = 0
#
# for i in range(1, task_number + 1):
#     number = randint(1, 100000)
#     print(str(i) + '-е число: ' + str(number))
#     numeral_count = get_numeral_count(number)
#     if numeral_count > max_numeral_count:
#         max_numeral_count = numeral_count
#         max_task = number
#
# print('Первая задача на обработку:', max_task)

# 13.3 Представление вещественных чисел в программе

# Задача 1. Возможности компьютера

# number = randint(1, 100)
# print('Число:', number)
# count = 0
#
# while number != 0:
#     number /= 2
#     count += 1
#     print(number)
# print('Итераций:', count)

# Задача 2. Тестирование

# number = float(input('Введите число в эксп. форме: '))
# x = 1
# count = 0
#
# while x <= 2:
#     x += number
#     count += 1
#
# print('Количество прибавлений: ', count)

# Задача 3. Урок информатики

# number = randint(11, 1000000000)
# print('Число:', number)
#
# exp = 0
#
# while number >= 10:
#     number /= 10
#     exp += 1
#
# print('Формат плавающей точки: x =', number, '*', 10, '**', exp)

# 13.4 Особенности работы с вещественными числами

# Задача 1. Опять налоги

# while True:
#     country_budget = float(input('Введите бюджет страны: '))
#     new_tax = float(input('Новые поступления (налог): '))
#     if country_budget + new_tax - country_budget > 1e-15:
#         print('Результат: Бюджет увеличится')
#     else:
#         print('Результат: Бюджет не изменится')

# Задача 2. Сравнение

# while True:
#
#     a = float(input('Введите первое число: '))
#     b = float(input('Введите второе число: '))
#     summ = float(input('Введите третье число: '))
#
#     if abs(a + b - summ) < 1e-15:
#         print('True')
#     else:
#         print('False')

# 13.6 Практическая работа

# Задача 1. Урок информатики 2

# number = random.uniform(0, 10000000)
# # number = 0.0012
# # number = 92345
# # number = 2
# print('Число:', number)
#
# exp = 0
# round_count = 0
#
# if number < 1:
#     while number < 1:
#         number *= 10
#         exp -= 1
#     number = math.ceil(number * 10) / 10
# elif 1 <= number <= 10:
#     exp = 0
# elif number > 10:
#     while number % 1 > 1e-15:
#         number *= 10
#         exp -= 1
#         print(number)
#     number = math.floor(number)
#     print(number)
#     if number > 10:
#         while number > 10:
#             number /= 10
#             exp += 1
#             round_count += 1
#
# print('Формат плавающей точки: x =', round(number, round_count), '*', 10, '**', exp)


# Задача 2. Функция максимума

# def max_number_search(a, b):
#     max_number = (abs((a - b)) + (a + b)) / 2
#     return max_number
#
#
# a = randint(-100, 100)
# b = randint(-100, 100)
# c = randint(-100, 100)
# print('Числа', a, ',', b, ',', c)
#
# max_number_ab = max_number_search(a, b)
# max_number_abc = max_number_search(max_number_ab, c)
# print('Наибольшее число:', int(max_number_abc))


# Задача 3. Число наоборот 2

# def reverse_number(number):
#     while number % 10 == 0:
#         number /= 10
#     reverse_number = ''
#     for digit in str(int(number)):
#         reverse_number = digit + reverse_number
#     return int(reverse_number)
#
# num_1 = randint(1, 1000)
# num_2 = randint(1, 1000)
# num_1_rev = reverse_number(num_1)
# num_2_rev = reverse_number(num_2)
# summ = num_2_rev + num_1_rev
# summ_rev = reverse_number(summ)
#
# print('Первое число:', num_1, '\nВторое число:', num_2,
#       '\nПервое число наоборот:', num_1_rev, '\nВторое число наоборот:', num_2_rev,
#       '\nСумма:', summ, '\nСумма наоборот:', summ_rev)

# Задача 4. Урок информатики 3

# num_exp = float(input('Введите число в экспоненциальной форме: '))
# num_exp = float('5e-15')
#
# log = math.log10(num_exp)
#
# print(math.floor(log)) # экспонента
# print(num_exp/(10**math.floor(log))) # мантисса

# Задача 5. Недоделка 2


# def chng_edge_digits(number, req_num_count):
#     num_count = 0
#     temp = number
#     while temp > 0:
#         num_count += 1
#         temp = temp // 10
#     if num_count < req_num_count:
#         print('В числе меньше ' + str(req_num_count) + '-х цифр.')
#     else:
#         last_digit = number % 10
#         first_digit = number // 10 ** (num_count - 1)
#         between_digits = number % 10 ** (num_count - 1) // 10
#         number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
#     return number
#
#
# first_n = int(input("Введите первое число: "))
# second_n = int(input("\nВведите второе число: "))
#
# chng_first_n = chng_edge_digits(first_n, 3)
# chng_second_n = chng_edge_digits(second_n, 4)
#
# print('\nИзменённое первое число:', chng_first_n)
# print('Изменённое второе число:', chng_second_n)
# print('\nСумма чисел:', chng_first_n + chng_second_n)

# Задача 6. Маятник

# amplitude = int(input('Введите начальную амплитуду: '))
# presicion = float(input('Введите амплитуду остановки: '))
#
# swing_count = 0
#
# while amplitude - presicion > 1e-15:
#     amplitude -= amplitude * 8.4 / 100
#     swing_count += 1
#
# print('Маятник считается остановившимся через', swing_count, 'колебаний')

# Задача 7. Яйца

# Вариант 1

# def find_depth(d):
#     x1 = 0
#     x2 = 4
#     while True:
#         x = x1 + (x2 - x1) / 2
#         y = x ** 3 - 3 * x ** 2 - 12 * x + 10
#         if y < 0:
#             x2 = x
#         elif y > d:
#             x1 = x
#         else:
#             print('Приблизительная глубина безопасной кладки:', x, 'м')
#             break
#
#
# # d = float(input('Введите максимально допустимый уровень опасности: '))
# d = 0.001
# find_depth(d)

# Вариант 2

# d = float(input('Введите максимально допустимый уровень опасности: '))
# # d = 0.001
#
# def f(x):
#     return x ** 3 - 3 * x ** 2 - 12 * x + 10
#
#
# def dih(x1, x2, d, fn):
#     while True:
#         x = x1 + (x2 - x1) / 2
#         y = fn(x)
#         if y < 0:
#             x2 = x
#         elif y > d:
#             x1 = x
#         else:
#             return x
#
#
# print('Приблизительная глубина безопасной кладки:', dih(0, 4, d, f), 'м')

# Задача 8. Сумма ряда

# precision = float(input('Введите точность: '))
#
# x = int(input('Введите x: '))
#
# result = 1
# numerator = 1
# denominator = 1
# count = 0
# sign = 1
# addMember = 1
#
# while abs(addMember) > precision:
#     numerator *= (x * x)
#     count += 2
#     denominator *= (count - 1) * count
#     sign *= (0 - 1)
#     addMember = sign * numerator / denominator
#     result += addMember
#
# print('Сумма ряда:', result)

# Задача 9. Аннуитетный платёж

# summ = float(input('Введите сумму кредита: '))
# years = int(input('На сколько лет выдан? '))
# percent = float(input('Сколько процентов годовых? '))
# print()

summ = 40e6
years = 5
percent = 0.06
period_count = 1


def calc_annuity_payment(summ, percent, years):
    k = (percent * ((1 + percent) ** years)) / (((1 + percent) ** years) - 1)
    return summ * k


def calc_percent_payment(summ, percent):
    return summ * percent


def calc_debt_payment(annuity_payment,  percent_payment):
    return annuity_payment - percent_payment


def calc_plan(period_count, summ, percent):
    print('Период', period_count)
    print('Остаток долга на начало периода:', summ)
    percent_payment = calc_percent_payment(summ, percent)
    print('Выплачено процентов:', percent_payment)
    debt_payment = calc_debt_payment(annuity_payment,  percent_payment)
    print('Выплачено тела кредита:',  debt_payment)
    print()

annuity_payment = calc_annuity_payment(summ, percent, years)

while period_count <= 3:
    calc_plan(period_count, summ, percent)
    period_count += 1
    summ -= calc_debt_payment(annuity_payment,  calc_percent_payment(summ, percent))

print('Остаток долга', summ)
print('===================')

years = years - period_count + 3
percent = 0.1
period_count = 1

annuity_payment = calc_annuity_payment(summ, percent, years)

while summ > 0.01:
    calc_plan(period_count, summ, percent)
    period_count += 1
    summ -= calc_debt_payment(annuity_payment,  calc_percent_payment(summ, percent))

print('Остаток долга:', summ)
