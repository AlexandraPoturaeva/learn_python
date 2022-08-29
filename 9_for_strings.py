from random import randint

# 9.2 Сравнение строк

# Задача 1. Урок литературы

# grade_count_2 = 0
#
# for i in range(5):
#     answer = input('Кто написал произведение "Евгений Онегин"?: ')
#     if answer == 'Пушкин' or answer == 'пушкин':
#         print('Верно!')
#         break
#     grade_count_2 += 1
#     print('Неправильно! Два!')
# print('Количество двоек:', grade_count_2)

# Задача 2. Начальник

# answer = input('Ты выполнил задание? ')
# while answer != 'Да, конечно, сделал':
#     answer = input('Ты выполнил задание? ')
# print('Молодец! Сейчас дам новое')

# Задача 3. Дразнилка.

# name = input('Как тебя зовут? ')
# print(name + ', купи слона ')
#
# while True:
#     answer = input()
#     print('Все говорят "'+ answer + '" , а ты купи слона!' )

# 9.3 Цикл for: итерирование по строке

# Задача 1. Python!

# for i in 'Python!':
#     print(i)

# Задача 2. Вирус

# text = input('Введите текст: ')
# for i in text:
#     print(i * 3)

# Задача 3.

# text = input('Введите текст: ')
# capital_count = 0
# small_count = 0
#
# for i in text:
#     if i == 'Ы':
#         capital_count += 1
#     if i == 'ы':
#         small_count += 1
#
# print('Больших букв Ы:', capital_count)
# print('Маленьких букв Ы:', small_count)

# 9.4 Дополнительные возможности функции print

# Задача 1. Доска

# print('-' * 10)
#
# for i in range(0, 4):
#     print('|', end='')
#     for j in range(0, 8):
#         print('0', end='')
#     print('|')
#
# print('-' * 10)

# Задача 2. Локальная сеть

# number = randint(0, 100)
# step = randint(0, 100)
# summ = 0
# print('Число:', number, '\nШаг:',step)
#
# print('\nIP-адрес:', end=' ')
# for i in range(3):
#     print(number, end='.')
#     summ += number
#     number += step
# print(summ)

# Задача 3. Табло

# number = randint(0, 100)
# print('Число:', number)
#
# print('\n-=-', end= ' ')
# for i in range(0, number, 10):
#     print(i, end=' -=- ')

# 9.6 Практическая работа

# Задача 1. Календарь

# day = input('Введите день недели: ')
# number = 0
#
# for i in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'):
#     number += 1
#     if i == day:
#         print('Номер дня недели:', number)
#         break

# Задача 2. Я стал новым пиратом!

# right_word = 0
# for i in range(1, 11):
#     word = input('Что крикнул '+ str(i) + '-й пират? ')
#     if word == 'Карамба' or word == 'карамба':
#         right_word += 1
# print(right_word, 'пирата(ов) попадут на борт')

# Задача 3. Кривой мессенджер

# Вариант 1
# text = input('Введите текст: ')
# number = 0
#
# for letter in text:
#     number += 1
#     if letter == '*':
#         print('Символ ‘*’ стоит на позиции', number)
#         break

# Вариант 2
# text = input('Введите текст: ')
#
# for i, letter in enumerate(text, start=1):
#     if letter == '*':
#         print('Символ ‘*’ стоит на позиции', i)
#         break

# Вариант 3

# text = input('Введите текст: ')
# print('Символ ‘*’ стоит на позиции', text.find('*') + 1)

# Задача 4. Театр

# Вариант 1

# row_count = randint(3, 10)
# seat_count = randint(5, 20)
# meter_count = randint(1, 5)
# print('Количество рядов:', row_count, '\nКоличество мест:', seat_count, '\nКоличество метров между рядами:', meter_count)

# for row in range(row_count):
#     for seat in range(seat_count):
#         print('=', end='')
#     print(' ', end='')
#     for meter in range(meter_count):
#         print('*', end='')
#     print(' ', end='')
#     for seat in range(seat_count):
#         print('=', end='')
#     print('')

# Вариант 2

# row_count = randint(3, 10)
# seat_count = randint(5, 20)
# meter_count = randint(1, 5)
# print('Количество рядов:', row_count, '\nКоличество мест:', seat_count, '\nКоличество метров между рядами:', meter_count)
#
# text = ('=' * seat_count + ' ' + '*' * meter_count + ' ' + '=' * seat_count)
# for row in range(row_count):
#     print(text)

# Задача 5. Марсоход 2

# x = 8
# y = 10
#
# while True:
#     move = input('Марсоход находится на позиции ' + str(x) + ', ' + str(y) + ', введите команду:')
#     if move == 'w' or move == 'W':
#         x += 1
#         if x >= 15:
#             x = 15
#     elif move == 's' or move == 'S':
#         x -= 1
#         if x <= 0:
#             x = 0
#     elif move == 'a' or move == 'A':
#         y -= 1
#         if y <= 0:
#             y = 0
#     elif move == 'd' or move == 'D':
#         y += 1
#         if y >= 20:
#             y = 20

# Задача 6. Спецшифр

# text = input('Введите строку: ')
# previous_letter = ''
# count = 0
# counts = ''
#
# for letter in text:
#     if letter == 's':
#         count += 1
#     elif letter != 's' and previous_letter == 's':
#         counts += str(count)
#         count = 0
#     previous_letter = letter
#
# if count > 0:
#     counts += str(count)
#
# print(counts)
#
# max_count = 0
# for i in counts:
#     if int(i) > max_count:
#         max_count = int(i)
# print('Самая длинная последовательность:', max_count)

# Задача 7. Великий и могучий

# text = input('Введите текст: ')
# count = 0
# counts = ''
#
# for letter in text:
#     if letter != ' ':
#         count += 1
#     elif letter == ' ':
#         counts += str(count)
#         count = 0
#
# if count > 0:
#     counts += str(count)
#
# print(counts)
#
# max_count = 0
# for i in counts:
#     if int(i) > max_count:
#         max_count = int(i)
# print('Самая длинное слово, букв:', max_count)

# Задача 8. Колонтитул

# symbols_count = randint(20, 40)
# exclamation_count = symbols_count - randint(10, 20)
# approx_count = symbols_count - exclamation_count
# print('Количество символов:', symbols_count, '\nКоличество восклицательных знаков:', exclamation_count)
#
# print('~' * (approx_count // 2) + '!' * exclamation_count + '~' * (approx_count - (approx_count // 2)))

# Задача 9. Коровы

# text = input('Введите расстановку коров в 10-ти стойлах (a - свободное стойло, b - занятое): ')
# production = 0
# production_summ = 0
#
# for i in text:
#     production += 2
#     if i == 'b':
#         production_summ += production
#
# print('При такой расстановке будет производиться', production_summ, 'л молока в день')

# Задача 10. Метод бутерброда

# Вариант 1

# encryption = input('Введите зашифрованный текст: ')
# encryption ='shacnidw'
# decryption = ''
# number = 0
# number_2 = 0
#
# for letter in encryption:
#     number += 1
#     if (number + 1) % 2 == 0:
#         decryption += letter
#
# if number % 2 != 0:
#     number -= 1
#
# while number > 0:
#     for letter in encryption:
#         number_2 += 1
#         if number_2 == number:
#             decryption += letter
#             number -= 2
#             number_2 = 0
#             break
#
# print('Расшифровка:', decryption)

# Вариант 2

# encryption ='shacnidw'
# decryption = ''
# number = 0
#
# for letter in encryption:
#     number += 1
#     if (number + 1) % 2 == 0:
#         decryption += letter
#
# if number % 2 != 0:
#     number = 1
# else:
#     number = 0
# encryption = encryption[::-1]
#
# for letter in encryption:
#     number += 1
#     if (number + 1) % 2 == 0:
#         decryption += letter
#
# print('Расшифровка:', decryption)

# Вариант 3

encryption ='shacnidw'
decryption = ''

for i in range(0, len(encryption), 2):
    decryption += encryption[i]

if len(encryption) % 2 != 0:
    start = 1
else:
    start = 0

encryption = encryption[::-1]

for i in range(start, len(encryption), 2):
    decryption += encryption[i]

print('Расшифровка:', decryption)