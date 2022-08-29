# number = int(input('Введите число: '))
# summ = 0
# while number != 0:
#     summ += number
#     number = int(input('Введите число: '))
# print(summ)

# password = int(input('Введите пароль: '))
# while password != 235:
#     print('Неверный пароль!')
#     password = int(input('Попробуйте ещё раз: '))
# print('Пароль верный! Добро пожаловать.')

# summ = int(input('Сколько отложить денег? '))
# bank = 0 + summ
# while bank < 500000:
#     summ = int(input('Сколько отложить денег? '))
#     bank += summ
# print('Ура! Идём покупать машину.')

# t = int(input('Сколько градусов на улице? '))
# meters = 0
# while t > 15:
#     meters += 20
#     t -= 2
#     if t <= 15:
#          break
#     meters += 10
# print('Пройдено', meters, 'метра(ов)')

# bank = int(input('Введите стартовую сумму: '))
# while bank < 10000:
#     number = int(input('Сколько выпало на кубике? '))
#     if number != 3:
#         bank += 500
#         print('Выиграли 500 рублей!')
#     else:
#         print('Вы проиграли всё!')
#         break
# print('Игра закончена.')
# print('Итого осталось:', bank, 'рублей')

number = int(input('Введите число: '))
summ = 0
while number != 0:
    last_number = number % 10
    print(last_number)
    if last_number == 5:
        print('Обнаружен разрыв')
        break
    summ += last_number
    number //= 10
print('Сумма: ', summ)


