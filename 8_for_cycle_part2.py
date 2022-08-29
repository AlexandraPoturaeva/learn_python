from random import randint

# 8.2 Алгоритмические задачи со счётными циклами

# Задача 1. Таблица кубов

number = randint(1, 100)
print('Берём число', number)

for i in range(1, number//2 + 1):
    i *= 2
    print(i, '^3 = ', i**3)

# Задача 2. Деление клетки

# observation_hours = randint(3, 24)
# print('Будем наблюдать', observation_hours, 'часов')
# cells = 1
#
# for hour in range(1, observation_hours//3 + 1):
#     hour *= 3
#     cells *= 2
#     print('Прошло часов: ', hour)
#     print('Клеток: ', cells)
#     print('Часов до конца эксперимента: ', observation_hours - hour)
#     print()

# Задача 3. Квадраты нечётных чисел

# number = randint(1, 100)
# print('Берём число', number)
#
# for i in range(1, (number // 2) + (number % 2) + 1):
#     i = (i * 2) - 1
#     print(str(i) + '^2 = ' + str(i ** 2))


# 8.3 Функция range: start, stop, step

# Задача 1. Степень нечётного числа

# number = randint(1, 100)
# print('Берём число', number)
#
# for i in range(1, number + 1, 2):
#     print(str(i) + '^3 = ' + str(i**3))

# Задача 2. Театр

# number = randint(1, 100)
# print('Считаем до стула с номером', number)
# summ = 0
# for i in range(1, number + 1, 5):
#     print('Номер стула: ', i)
#     summ += i
# print('Сумма: ', summ)

# wake_up = randint(1, 22)
# print('Проснулся в ', wake_up, 'часов')
# water = 0
# calories_sum = 0
#
# for i in range(wake_up, 23, 3):
#     water += 1
#     calories = randint(100, 1500)
#     calories_sum += calories
#     print('Съедено калорий в ', i, 'часов: ', calories)
# print('Выпито литров воды: ', water)
# print('Всего седено калорий: ', calories_sum)


# 8.4 Отрицательный шаг в функции range

# Задача 1. Прятки

# seconds = randint(5, 50)
# for i in range(seconds, 0, -1):
#     print(i)
# print('Я иду искать!')

# Задача 2. Армия (с конца)

# total_soldiers = randint(2, 50)
# total_push_ups = 0
# print('Количество солдат в шеренге: ', total_soldiers)
#
# for i in range(total_soldiers, 0, -4):
#     print('Солдат №', i)
#     total_rules_officer = randint(100, 200)
#     print('Правил в уставе (офицер): ', total_rules_officer)
#     total_rules_soldier = randint(100, 200)
#     print('Солдат назвал число: ',  total_rules_soldier)
#
#     if total_rules_soldier != total_rules_officer:
#         total_push_ups += i*10
#         print('Неверно! ', i*10, 'отжиманий')
#
# print('Общее количество отжиманий: ', total_push_ups)

# Задача 2. Армия (с четвёртого с конца)

# total_soldiers = randint(10, 150)
# total_push_ups = 0
# print('Количество солдат в шеренге: ', total_soldiers)
#
# for i in range(total_soldiers - 4, 0, -4):
#     total_rules = randint(100, 105)
#     print('Правил в уставе (офицер): ', total_rules)
#     total_rules_soldier = randint(100, 105)
#     print('Солдат №', i, 'назвал число: ',  total_rules_soldier)
#     if total_rules_soldier != total_rules:
#         total_push_ups += i*10
#         print('Неверно! ', i*10, 'отжиманий')
# print('Общее количество отжиманий: ', total_push_ups)

# Задача 3. Прятки 2

# seconds = 11
# for i in range(seconds//2, 0, -1):
#     print(i*2)
# print(1)
# print('Я иду искать!')

# 8.6 Практическая работа

# Задача 1. Космическая еда

# months = 0
# for i in range(96, -1, -4):
#     months += 1
#     print('Через', months, 'месяц(ев) должно остаться гречки: ', i, 'кг')

# Задача 2. Долги

# debtors_number = randint(5, 50)
# print('Количество должников: ', debtors_number)
# debt_sum = 0
# for i in range(0, debtors_number, 5):
#     debt = randint(1000, 50000)
#     debt_sum += debt
#     print('Должник с номером', i, 'должен', debt)
# print('Общая сумма долга:', debt_sum)

# Задача 3. Таймер для микроволновых печей

# reverse_timer =  int(input('Время: '))
#
# for i in range(reverse_timer, 0, -1):
#     print(i)
#     # answer = randint(0, 1)
#     answer = int(input('Хотите забрать еду? '))
#     reverse_timer -= 1
#     if answer == 1:
#         print('Ваша еда готова, можете забрать. Осталось', reverse_timer, 'секунд(ы)')
#         break
# if reverse_timer == 0:
#     print('Ваша еда готова, осторожно горячo!')

# Задача 4. Среднее на отрезке

# a = randint(0, 150)
# b = randint(151, 300)
# c = randint(2, 50)
# print('Отрезок [', a, ',', b, '], кратность', c)
# summ = 0
# number_count = 0
#
# for number in range((a // c) * c + (a % c) + (c + (c * (a // c + 1)) - a) % c, b + 1, c):
#     print(number)
#     summ += number
#     number_count += 1
# print('Среднее арифметическое: ', summ / number_count)
#
# for number in range(a + (c - a % c) * round(a % c / (a % c + 0.1)), b + 1, c):
#     print(number)
#     summ += number
#     number_count += 1
# print('Среднее арифметическое: ', summ / number_count)

# Задача 5. Функция 2

# a = randint(-100, 0)
# b = randint(1, 100)
# c = randint(1, 10)
# print('Отрезок [', a, ',', b, '], шаг', c)
#
# for x in range(b, a-1, -c):
#     y = x ** 3 + 2 * x ** 2 - 4 * x + 1
#     print('В точке', x, 'функция равна', y)

# Задача 6. Письмо

# sheet_side = randint(13, 1000000)
# print('Размер листа: ', sheet_side, 'х', sheet_side)
# times = 0
# new_side = sheet_side
#
# for i in range(sheet_side, 0, -1):
#     new_side /= 2
#     times += 2
#     if new_side < 12:
#         print('Лист нужно сложить', times, 'раз(а)')
#         break

# Задача 7. Стипендия

# educational_grant = randint(10000, 100000)
# expenses_month = educational_grant + randint(1000, 20000)
# expenses_sum = expenses_month
#
# print('Ежемесячная стипендия:', educational_grant)
# print('Расходы на проживание:', expenses_month)
#
# for month in range(2, 11):
#     expenses_month = expenses_month + expenses_month / 100 * 3
#     expenses_sum += expenses_month
#     print('Расходы за', month, 'месяц:', round(expenses_month, 1))
#
# expenses_total = expenses_sum
# print('У родителей необходимо попросить:', round(expenses_total - (educational_grant * 10), 1))

# Задача 8. Сумма ряда

# n = randint(10, 100)
# print('n = ', n)
# s = 1 + ((-1) ** n) * (2 ** (-n))
#
# for i in range(1, n+1):
#     s += ((-1) ** i) * (2 ** (-i))
# print('s =', s)
#
# s = 0
# for i in range(0, n + 1):
#     s += ((-1) ** i) / 2 ** i
# print('s =', s)

# Задача 9. Выражение

# x = randint(1, 50)
# numenator = 1
# denominator = 1
#
# for i in range(1, 6):
#     numenator *= (x - 2 ** i - 1)
#     denominator *= (x - 2 ** i)
#
# print('res =', numenator / denominator)

# Задача 10. Кинотеатр

# x = randint(1, 10) # B
# y = randint(1, 10) # G
# x = 9
# y = 3
# print('Количество мальчиков:', x)
# print('Количество девочек:', y)
# text = ''
#
# if x / y > 2 or y / x > 2:
#     print('Нет решения')
# elif x == y:
#     for i in range(0, x):
#         text += 'BG'
# elif x >= y:
#     for i in range(0, x-y):
#         text += 'BGB'
#     for i in range(0, 2 * y - x):
#         text += 'BG'
# elif x <= y:
#     for i in range(0, y-x):
#         text += 'GBG'
#     for i in range(0, 2 * x - y):
#         text += 'GB'
# print(text)