# number = int(input('Введите число: '))
# counter = 1
# while counter <= number:
#     print(str(counter) + '^3 = '+ str(counter**3))
#     counter += 1

# name, debt = input('Введите Ваше имя: '), int(input('Введите сумму долга: '))
# print(name + ', ваша задолженность составляет ' + str(debt) + ' рублей.')
# while True:
#     payment = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
#     if payment >= debt:
#         print('Отлично, ' + name + '. Вы погасили долг. Спасибо!')
#         break
#     print('Маловато, '+ name + '. Давайте ещё раз.')

# number = int(input('Введите число: '))
# counter = 0
# while True:
#     number //= 10
#     counter += 1
#     if number == 0:
#         print('В числе', counter, 'цифр(ы)')
#         break


# while True:
#     ticket_number = int(input('Введите номер билета: '))
#     sum_1 = (ticket_number // 1000) % 10 + (ticket_number // 1000) % 10 % 10 + (ticket_number // 1000) % 10 % 10 % 10
#     sum_2 = (ticket_number % 1000) % 10 + (ticket_number % 1000) % 10 % 10 + (ticket_number % 1000) % 10 % 10 % 10
#     if sum_1 == sum_2:
#         print('Билет счастливый! :)')
#     else:
#         print('Билет несчастливый! :(')
#     print('Попробуйте ещё раз!')

# counter_pos = 0
# counter_neg = 0
# while True:
#     mark = int(input('Введите число: '))
#     if mark > 0:
#         counter_pos += 1
#     elif mark < 0:
#         counter_neg += 1
#     else:
#         print('Кол-во положительных оценок: ', counter_pos)
#         print('Кол-во отрицательных оценок: ', counter_neg)
#         break

# print('Начался 8-часовой рабочий день')
#
# hour_counter = 1
# task_counter = 0
# wife = False
#
# while hour_counter <= 8:
#     print(str(hour_counter) + '-й час')
#     tasks = int(input('Сколько задач решит Максим? '))
#     task_counter += tasks
#
#     wife_call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет) '))
#     if wife_call == 1:
#         wife = True
#
#     hour_counter += 1
#
#
# print('Рабочий день закончился. Всего выполнено задач:', task_counter)
#
# if wife == True:
#     print('Нужно зайти в магазин')

# deposit = float(input('Введите первоначальный размер вклада: '))
# percent = float(input('Введите процент по вкладу: '))
# wish_deposit = float(input('Введите итоговый размер вклада: '))
# year = 0
# while deposit < wish_deposit:
#     year += 1
#     deposit += deposit/100*percent//1
# print('Вклад достигнет', wish_deposit, 'через', year, 'года (лет).')

# attempts = 0
# while True:
#     son = int(input('Введите число: '))
#     attempts +=1
#     if son > 7:
#         print ('Число больше, чем нужно. Попробуйте ещё раз!')
#     elif son < 7:
#         print('Число меньше, чем нужно. Попробуйте ещё раз!')
#     else:
#         print('Вы угадали! Число попыток: ', attempts)
#         break


print('Загадайте число от 1 до 100')

x1 = 0
x2 = 100
answer = -1
attempts = 1

while answer != 1 and attempts <= 7:
    x = int(x1 + (x2 - x1) / 2)
    answer = int(input('Попытка № ' + str(attempts) + '. Это число равно, меньше или больше, чем число ' + str(
        x) + '? (1 - равно, 2 - больше, 3 - меньше) '))
    if answer == 2:
        x1 = x
    else:
        x2 = x
    attempts += 1

if answer == 1:
    print('Вы угадали. Число равно', x)
else:
    print('Вы где-то соврали')
