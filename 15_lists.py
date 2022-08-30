# 15.1 Списки и их инициализация

# Задача 1. Таблица степеней

# numbers = [3, 7, 5]
#
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#     for i in numbers:
#         print(i ** 2, i ** 3, i ** 4)
#     print()

# Задача 2. Очень простая задача

# numbers = []
#
# for i in range(0, 101):
#     numbers.append(i)
#
# print(numbers)

# Задача 3. Контроль

from random import randint
#
# workers_count = randint(10, 30)
# print('Кол-во сотрудников в офисе:', workers_count)
#
# workers_ID = []
#
# for num in range(1, workers_count + 1):
#     id = randint(1, 30)
#     print(str(num) + ') ID сотрудника: ' + str(id))
#     workers_ID.append(id)
#
# worker_ID_find = randint(1, 30)
# print('Какой ID ищем?', worker_ID_find)
#
# result = 0
# for id in workers_ID:
#     if worker_ID_find == id:
#         result = 1
#
# if result == 1:
#     print('Сотрудник на месте')
# else:
#     print('Сотрудник не работает!')

# 15.2 Индексы. Работа с элементами списка

# Задача 1. Гугл

# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# maximum = 0
#
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#
# minimum = maximum
#
# for i in nums_list:
#     if minimum >= i:
#         minimum = i
#
#
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)

# Задача 2. Кратность

# nums_count = randint(3, 10)
# print('Кол-во чисел в списке:', nums_count)
# numbers = []
# numbers_indexes_sum = 0
#
# for i in range(1, nums_count + 1):
#     number = randint(1, 10000)
#     print('Число ' + str(i) + ': ', number)
#     numbers.append(number)
# print('')
#
# divisor = randint(2, 10)
# print('Делитель:', divisor)
# print('')
#
# for i_num in range(nums_count):
#     if numbers[i_num] % divisor == 0:
#         print('Индекс числа ' + str(numbers[i_num]) + ': ' +  str(i_num))
#         numbers_indexes_sum += i_num
#
# if numbers_indexes_sum > 0:
#     print('Сумма индексов:', numbers_indexes_sum)
# else:
#     print('Все эти числа не делятся без остатка на', divisor)

# Задача 3. Собачьи бега

# dogs_count = randint(5, 20)
# print('В бегах участвует собак:', dogs_count)
# dog_scores_list = []
#
# print('Очки:')
#
# for i in range(1, dogs_count + 1):
#     dog_scores = randint(1, 100)
#     print(str(i) + ' - ', dog_scores)
#     dog_scores_list.append(dog_scores)
#
# maximum = max(dog_scores_list)
# minimum = min(dog_scores_list)
#
# print('Максимальное количество очков:', maximum)
# print('Минимальное количество очков:', minimum)
# print('')
#
# difference = maximum - minimum
#
# for i in range(dogs_count):
#     if dog_scores_list[i] == maximum:
#         dog_scores_list[i] -= difference
#     elif dog_scores_list[i] == minimum:
#         dog_scores_list[i] += difference
#
# print('Исправленное распределение очков:')
# for i in range(1, dogs_count + 1):
#     print(str(i) + ' - ', dog_scores_list[i - 1])

# 15.3 Списки: работа со строками

# Задача 1. Текстовый редактор: возвращение

# text = input('Введите строку: ')
#
# text_list = list(text)
# replacements_indexes = []
# sym_count = -1
# replacements_count = 0
#
# for sym in text_list:
#     sym_count += 1
#     if sym == ':':
#         replacements_indexes.append(sym_count)
#         replacements_count += 1
# # print(replacements_indexes)
#
# print('Исправленная строка: ', end='')
#
# for i in replacements_indexes:
#     text_list[i] = ';'
#
# for sym in text_list:
#     print(sym, end='')
#
# print('\nКоличество замен:', replacements_count)

# Задача 2. Соседи

# text = input('Введите строку: ')
# sym_number = int(input('Номер символа: '))
#
# text_list = list(text)
#
# left_sym = text_list[sym_number - 2]
# right_sym = text_list[sym_number]
# find_sym = text_list[sym_number - 1]
#
# print('Символ слева:', left_sym)
# print('Символ справа:', right_sym)
#
# if (left_sym == find_sym and right_sym != find_sym) or (right_sym == find_sym and left_sym != find_sym):
#     print('Есть ровно один такой же символ')
# elif left_sym == find_sym and right_sym == find_sym:
#     print('Есть два таких же символа')
# else:
#     print('Таких же символов нет')

# Задача 3. Улучшенная лингвистика

words_to_find_list = []
words_count = [0, 0, 0]

for i in range(1, 4):
    word = input('Введите ' + str(i) + '-е слово: ')
    words_to_find_list.append(word)

print('Введите текст по словам:')
text = input('Слово из текста: ')
while text != 'end':
    for i in range(3):
        if text == words_to_find_list[i]:
            words_count[i] += 1
    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте:')
for i in range(3):
    print(words_to_find_list[i] + ': ' + str(words_count[i]))


