# 11.2 Ввод вещественного числа. Функции float и round

import random
from random import randint, randrange

# Задача 1. Ставки на спорт

# bet = randint(100, 10000)
# print('Сколько ставим?', bet)
#
# coef = round(random.uniform(1, 10), 3)
# print('Какой коэффициент?', coef)
#
# win = round(bet*coef, 2)
# print('Потенциальный выигрыш:', win)

# Задача 2. День рождения

# age = randint(1, 100)
# print('Возраст:', age)
#
# temp = round(random.uniform(34, 40), 1)
# print('Температура тела:', temp)
#
# gift_sum = round(age*temp*1.5, 2)
# print('Нужно подарить:', gift_sum)

# Задача 3. Индекс массы тела

# weight = round(random.uniform(40, 150), 1)
# height = round(random.uniform(1.4, 2.2), 2)
# print('Вес:', weight, '\nРост:', height)
#
# bmi = round(weight / height ** 2, 2)
# print('Индекс массы тела:', bmi)
#
# if bmi < 18.5:
#     print('Масса тела - недостаточная')
# elif bmi < 25:
#     print('Масса тела - нормальная')
# elif bmi < 30:
#     print('Масса тела - избыточная')
# else:
#     print('У Вас ожирение')

# 11.3 Приведение типов между int и float

# Задача 1. Космические рейнджеры

# chatles = randint(2000, 10000)
# CR = chatles / 2200
# spacecrafts = int(CR * 2)
# print('Сколько чатлов?', chatles, '\nЭто', CR, 'CR', '\nМожно купить кораблей:', spacecrafts)

# Задача 2. Компьютерное зрение

# x = random.uniform(0, 0.8)
# y = random.uniform(0, 0.8)
#
# print('По горизонтали:', x, '\nПо вертикали:', y)
# print('Фигура находится в клетке (' + str(int(x*10)) + ', ' + str(int(y*10)) + ')')

# Задача 3. Точность и аккуратность

# x = round(random.uniform(0, 0.8), 3)
# y = round(random.uniform(0, 0.8), 3)
#
# # x = 0.731
# # y = 0.167
#
# x_cell = int(x*10)
# y_cell = int(y*10)
#
# print('По горизонтали:', x, '\nПо вертикали:', y)
# print('Фигура находится в клетке (' + str(x_cell) + ', ' + str(y_cell) + ')')
#
# shift_x = round((x_cell + 0.5)/10 - x, 3)
# shift_y = round((y_cell + 0.5)/10 - y, 3)
#
# print('Поправьте положение фигуры на (' + str(shift_x) + ', ' + str(shift_y) + ')')

# 11.4 Математические функции. Работа с модулем math

# Задача 1. Герон

import math

# while True:
#     a = randint(1, 30)
#     b = randint(1, 30)
#     c = randint(1, 30)
#     if (a + b > c) and (a + c > b) and (c + b > a):
#         break
#
# print('a =', a, '\nb =', b, '\nc =', c)
#
# p = (a+b+c) / 2
# square = math.sqrt(p * (p - a)*(p - b)*(p - c))
# print('Площадь прямоугольника: ', square)

# Задача 2. World of tanks

# distance = round(random.uniform(0, 50), 3)
# angle = round(random.uniform(0, 360), 3)
# print('Расстояние:', distance, '\nУгол:', angle)
# angle /= 57.2957795
#
# x = round(distance * math.cos(angle), 3)
# y = round(distance * math.sin(angle), 3)
#
# print('Координаты танка: x =', x, 'y =', y)

# Задача 3. Мега-калькулятор

# number = random.uniform(0, 100)
# print(round(number, 3))

# print('Округление вниз:', math.floor(number))
# print('Округление вверх:', math.ceil(number))
# print('Модуль:', abs(number))
# print('Квадратный корень:', math.sqrt(number))
# print('Экспонента:', math.exp(number))
# print('Натуральный логарифм:', math.log(number))
# print('Логарифм по основанию 2:', math.log2(number))
# print('Логарифм по основанию 10:', math.log10(number))
# print('Синус:', math.sin(number))
# print('Косинус:', math.cos(number))

# 11.6 Практическая работа

# Задача 1. Конвертация

# EUR_cost = random.uniform(1, 1000)
# print('Стоимость покупки в евро:', round(EUR_cost, 2))
# RUB_cost = EUR_cost*1.25*60.87
# print('Стоимость покупки в рублях:', round(RUB_cost, 2))

# Задача 2. Грубая математика

# count = randint(1, 10)
# print('Количество чисел:', count)

# for i in range(1, count + 1):
#     number = random.uniform(-100, 100)
#     print(str(i) + '-е число: ' + str(number))
#     if number > 0:
#         print('x =', math.ceil(number), '\nlog(x) =', math.log(number))
#     else:
#         print('x =', math.floor(number), '\nexp(x) =', math.exp(number))

# Задача 3. Убийца Steam

# size = random.uniform(100, 1000)
# speed = random.uniform(0, 100)
#
# print('Размер файла для скачивания, Mb:', round(size, 2), '\nСкорость соединения, Mbps:', round(speed, 2))
#
# seconds = math.ceil(size / speed)
#
# for i in range(1, seconds):
#     download = speed * i
#     print('Прошло ' + str(i) + ' сек. Скачано ' + str(round(download, 2)) +
#           ' Mb (' + str(round(download / size * 100, 1)) + '%)')
#
# print('Скачивание обновления заняло', seconds, 'сек.')

# Задача 4. Первая цифра

# x = random.uniform(0, 100)
# print('Число:', x)
#
# number = math.floor((x - math.floor(x))*10)
#
# print('Первое число после ".":', number)

# Задача 5. Вот это объёмы!

# radius_random = random.uniform(1000, 10000)
# radius_random = 7000

# print('Радиус планеты:', round(radius_random, 2))
#
# volume_earth = 10.8321 * (10 ** 11)
# volume_random = (math.pi * (radius_random ** 3)) * 4 / 3
# comparison = volume_earth / volume_random
#
# if comparison > 1:
#     print('Объём планеты Земля больше в', round(comparison, 3), 'раза')
# else:
#     print('Объём планеты Земля меньше в (1/' + str(round(comparison, 3)) + ') = ' +
#     str(round(1/comparison, 3)) + ' раза')

# Задача 6. Метеостанция

# t_min = randint(0, 25)
# t_max = randint(26, 50)
# step = randint(0, 25)
#
# print('Ввод:', '\nНижняя граница:', t_min, '\nВерхняя граница:', t_max, '\nШаг:', step)
# print('Вывод:', '\nC', '\t F')
#
# for t in range(t_min, t_max + 1, step):
#     print(t, '\t', round(32 + t * 1.8))
#
# if (t_max - t_min) % step != 0:
#     print(t_max, '\t', round(32 + t_max * 1.8))

# Задача 7. Ход конём

# tries = 0
#
# while True:
#     x = random.uniform(0, 0.8)
#     y = random.uniform(0, 0.8)
#     x_point = int(x*10)
#     y_point = int(y*10)
#
#     x_new = random.uniform(0, 0.8)
#     y_new = random.uniform(0, 0.8)
#     x_new_point = int(x_new*10)
#     y_new_point = int(y_new*10)
#
#     x_shift = abs(x_new_point - x_point)
#     y_shift = abs(y_new_point - y_point)
#
#     tries += 1
#     print('Попытка №', tries)
#
#     print('Местоположение коня \nПо горизонтали:', round(x, 3), '\nПо вертикали:', round(y, 3))
#     print()
#     print('Местоположение точки \nПо горизонтали:', round(x_new, 3), '\nПо вертикали:', round(y_new, 3))
#     print()
#     print('Конь в клетке (' + str(x_point) + ', ' + str(y_point) +
#           '). Точка в клетке (' + str(x_new_point) + ', ' + str(y_new_point) + ')')
#
#     if (x_shift == 2 and y_shift == 1) or (x_shift == 1 and y_shift == 2):
#         print('Да, конь может ходить в эту точку.')
#         break
#     else:
#         print('Конь не может ходить в эту точку.')
#         print()

# Задача 8. Часы

# hour_angle = random.uniform(0, 360)
# print('Угол поворота часовой стрелки:', round(hour_angle, 2))
#
# minute_angle = (hour_angle % 30) * 12
#
# print('Угол поворота минутной стрелки:', round(minute_angle, 2))

# Задача 9. Уравнение

# while True:
#     a = random.uniform(-100, 100)
#     if a != 0:
#         break
# b = random.uniform(-100, 100)
# c = random.uniform(-100, 100)
#
# print('Дано квадратное уравнение: ' + str(a) + 'x + ' + str(b) + 'x + ' + str(c) + ' = 0')
#
# d = (b ** 2) - (4 * a * c)
#
# if d < 0:
#     print('Уравнение не имеет решения в действительных числах')
# elif d == 0:
#     x = (0 - b) / (a * 2)
#     print('x =', x)
# else:
#     x1 = ((0 - b) + math.sqrt(d)) / (a * 2)
#     x2 = ((0 - b) - math.sqrt(d)) / (a * 2)
#     print('x1 =', x1, 'x2 =', x2)

# Задача 10. За что?

a = randint(-100, 100)
b = randint(-100, 100)

print('Числа', a, ',', b)

max_number = (abs((a-b) + (a+b))/2
print('Наибольшее число:', max_number)