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
# student_info_dict['Оценки'] = [int(grade) for grade in student_info_lst[4::]]
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

# 6.2 Методы словарей
# Задача 1. Склады

# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# big_storage.update(small_storage)
#
# items_list = [key for key in big_storage]
# items_list.extend(['гайки', 'брусья', 'шайбы', 'уголки', 'stop'])
# item = random.choice(items_list)
#
# while item != 'stop':
#     print('Наименование товара:', item, '\nКоличество:', big_storage.get(item))
#     item = random.choice(items_list)

# Задача 2. Кризис фруктов

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}


# Мой вариант
# fruit_min_income = list(incomes.keys())[list(incomes.values()).index(min(list(incomes.values())))]
#
# print('Общий доход за год составил:', sum(incomes.values()),
#       '\nСамый маленький доход у', fruit_min_income,
#       '\nОн составляет:', incomes.pop(fruit_min_income), 'рублей'
#       )

# Вариант из решебника

# def get_value(x):
#     return x[1]
#
#
# result_sum = sum(incomes.values())
# min_name, min_value = min(incomes.items(), key=get_value)
#
# print('Общий доход за год составил:', result_sum,
#       '\nСамый маленький доход у', min_name,
#       '\nОн составляет:', min_value, 'рублей'
#       )
#
# incomes.pop(min_name)
#
# print('Итоговый словарь:', incomes)

# Задача 3. Гистограмма частоты

# def histogram(text):
#     sym_dict = dict()
#     for sym in text:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] = 1
#     return sym_dict
#
#
# text = ' '.join(helper.make_random_text_list('words', 20))
# print('Текст:', text)
# hist = histogram(text)
#
# for i_sym in sorted(hist.keys()):
#     print(i_sym, ':', hist[i_sym])
# print('Максимальная частота:', max(hist.values()))
