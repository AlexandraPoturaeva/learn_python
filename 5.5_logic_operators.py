# skill = int(input('Введите количество опыта: '))
# if skill < 1000:
#     print('Ваш уровень: 1')
# elif skill < 2500:
#     print('Ваш уровень: 2')
# elif skill < 5000:
#     print('Ваш уровень: 3')
# else:
#     print('Ваш уровень: 4')

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
# if a > b and a > c:
#     print('Наибольшее число: ', a)
# elif b > c:
#     print('Наибольшее число: ', b)
# else:
#     print('Наибольшее число: ', c)

# x = int(input('Введите число X: '))
# if x > 0:
#     print('Y =', x-12)
# elif x == 0:
#     print('Y = 5')
# else:
#     print('Y =', x**2)

# place = int(input('Введите место в списке: '))
# exams = int(input('ВВведите количество баллов за экзамены: '))
# if place <= 10 and exams >= 290:
#     print('Поздравляем, вы поступили!')
#     print('Бонусом вам будет начисляться стипендия.')
# elif place <= 10:
#     print('Поздравляем, вы поступили!')
#     print('Но вам не хватило баллов для стипендии.')
# else:
#     print('К сожалению, вы не поступили.')

# rating = int(input('Что получил по математике? '))
# if rating <= 3:
#     print('Плохо. Марш учиться!')
# else:
#     print('Молодец! Можешь отдохнуть.')

# x = int(input('Введите число: '))
# if (x > 0 and (x // 10) >= 1 and (x // 10) < 10) or (x < 0 and (-x // 10) >= 1 and (-x // 10) < 10):
#     print('Вы ввели двузначное число')
# else:
#     print('Ошибка. Вы ввели не двузначное число')

# x = abs(int(input('Введите число: ')))
# if (x // 10) >= 1 and (x // 10) < 10:
#     print('Вы ввели двузначное число')
# else:
#     print('Ошибка. Вы ввели не двузначное число')

import random

# a = random.randint(1, 9)
# b = random.randint(1, 9)
# c = random.randint(1, 9)
# print(a, b, c)
#
# if a == b and b == c:
#     print(3)
# elif a != b and b != c and a != c:
#     print(0)
# else:
#     print(2)

# square = int(input('Введите площадь: '))
# price = int(input('Введите стоимость: '))
# if (square >= 100 and price <= 10) or (square >= 80 and price <= 7):
#     print('Квартира подходит :)')
# else:
#     print('Квартира не подходит :(')

# profit = int(input('Введите доход: '))
# if profit < 0:
#     print('Ошибка. Доход не может быть отрицательным')
# elif profit < 10000:
#     print('Сумма налога (13%) составляет', profit * 0.13)
# elif profit < 50000:
#     tax = 1300 + (profit-10000)*0.2
#     print('Сумма налога составляет', tax)
# else:
#     tax = 9300 + (profit - 50000) * 0.3
#     print('Сумма налога составляет', tax)

# profit = int(input('Введите доход: '))
# if profit < 0:
#     print('Ошибка. Доход не может быть отрицательным')
# else:
#     if profit < 10000:
#         tax = profit * 0.13
#     elif profit < 50000:
#         tax = 1300 + (profit-10000)*0.2
#     else:
#         tax = 9300 + (profit - 50000) * 0.3
#     print('Сумма налога составляет', tax)

# t = random.randint(0, 23)
# print(t)
# if (t >= 8 and t < 10) or (t >= 12 and t < 14) or (t >= 15 and t < 18) or (t >= 20 and t < 22):
#     print('Можно получить посылку')
# else:
#     print('Посылку получить нельзя')

t = random.randint(0, 23)
print(t)
if not ((t >= 8 and t < 10) or (t >= 12 and t < 14) or (t >= 15 and t < 18) or (t >= 20 and t < 22)):
    print('Посылку получить нельзя')
else:
    print('Можно получить посылку')