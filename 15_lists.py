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

dogs_count = randint(5, 20)
print('В бегах участвует собак:', dogs_count)
dog_scores_list = []

print('Очки:')

for i in range(1, dogs_count + 1):
    dog_scores = randint(1, 100)
    print(str(i) + ' - ', dog_scores)
    dog_scores_list.append(dog_scores)

maximum = max(dog_scores_list)
minimum = min(dog_scores_list)

print('Максимальное количество очков:', maximum)
print('Минимальное количество очков:', minimum)
print('')

difference = maximum - minimum

for i in range(dogs_count):
    if dog_scores_list[i] == maximum:
        dog_scores_list[i] -= difference
    elif dog_scores_list[i] == minimum:
        dog_scores_list[i] += difference

print('Исправленное распределение очков:')
for i in range(1, dogs_count + 1):
    print(str(i) + ' - ', dog_scores_list[i - 1])