import random
import string
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

def histogram(text):
    sym_dict = dict()
    for sym in text:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


#
#
# text = ' '.join(helper.make_random_text_list('words', 20))
# print('Текст:', text)
# hist = histogram(text)
#
# for i_sym in sorted(hist.keys()):
#     print(i_sym, ':', hist[i_sym])
# print('Максимальная частота:', max(hist.values()))

# 6.3 Вложенные словари и значения по умолчанию в get
# Задача 1. Член семьи

# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
#
# children_dict = dict()
# for child in family_member['children']:
#     children_dict[child['name']] = child['age']
#
#
# def search_child_name(name):
#     if children_dict.get(name, None):
#         return '{name} найден'.format(name=name)
#     else:
#         return '{name} не найден'.format(name=name)
#
#
# print(search_child_name('Bob'))
#
# children_surname = family_member.get("surname", None)
# if children_surname:
#     print(children_surname)
# else:
#     print("Nosurname")

# Задача 2. Игроки

# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
#
# def get_players_list(dict, team, status):
#     players_list = [
#         player['name']
#         for player in dict.values()
#         if player['team'] == team and
#            player['status'] == status
#     ]
#     return players_list
#
#
# request_dict = {
#     'A': ['Rest', 'отдыхают'],
#     'B': ['Training', 'тренируются'],
#     'C': ['Travel', 'путешествуют']
# }
#
# for key, value in request_dict.items():
#     answer = get_players_list(players_dict, key, value[0])
#     print('Всe члены команды {team}, которые {status}:'.format(team=key, status=value[1]), answer)

# 6.4 Множества. Функция set
# Задача 1. Пунктуация

# punctuation = {'.', ',', ';', ':', '!', '?'}
# words = [helper.make_random_letters_sequence() + random.choice(string.punctuation) for _ in range(randint(10, 20))]
# text = ' '.join(words)
# print('Текст:', text)
#
# text_punc = set(text) & punctuation # Нахожу пересечение набора знаков пунктуации и набора символов текста
# text_list = list(text)
#
# # Способ 1
# text_hist = histogram(text) # создаю словарь частоты символов в тексте
# text_punk_num = sum([text_hist[punc] for punc in text_punc]) # суммирую частоты употребления знаков препинания в тексте
#
# # Способ 2
# text_punk_num_2 = sum([text_list.count(punc) for punc in text_punc]) # суммирую частоты употребления знаков препинания в тексте
#
# print('Количество знаков пунктуации:', text_punk_num)
# print('Количество знаков пунктуации:', text_punk_num_2)

# Задача 2. Семинар

# nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
# nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
#
# nums_1_set = set(nums_1)
# nums_2_set = set(nums_2)
#
# print('1-е множество:', nums_1_set,
#       '\n2-е множество:', nums_2_set)
#
# min_nums_1 = min(nums_1_set)
# min_nums_2 = min(nums_2_set)
#
# random_nums_1 = randint(100, 200)
# random_nums_2 = randint(100, 200)
#
# nums_1_set.discard(min_nums_1)
# nums_1_set.add(random_nums_1)
# nums_2_set.discard(min_nums_2)
# nums_2_set.add(random_nums_2)
#
# print('\n\nМинимальный элемент 1-го множества:', min_nums_1,
#       '\nМинимальный элемент 1-го множества:', min_nums_2,
#       '\n\nСлучайное число для 1-го множества:', random_nums_1,
#       '\nСлучайное число для 2-го множества:', random_nums_2,
#       '\n\nОбъединение множеств:', nums_1_set | nums_2_set,
#       '\nПересечение множеств:', nums_1_set & nums_2_set,
#       '\nЭлементы, входящие в nums_2, но не входящие в nums_1:', nums_2_set - nums_1_set)

# Задача 3. Различные цифры

# letters = [random.choice(string.ascii_letters) for _ in range(10)]
# digits = [str(randint(0, 9)) for _ in range(10)]
# letters.extend(digits)
# random.shuffle(letters)
# user_string = ''.join(letters)
#
# print('Строка:', user_string)
# string_set = set(user_string)
#
# # Способ 1
# only_digits = [sym for sym in string_set if sym.isdigit()]
# print(''.join(sorted(only_digits)))
#
# # Способ 2
# result = string_set & set("0123456789")
# print(''.join(sorted(result)))