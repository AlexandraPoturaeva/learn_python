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

workers_count = randint(10, 30)
print('Кол-во сотрудников в офисе:', workers_count)

workers_ID = []

for num in range(1, workers_count + 1):
    id = randint(1, 30)
    print(str(num) + ') ID сотрудника: ' + str(id))
    workers_ID.append(id)

worker_ID_find = randint(1, 30)
print('Какой ID ищем?', worker_ID_find)

result = 0
for id in workers_ID:
    if worker_ID_find == id:
        result = 1

if result == 1:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')