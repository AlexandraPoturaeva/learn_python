# 12.2 Функции и их вызов

# Задача 1. Робот

# def greeting():
#     print('Привет!')
#     print('Добро пожаловать!')
#
#
# while True:
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting()
#     print('Следующий.\n')

# Задача 2. Провизия

# def countFood():
#     a = int(input())
#     b = int(input())
#     print("Всего", a + b, "шт.")
#
# print("Сколько мешков рыбы и мяса?")
# countFood()
#
# print("Сколько буханок белого и чёрного хлеба?")
# countFood()
#
# print("Сколько вёдер воды и молока?")
# countFood()

# Задача 3. Почта

# while True:
#     surname = input('Фамилия: ')
#     name = input('Имя: ')
#     street = input('Улица: ')
#     apt = input('Дом: ')
#     print()
#
#     def person_data():
#         print('Фамилия:', surname)
#         print('Имя:', name)
#         print('Улица:', street)
#         print('Дом:', apt)
#         print()
#
#
#     person_data()
#     person_data()
#     person_data()

# 12.3 Функции с одним параметром

# Задача 1. Вода

# def aboutWater(price):
#     print('Название: КлирВотер')
#     print('Производитель: ВодЗавод')
#     print(price)
#     print()
#
# aboutWater(25)
# aboutWater(30)
# aboutWater(40)

# Задача 2. Вот это объёмы 2
import math

# def sphereArea(r):
#     s = 4 * math.pi * (r ** 2)
#     print('Площадь сферы:', s)
#
# def sphereVolume(r):
#     v = math.pi * (r ** 3) * 4 / 3
#     print('Объём шара: ', v)
#
# r = float(input('Введите радиус планеты: '))
# sphereArea(r)
# sphereVolume(r)

# Задача 3. Простые числа

from random import randint


#
#
# def is_prime(count):
#     for number in range(2, count + 1):
#         for num in range(2, number):
#             if number % num == 0:
#                 count -= 1
#                 break
#     print('Количество простых чисел:', count)
#
#
# count = randint(1, 100)
# print('Чисел в последовательности:', count)
# is_prime(count)

# 12.4 Функции с несколькими параметрами

# Задача 1. Среднее арифметическое

# Вариант 1

# def average(a, b):
#     summ = 0
#     count = (b - a) + 1
#     for i in range(a, b + 1):
#         summ += i
#     print('Среднее арифметическое:', summ / count)
#
#
# a = randint(0, 10)
# b = randint(11, 20)
#
# print('Левая граница:', a, '\nПравая граница:', b)
#
# average(a, b)

# Вариант 2

# def average(a, b):
#     count = (b - a) + 1
#     summ = (a + b) / 2 * count
#     print('Среднее арифметическое:', summ / count)
#
#
# a = randint(0, 10)
# b = randint(11, 20)
# a = 3
# b = 8
#
# print('Левая граница:', a, '\nПравая граница:', b)
#
# average(a, b)

# Задача 2. Почта 2

# def person_data(surname, name, country, city, street, apt):
#     print('Фамилия:', surname)
#     print('Имя:', name)
#     print('Страна проживания:', country)
#     print('Город', city)
#     print('Улица:', street)
#     print('Дом:', apt)
#     print()
#
#
# while True:
#     surname = input('Фамилия: ')
#     name = input('Имя: ')
#     country = input('Страна проживания: ')
#     city = input('Город: ')
#     street = input('Улица: ')
#     apt = input('Дом: ')
#     print()
#
#     person_data(surname, name, country, city, street, apt)

# Задача 3. GPS-навигатор 2.0

# def distance(x, y):
#     distanse = math.sqrt(x ** 2 + y ** 2)
#     print('Расстояние до точки:', distanse)
#     print()
#
#
# def distance_between(x, y, x_1, y_1):
#     distanse = math.sqrt((x_1 - x) ** 2 + (y_1 - y) ** 2)
#     print('Расстояние между точками:', distanse)
#     print()
#
# while True:
#     answer = int(input('Введите запрос (1 - найти расстояние от себя до точки, 2 - найти расстояние между двумя точками): '))
#
#     if answer == 1:
#         x = int(input('Введите координату x: '))
#         y = int(input('Введите координату y: '))
#         distance(x, y)
#     elif answer == 2:
#         x = int(input('Введите координату x первой точки: '))
#         y = int(input('Введите координату y первой точки: '))
#         x_1 = int(input('Введите координату x второй точки: '))
#         y_1 = int(input('Введите координату y второй точки: '))
#         distance_between(x, y, x_1, y_1)
#     else:
#         print('Ошибка ввода')

# 12.6 Практическая работа

# Задача 1. Сумма чисел

# def summ(number):
#     summ = number * (number + 1) / 2
#     print('Я знаю, что сумма чисел от 1 до', number, 'равна', summ)
#
# number = randint(1, 100)
# print('Число: ', number)
#
# summ(number)

# Задача 2. Функция в функции

# def negative():
#     print('Отрицательное')
#
# def positive():
#     print('Положительное')
#
# def test():
#     number = randint(-100, 100)
#     print('Число:', number)
#     if number > 0:
#         positive()
#     elif number < 0:
#         negative()
#     else:
#         print('Нужно ввести целое число')
#
# test()

# Задача 3. Апгрейд калькулятора
# def digits_sum(number):
#     summ = 0
#     for i in str(number):
#         summ += int(i)
#     print('Сумма цифр: ', summ)
#
#
# def max_digit(number):
#     max_digit = 0
#     for i in str(number):
#         if int(i) > max_digit:
#             max_digit = int(i)
#     print('Максимальная цифра:', max_digit)
#
#
# def min_digit(number):
#     min_digit = 10
#     for i in str(number):
#         if int(i) < min_digit:
#             min_digit = int(i)
#     print('Минимальная цифра:', min_digit)
#
#
# while True:
#     number = randint(0, 1000)
#     print('Число:', number)
#     choice = int(input('Выберите действие (1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра): '))
#     if choice == 1:
#         digits_sum(number)
#     elif choice == 2:
#         max_digit(number)
#     elif choice == 3:
#         min_digit(number)
#     else:
#         print('Ошибка ввода')

# Задача 4. Число наоборот

# Вариант 1

def reverse_number(number):
    reverse_number = ''
    for digit in str(number):
        reverse_number = digit + reverse_number
    print(reverse_number)


while True:
    number = int(input('Введите число: '))
    if number != 0:
        reverse_number(number)
    else:
        print('Программа завершена')
        break

# Вариант 2

# def reverse_number(number):
#     reverse_number = str(number)[::-1]
#     print(reverse_number)
#
#
# while True:
#     number = int(input('Введите число: '))
#     if number != 0:
#         reverse_number(number)
#     else:
#         print('Программа завершена')
#         break

# Дополнительно. Вариант 1

# def reverse_number(number):
#     while number % 10 == 0:
#         number /= 10
#     reverse_number = ''
#     for digit in str(int(number)):
#         reverse_number = digit + reverse_number
#     print(reverse_number)
#
#
# while True:
#     number = int(input('Введите число: '))
#     if number != 0:
#         reverse_number(number)
#     else:
#         print('Программа завершена')
#         break

# Дополнительно. Вариант 2

# def reverse_number(number):
#     while number % 10 == 0:
#         number /= 10
#     reverse_number = str(int(number))[::-1]
#     print(reverse_number)
#
#
# while True:
#     number = int(input('Введите число: '))
#     if number != 0:
#         reverse_number(number)
#     else:
#         print('Программа завершена')
#         break

# Задача 5. Текстовый редактор
# def count_letters(text, digit, letter):
#     digit_count = 0
#     letter_count = 0
#     for symbol in text:
#         if symbol == str(digit):
#             digit_count += 1
#         elif symbol == letter:
#             letter_count += 1
#     print('Количество цифр', digit, ':', digit_count)
#     print('Количество букв', letter, ':', letter_count)
#     print()
#
#
# while True:
#     text = input('Введите текст: ')
#     digit = int(input('Какую цифру ищем? '))
#     letter = input('Какую букву ищем? ')
#     count_letters(text, digit, letter)

# Задача 6. Монетка

# def coin_search(x, y):
#     if -1 <= x <= 1 and -1 <= y <= 1:
#         print('Монетка где-то рядом')
#     else:
#         print('Монетки в области нет')
#
# while True:
#     x = float(input('Введите координату x: '))
#     y = float(input('Введите координату y: '))
#     coin_search(x, y)

# Задача 7. Опять?

# def min_number_search(a, b):
#     min_number = (a + b) - (abs((a - b)) + (a + b)) / 2
#     print('Наименьшее число:', min_number)
#
#
# a = randint(-100, 100)
# b = randint(-100, 100)
# print('Числа', a, ',', b)
# min_number_search(a,b)

# Задача 8. НОД

# Вариант 1

# def max_common_div(a, b):
#     min_number = (a + b) - (abs((a - b)) + (a + b)) / 2
#     max_common_div = 0
#     for number in range(1, int(min_number) + 1):
#         if a % number == 0 and b % number == 0:
#             max_common_div = number
#     print('НОД: ', max_common_div)
#
# a = randint(0, 10000)
# b = randint(0, 10000)
# print('Числа', a, ',', b)
# max_common_div(a, b)

# Вариант 2
# def max_common_div(a, b):
#     max_num = (abs((a - b)) + (a + b)) / 2
#     min_num = a + b - max_num
#     while True:
#         r = max_num % min_num
#         if r != 0:
#             max_num = min_num
#             min_num = r
#         else:
#             break
#     print('НОД:', int(min_num))
#
#
# a = randint(0, 10000)
# b = randint(0, 10000)
# print('Числа', a, ',', b)
# max_common_div(a, b)

# Вариант 3

# def max_common_div(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     print('НОД:', a + b)
#
#
# a = randint(0, 10000)
# b = randint(0, 10000)
# print('Числа', a, ',', b)
# max_common_div(a, b)

# Вариант 4

# a = randint(0, 10000)
# b = randint(0, 10000)
# print('Числа', a, ',', b)
# print('НОД:', math.gcd(a, b))

# Задача 9. Недоделка

# def mainMenu():
#     choice = int(input('Выберите игру (1 - Камень, ножницы, бумага, 2 - Угадай число): '))
#     if choice == 1:
#         rock_paper_scissors()
#     elif choice == 2:
#         guess_the_number()
#     else:
#         print('Ошибка ввода. Попробуйте ещё раз.')
#         mainMenu()
#
#
# def rock_paper_scissors():
#     while True:
#         user_answer = int(input('Ваш ход (1 - камень, 2 - ножницы, 3 - бумага, 0 - выйти из игры): '))
#         if user_answer == 0:
#             break
#         elif user_answer < 0 or user_answer > 3:
#             print('Ошибка ввода. Попробуйте ещё раз.')
#         else:
#             comp_answer = randint(1, 3)
#             print('Ваш выбор:', user_answer, '\nКомпьютер:', comp_answer)
#             if (user_answer == 1 and comp_answer == 2) or (user_answer == 2 and comp_answer == 3) or (user_answer == 3 and comp_answer == 1):
#                 print('Вы выиграли')
#             elif (user_answer == 2 and comp_answer == 1) or (user_answer == 3 and comp_answer == 2) or (user_answer == 1 and comp_answer == 3):
#                 print('Вы проиграли')
#             else:
#                 print('Пока ничья. Попробуйте ещё раз.')
#     mainMenu()
#
#
# def guess_the_number():
#     number = randint(0, 100)
#     attempts = 0
#     while True:
#         user = int(input('Введите число от 0 до 100: '))
#         attempts +=1
#         if user > number:
#             print ('Число больше, чем нужно. Попробуйте ещё раз!')
#         elif user < number:
#             print('Число меньше, чем нужно. Попробуйте ещё раз!')
#         else:
#             print('Вы угадали! Число попыток: ', attempts)
#             break
#     mainMenu()
#
#
# mainMenu()
