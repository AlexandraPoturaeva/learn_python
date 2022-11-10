import random
from random import randint
from my_modules import helper

# 6.1 Словарь: основы
# Задача 1. Словарь квадратов чисел

# numbers_and_squares_dict = dict()
#
# max_number = randint(5, 30)
# print('Число:', max_number)
#
# for num in range(1, max_number + 1):
#     numbers_and_squares_dict[num] = num ** 2
#
# print('Результат:', numbers_and_squares_dict)

# Задача 2. Студент

# student_info_str = 'Илья Иванов Москва МГУ 5 4 4 4 5'
# info_template = ['Имя', 'Фамилия', 'Город', 'Вуз']
# student_info_lst = student_info_str.split()
# student_info_dict = dict()
#
# for num in range(0, 4):
#     student_info_dict[info_template[num]] = student_info_lst[num]
# student_info_dict['Оценки'] = []
#
# for i_grade in student_info_lst[4::]:
#     student_info_dict['Оценки'].append(int(i_grade))
#
# for i_cat in student_info_dict:
#     print(i_cat, '-', student_info_dict[i_cat])

# Задача 3. Контакты

# name_list = helper.make_random_text_list('names', 25)
# name_list.append('end')
# name = random.choice(name_list)
# phone_book = dict()
#
# while name != 'end':
#     phone_number = '+7 ({code}) {fig1}-{fig2}-{fig3}'.format(
#         code=randint(900, 999),
#         fig1=randint(100, 999),
#         fig2=randint(10, 99),
#         fig3=randint(10, 99)
#     )
#     print('Введите имя:', name)
#     if name in phone_book:
#         print('Ошибка: такое имя уже существует.\n')
#     else:
#         print('Введите номер телефона:', phone_number)
#         phone_book[name] = phone_number
#         print('\nТекущие контакты на телефоне:')
#         for i in phone_book:
#             print(i, phone_book[i])
#         print('\n')
#     name = random.choice(name_list)
