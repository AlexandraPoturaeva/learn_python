# for meters in 100, 90, 95, 87, 102:
#     if meters % 3 == 0:
#         print(meters, 'Подходит')
#     else:
#         print(meters, 'Не подходит')

# for number in 3,7,5,6,4:
#     print(number**2, number**3, number**4)

# winners = 0
# for ticket in 345, 19, 87, 1020, 421, 333, 1200:
#     if 1 < ticket // 100 < 10 and ticket % 3 == 0:
#         print(ticket, ' - выигрышный билет')
#         winners += 1
# print('Количество победителей:', winners)

# for i in range(11):
#     print(i**2)

# current_hour = int(input('Который сейчас час? '))
# for hour in range(current_hour):
#     print('Ку-ку!')

# for number in range(20):
#     print(2 ** number)

# for number in range(1, 11):
#     print(number ** 3)

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# summ = 0
# for i in range(a, b + 1):
#     summ += i
# print('Сумма чисел от', a, 'до', b, 'равна', summ)

# hour_wakeup = int(input('Когда проснулся? '))
# callories_sum = 0
# awake_hours = 0

# for hour in range(hour_wakeup, 23):
#     print('Сейчас', hour, 'часов')
#     callories = int(input('Сколько съел? '))
#     callories_sum += callories
#     if callories_sum > 2000:
#         print('Поел - можно и поспать')
#         break
#     awake_hours += 1
# print('Съедено', callories_sum, 'калорий. Бодрствовал', awake_hours, 'часа(ов).')

# for number in 114, 12, 14, 10605, 4907, 450:
#     if number % 2 == 0 and number % 3 != 0:
#         print(number, 'подходит')
#     else:
#         print(number, 'не подходит')


# right_numbers = 0
# for number in range(1, 11):
#     meaning = int(input('Введите ' + str(number) + '-е число: '))
#     if meaning > 0 and meaning % 2 == 0:
#         right_numbers += 1
# print('Количество чётных и положительных: ', right_numbers)

# salary_sum = 0
# for month in range(1, 13):
#     salary = int(input('Введите зарплату за ' + str(month) + ' месяц: '))
#     salary_sum += salary
# print('Среднегодовая зарплата: ', salary_sum/12)

# excess_times = 0
#
# for sector in range(30, 36):
#     people_counter = int(input('Людей в ' + str(sector) + '-м секторе: '))
#     if people_counter > 10:
#         print('Нарушение! Слишком много людей в секторе!')
#         excess_times += 1
#     else:
#         print('Всё спокойно.')
#
# print('Количество нарушений: ', excess_times)

# number = int(input('Введите число: '))
# factorial = 1
# for n in range(2, number + 1):
#     factorial *= n
# print('Факториал числа', number, 'равен', factorial)

from random import randint

#
# students = int(input('Сколько человек в классе? '))
# mark3 = 0
# mark4 = 0
# mark5 = 0
#
# for student in range(1, students + 1):
#     mark = randint(3, 5)
#     print(str(student) +'-й получил оценку ' + str(mark))
#     if mark == 3:
#         mark3 += 1
#     elif mark == 4:
#         mark4 += 1
#     else:
#         mark5 += 1
#
# largest_group = max(mark3, mark4, mark5)
#
# if largest_group == mark3:
#     print('Сегодня больше троечников')
# elif largest_group == mark4:
#     print('Сегодня больше хорошистов')
# else:
#     print('Сегодня больше отличников')

# start_number = randint(0, 100)
# end_number = start_number + randint(100, 200)
# print('Отрезок: [' + str(start_number) + ', ' + str(end_number) + ']')
# summ = 0
# number_mult_3 = 0
#
# for number in range(start_number, end_number + 1):
#     if number % 3 == 0:
#         summ += number
#         number_mult_3 += 1
# print('Cреднее арифметическое всех чисел из отрезка [' +
#       str(start_number) + ',' + str(end_number) + '], кратных числу 3 равно: ' +
#       str(summ/number_mult_3))

# start_number = о
# end_number = start_number + randint(100, 200)
# print('Отрезок: [' + str(start_number) + ', ' + str(end_number) + ']')
# summ = 0
# number_mult_3 = 0
#
# for number in range(start_number, end_number + 1):
#     if number % 3 == 0:
#         summ += number
#         number_mult_3 += 1
# print('Метод 1. Cреднее арифметическое всех чисел из отрезка [' +
#       str(start_number) + ',' + str(end_number) + '], кратных числу 3 равно: ' +
#       str(summ/number_mult_3))
#
# remain_3 = start_number % 3
# if remain_3 == 0:
#     first = start_number
# else:
#     first = start_number - remain_3 + 3
#
# remain_3 = end_number % 3
# if remain_3 == 0:
#     last = end_number
# else:
#     last = end_number - remain_3
#
# print('Метод 2. Cреднее арифметическое всех чисел из отрезка [' +
#       str(start_number) + ',' + str(end_number) + '], кратных числу 3 равно: ' +
#       str((first+last)/2))

# for number in range(10, 100):
#     first_number = number // 10
#     second_number = number % 10
#     if number == (first_number*second_number*3):
#         print(number)

# previous_salary = 0
# decline_counter = 0
#
# for month in range(1, 11):
#     current_salary = randint(10000, 80000)
#     print('Заработная плата за ' + str(month) + '-й месяц составляет: ' + str(current_salary))
#     if current_salary <= previous_salary:
#         decline_counter +=1
#         print('↓')
#     else:
#         print('↑')
#     previous_salary = current_salary
#
# if decline_counter > 0:
#     print('Итог: заработная плата не увеличивается с каждым месяцем')
# else:
#     print('Итог: Заработная плата увеличивается с каждым месяцем')



# Метод 1
# cards_number = randint(3, 20)

# summ_all = sum(range(1, cards_number + 1))
#
# #for card in range(1, cards_number+1):
# #    summ_all += card
#
# for card in range(cards_number - 1):
#     number = int(input('Введите номер оставшейся карточки: '))
#     summ_all -= number
#
# print('Номер пропавшей карточки:', summ_all)

# Метод 2

cards_number = randint(3, 20)

print('Число карточек в игре: ', cards_number)
cards_set = list(range(1, cards_number + 1))
print(cards_set)
cards_left_number = cards_number

for i in range(1, cards_number):
    index = randint(0, cards_left_number - i)
    print('Вытащили карту: ', cards_set[index])
    del cards_set[index]
    print('Осталось проверить карт: ', cards_left_number - i)

print('Потерявшаяся карта:', cards_set[0])

