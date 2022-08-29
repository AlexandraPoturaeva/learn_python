# 10.1 Работа со вложенными циклами

# Задача 1. Таблица умножения

# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row * col, end= '\t')
#     print('')

# Задача 2. Таблица суммы

from random import randint

# n = randint(5, 20)
#
# for row in range(n+1):
#     for col in range(n+1):
#         print(row + col, end='\t')
#     print(' ')

# Задача 3. Анализ данных

# for row in range(0, 10):
#     for col in range(0, -10, -1):
#         print(row + col, end='\t')
#     print(' ')

# 10.2 Использование if во вложенных циклах

# Задача 1. Матрица

# size = randint(5, 15)
#
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if row % 2 == 0:
#             print(row, end=' ')
#         else:
#             print(col, end= ' ')
#     print(' ')

# Задача 2. Чёрный ящик

# size = randint(5, 15)
#
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if col % 3 == 0:
#             print(col, end='\t')
#         else:
#             print(row, end='\t')
#     print(' ')

# Задача 3. Координатные оси

# for row in range(20):
#     for col in range(50):
#         if col == 24:
#             print('|', end= '')
#         elif row == 9:
#             print('-', end= '')
#         else:
#             print(' ', end= '')
#     print(' ')

# 10.3 Работа с двумя счетчиками в условном операторе

# Задача 1. Врата

# size_vert = randint(5, 20)
# size_hor = randint(5, 20)
#
# for row in range(size_vert):
#     for col in range(size_hor):
#         if row == 0:
#             print('-', end='')
#         elif col == 0 or col == size_hor - 1:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print('')

# Задача 2. Дорога

# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end='')
#         elif col == 24:
#             print('|', end='')
#         elif col == row + 29:
#             print('\\', end='')
#         elif col == - row + 19:
#             print('/', end='')
#         else:
#             print(' ',end='')
#     print('')

# Задача 3. Диагональная матрица

# size = randint(3, 15)
#
# for row in range(size):
#     for col in range(size):
#         if row == -col + size - 1:
#             print(1, end= ' ')
#         elif row < -col + size - 1:
#             print(0, end= ' ')
#         elif row > -col + size - 1:
#             print(2, end= ' ')
#     print('')

# 10.4 Решение задач с помощью вложенных циклов

# Задача 1. Электронная очередь

# people = randint(3, 8)
#
# for hour in range(people):
#     print('Идёт ' + str(hour) + '-й час')
#     for number in range(hour, people):
#         print('Номер в очереди:', number)
#     print(' ')
# print('Очередь обслужена')

# Задача 2. Цифры больше пяти

# sequence_number = randint(3, 10)
# print('Последовательность из', sequence_number, 'чисел')
# numeral_5_count = 0
#
# for i in range(1, sequence_number + 1):
#     number = randint(1, 10000)
#     print(str(i)+ '-е число: '+ str(number))
#     for numeral in str(number):
#         if int(numeral) > 5:
#             numeral_5_count += 1
# print('Количество цифр больше 5:', numeral_5_count)

# Задача 3. Лестница чисел

# size = randint(5, 20)
#
# for row in range(size):
#     for col in range(row, size):
#         print(col, end= '\t')
#     print('')

# 10.6 Практическая работа

# Задача 1. Тестовое задание

# for row in range(6):
#     for col in range(0, 11, 2):
#         print(row + col, end= '\t')
#     print('')

# Задача 2. Лестница

# size = randint(4, 15)
# print('Число:', size)
#
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if col <= row:
#             print(row, end= '\t')
#         else:
#             print(' ', end= '')
#     print(' ')

# Задача 3. Рамка

# size_hor = randint(5, 30)
# size_vert = randint(5, 30)
#
# for row in range(size_vert):
#     for col in range(size_hor):
#         if col == 0 or col == size_hor - 1:
#             print('|', end= '')
#         elif row == 0 or row == size_vert - 1:
#             print('-', end= '')
#         else:
#             print(' ', end= '')
#     print('')

# Задача 4. Крест

# size = randint(5, 20)
#
# for row in range(size):
#     for col in range(size):
#         if row == col or row == size - col - 1:
#             print('^', end= '')
#         else:
#             print(' ', end= '')
#     print('')

# Задача 5. Простые числа

# count = randint(5, 20)
# print('Количество чисел:', count)
#
# for i in range(1, count + 1):
#     number = randint(1, 100)
#     print(str(i) + '-е число: ' + str(number))
#     for num in range(2, number):
#         if number % num == 0:
#             count -= 1
#             break
#
# print('Количество простых чисел в последовательности:', count)

# Задача 6. Сумма факториалов

# number = randint(1, 10)
# print('n =', number)
# factorial_sum = 0
# factorial = 1
#
# for num in range(1, number + 1):
#     for i in range(1, num + 1):
#         factorial *= i
#     factorial_sum += factorial
#     factorial = 1
#
# print('Сумма факториаалов 1! + 2! + 3! + ... + n!:', factorial_sum)

# Задача 7. Наибольшая сумма цифр

# count = randint(3, 8)
# print(count, 'чисел')
# sum_current = 0
# sum_max = 0
# number_max = 0
#
# for i in range(1, count+1):
#     number = randint(1, 10000)
#     print(str(i) + '-е число: ' + str(number))
#     for num in str(number):
#         sum_current += int(num)
#     if sum_current > sum_max:
#         sum_max = sum_current
#         number_max = number
#     sum_current = 0
#
# print('Число', number_max, 'имеет максимальную сумму чисел', sum_max)

# Задача 8. Пирамидка

# size = randint(4, 20)
# print('Высота:', size)
#
# for row in range(size):
#     for col in range(size + size - 1):
#         if row < size - col - 1 or col > size + row - 1:
#             print(' ', end='.')
#         else:
#             print('#', end='.')
#     print(' ')

# Задача 9. Пирамидка 2

# Вариант 1

# size = randint(4, 20)
# print('Высота:', size)
# sum = 0
#
# for row in range(size):
#     for col in range(size + size - 1):
#         if row < size - col - 1 or col > size + row - 1:
#             print(' ', end='\t')
#         else:
#             if ((size % 2 > 0) and ((row + col) % 2 == 0)) or ((size % 2 == 0) and ((row + col) % 2 > 0)):
#                 print(1 + sum, end= '\t')
#                 sum += 2
#             else:
#                 print(' ', end= '\t')
#     print('')

# Вариант 2

# size = randint(4, 20)
# print('Высота:', size)
# new_num = 1
#
# for line in range(size):
#     space_count = size - line - 1
#     print('   ' * space_count, end='')
#     for number in range(line + 1):
#         print(new_num, end='   ')
#         new_num += 2
#     print(' ')

# Задача 10. Яма

# Вариант 1

# size = randint(4, 20)
# # size = 5
# print('Высота:', size)
#
# for row in range(size):
#     for col in range(size * 2):
#         if row < col < size * 2 - row - 1:
#             print('.', end = '\t')
#         else:
#             if size - col >= 1:
#                 print(size - col, end= '\t')
#             else:
#                 print(col - size + 1, end= '\t')
#     print(' ')

# Вариант 2

size = randint(4, 20)
size = 5
print('Высота:', size)

for line in range(size):
    for left_number in range(size, size - line - 1, -1):
        print(left_number, end='')
    point_count = 2 * (size - line -1)
    print('.' * point_count, end='')
    for right_number in range(size - line, size + 1):
        print(right_number, end='')
    print()