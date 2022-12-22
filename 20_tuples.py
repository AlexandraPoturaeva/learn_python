import math
import pickle
import random
from my_modules import helper
import math

# 7.2 Кортежи
# Задача 1. Создание кортежей


# def create_random_tuple(start, stop, count):
#     return tuple([random.randint(start, stop) for _ in range(count)])
#
#
# first_tuple = create_random_tuple(0, 5, 10)
# second_tuple = create_random_tuple(-5, 0, 10)
# third_tuple = first_tuple + second_tuple
#
# print(third_tuple)
# print('Количество нулей:', third_tuple.count(0))

# Задача 2. Цилиндр

# r = random.randint(1, 100)
# h = random.randint(1, 100)
#
# print('Радиус:', r,
#       '\nВысота:', h)
#
#
# def cylinder_sq():
#     side = 2 * math.pi * r * h
#     full = side + 2 * math.pi * (r ** 2)
#     return side, full
#
#
# answer = cylinder_sq()
#
# print('Площадь боковой поверхности:', answer[0],
#       '\nПолная площадь:', answer[1])

# Задача 3. Неправильный код
#
# import random
#
#
# def change(nums):
#     index = random.randint(0, 5)
#     value = random.randint(100, 1000)
#     nums = list(nums)
#     nums[index] = value
#     return tuple(nums), value
#
#
# my_nums = 1, 2, 3, 4, 5
#
# new_nums, rand_val = change(my_nums)
#
# print(new_nums, rand_val)
#
# new_nums = change(new_nums)[0]
#
# rand_val += change(new_nums)[1]
#
# print(new_nums, rand_val)

# 7.3 Функция enumerate. Перебор нескольких значений
# Задача 1. Саботаж!

# string = 'so~mec~od~e'
#
#
# def find_sym(string, sym):
#     return [index for index, letter in enumerate(string) if letter == sym]
#
#
# print(*find_sym(string, '~'))

# Задача 2. Словари из списков

# def create_random_letter_list(count):
#     # return [chr(random.randint(1072, 1103)) for _ in range(count)]
#     return random.choices([chr(i) for i in range(ord("а"), ord("я"))], k=count)
#
#
# first_list = create_random_letter_list(10)
# second_list = create_random_letter_list(10)
#
# first_dict = dict(enumerate(first_list))
# second_dict = dict(enumerate(second_list))
#
# print('Первый список:', first_list,
#       '\nВторой список:', second_list,
#       '\n\nПервый словарь:', first_dict,
#       '\nВторой словарь:', second_dict)

# Задача 3. Универсальная программа

# data_for_random = ['О Дивный Новый мир!',
#              [100, 200, 300, 'буква', 0, 2, 'а'],
#              (5, 7, 8, 'а', 's', 6, 9),
#              {0: 'е', 1: 'о', 2: 'ж', 3: 'й', 4: 'н', 5: 'ф', 6: 'с', 7: 'ъ', 8: 'б', 9: 'т'}]
#
# answer = 9
#
# while answer != 1:
#     user_data = random.choice(data_for_random)
#     print('Данные:', user_data)
#     if isinstance(user_data, dict):
#         user_data = user_data.items()
#     result = [value for index, value in enumerate(user_data) if index % 2 == 0]
#     print('Результат:', result)
#     answer = random.choice(range(0, 9))

# 7.4 Перебор ключей и значений в словаре. Метод items
# Задача 1. Кризис миновал

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
# for key, value in incomes.items():
#     print(key, '--', value)

# Задача 2. Сервер

# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
#
# for key, value in server_data.items():
#     print(key + ':')
#     for i_key, i_value in value.items():
#         print(f'  {i_key}: {i_value}')

# Задача 3. В одну строчку

# print([value for key, value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if key % 2 == 0])

# 7.5 Составные ключи
# Задача 1. Паспортные данные

# data = {
#     (5000, 123456): ('Иванов', 'Василий'),
#     (6000, 111111): ('Иванов', 'Петр'),
#     (7000, 222222): ('Медведев', 'Алексей'),
#     (8000, 333333): ('Алексеев', 'Георгий'),
#     (9000, 444444): ('Георгиева', 'Мария')
# }
#
# variants = [(5000, 123456), (6000, 111111), (7000, 222222), (8000, 333333), (9000, 444444)]
#
# key = random.choice(variants)
# print(key, *data[key], )

# Задача 2. Контакты 2

# with open('C:/code/Skillbox/data/text_lists/names_male', 'rb') as f:
#     names = pickle.load(f)
#
# with open('C:/code/Skillbox/data/text_lists/russian_surnames', 'rb') as f:
#     surnames = pickle.load(f)
#
# contacts = dict()
# answer = 9
#
#
# while answer != 1:
#     name = random.choice(names)
#     surname = random.choice(surnames)
#     phone_number = int('89' + str(random.randint(0, 9)) + str(random.randint(10000000, 99999999)))
#     print(f'Имя: {name} \nФамилия: {surname} \nНомер телефона: {phone_number}\n')
#     if (name, surname) in contacts.keys():
#         print('Человек с таким именем и фамилией уже есть в списке контактов')
#     else:
#         contacts[(name, surname)] = phone_number
#     answer = random.choice(range(0, 10))
#
# for key, value in contacts.items():
#     print(key[0], key[1], '-', value)

# 7.8 Практическая работа
# Задача 1. Ревью кода

# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
#
#
# def f(dict):
#     interests = {i for value in dict.values() for i in value['interests']}
#     total_surname_length = sum([len(i) for value in dict.values() for i in value['surname']])
#     return interests, total_surname_length
#
#
# id_age = [(key, value['age']) for key, value in students.items()]
#
# print('Список пар "ID студента — возраст":', id_age,
#       '\nПолный список интересов всех студентов:', f(students)[0],
#       '\nОбщая длина всех фамилий студентов:', f(students)[1])

# Задача 2. Универсальная программа 2

# data_for_random = ['О Дивный Новый мир!',
#              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#              (5, 7, 8, 'а', 's', 6, 9),
#              {0: 'е', 1: 'о', 2: 'ж', 3: 'й', 4: 'н', 5: 'ф', 6: 'с', 7: 'ъ', 8: 'б', 9: 'т'}]
#
# answer = 9
#
#
# def is_prime(num):
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if (num % i) == 0:
#             return False
#     return True
#
#
# def dict_to_list(data):
#     if isinstance(data, dict):
#         data = data.items()
#     return data
#
#
# def return_prime_ind(data):
#     return [elem for index, elem in enumerate(dict_to_list(data)) if index not in [0, 1] and is_prime(index)]
#
#
# while answer != 1:
#     user_data = random.choice(data_for_random)
#     print('Данные:', user_data)
#     print('Результат:', return_prime_ind(user_data))
#     answer = random.choice(range(0, 9))

# Задача 3. Функция

# random_tuple = tuple([random.randint(0, 9) for _ in range(random.randint(5, 20))])
# random_num = random.randint(0, 9)
#
# print('Input:', random_tuple, random_num)
#
#
# def slicer(u_tuple, u_num):
#     if u_num in u_tuple:
#         indexes = [i for i, elem in enumerate(u_tuple) if elem == u_num][0:1]
#         start = indexes[0]
#         if len(indexes) >= 2:
#             stop = indexes[1]
#         else:
#             stop = len(u_tuple)
#         return u_tuple[start:stop + 1]
#     else:
#         return tuple()
#
#
# print(slicer(random_tuple, random_num))

# Задача 4. Игроки

# players = {
#     ("Ivan", "Volkin"): (10, 5, 13),
#     ("Bob", "Robbin"): (7, 5, 14),
#     ("Rob", "Bobbin"): (12, 8, 2)
# }
#
# result = [key + value for key, value in players.items()]
# print(result)

# Задача 5. Одна семья

# with open('C:/code/Skillbox/data/text_lists/russian_surnames', 'rb') as f:
#     all_surnames = pickle.load(f)
#
# with open('C:/code/Skillbox/data/text_lists/names_female', 'rb') as f:
#     female_names = pickle.load(f)
#
# with open('C:/code/Skillbox/data/text_lists/names_male', 'rb') as f:
#     male_names = pickle.load(f)
#
# surnames_for_random = [surname for surname in all_surnames if 'ий' not in surname][:40]
#
# family_dict = dict()
#
# for _ in range(100):
#     female = (random.choice(surnames_for_random) + 'а', random.choice(female_names))
#     male = (random.choice(surnames_for_random), random.choice(male_names))
#     age_female = random.randint(0, 100)
#     age_male = random.randint(0, 100)
#     family_dict[female] = age_female
#     family_dict[male] = age_male
#
# print(family_dict)
# family_surnames = [key[0] for key in family_dict.keys()]
# print(family_surnames)
#
# for surname in surnames_for_random:
#     print('Фамилия:', surname)
#     if (surname or (surname + 'а')) in family_surnames:
#         for key, value in family_dict.items():
#             if surname in key[0]:
#                 print(key[0], key[1], value)
#     else:
#         print('Нет данных')
#     print('')

# Задача 6. По парам

# random_list = [random.randint(0, 9) for _ in range(10)]
# print(random_list)
#
# print(list(zip(random_list[0::2], random_list[1::2])))
#
# result = [(random_list[i], random_list[i+1]) for i in range(0, len(random_list), 2)]
# print(result)

# Задача 7. Функция сортировки

# decimal_num = random.uniform(-10, 10)
#
# data_list = tuple([random.randint(-10, 10) for _ in range(random.randint(10, 20))])
#
# answer = random.randint(0, 100)
# if answer % 2 == 0:
#     data = data_list + (decimal_num,)
# else:
#     data = data_list
#
#
# def tpl_sort(tuple):
#     if all(isinstance(number, int) for number in tuple):
#         return sorted(tuple)
#     else:
#         return tuple
#
#
# print(tpl_sort(data))

# Задача 8. Контакты 3

# with open('C:/code/Skillbox/data/text_lists/names_male', 'rb') as f:
#     names = pickle.load(f)
#
# with open('C:/code/Skillbox/data/text_lists/russian_surnames', 'rb') as f:
#     surnames = pickle.load(f)
#
# contacts = dict()
# contacts_surnames = []
# answer = 9
# command = 1
#
#
# def find_contact(surname):
#     result = tuple()
#     for key, value in contacts.items():
#         if surname in key:
#             result += (key[0], key[1], value)
#     if len(result) == 0:
#         return 'Человека с такой фамилией нет в списке контактов'
#     else:
#         return result
#
#
# while answer != 1:
#     print('Введите номер действия (1 - добавить контакт,  2 - найти человека):', command)
#     match command:
#         case 1:
#             name = random.choice(names)
#             surname = random.choice(surnames)
#             phone_number = int('89' + str(random.randint(0, 9)) + str(random.randint(10000000, 99999999)))
#             print(f'Имя: {name} \nФамилия: {surname} \nНомер телефона: {phone_number}\n')
#             if (name, surname) in contacts.keys():
#                 print('Человек с таким именем и фамилией уже есть в списке контактов')
#             else:
#                 contacts[(name, surname)] = phone_number
#                 contacts_surnames.append(surname)
#         case 2:
#             surname = random.choice(contacts_surnames)
#             print('Введите фамилию для поиска:', surname)
#             print(find_contact(surname))
#     for key, value in contacts.items():
#         print(key[0], key[1], '-', value)
#     answer = random.choice(range(0, 30))
#     command = random.choice([1, 2])

# Задача 9. Протокол соревнований

# with open('C:/code/Skillbox/data/text_lists/names', 'rb') as f:
#     names = pickle.load(f)
#
# gamers = list({random.choice(names) for _ in range(random.randint(3, 10))})
# print(gamers)
#
# record_cnt = random.randint(10, 25)
# protocol_dict = dict()
#
# for i in range(1, record_cnt + 1):
#     gamer = random.choice(gamers)
#     score = random.randrange(70000, 80000, 2000)
#     print(f'{i}-запись: {score} {gamer}')
#     if gamer not in protocol_dict.keys() or score > protocol_dict[gamer][0]:
#         protocol_dict[gamer] = (score, i)
#
# print(protocol_dict)
#
# print('Итоги соревнований:')
# for i in range(1, 4):
#     max_score = max([value[0] for value in protocol_dict.values()])
#     min_time = min([value[1] for value in protocol_dict.values() if value[0] == max_score])
#     for key, value in protocol_dict.items():
#         if value == (max_score, min_time):
#             print(f'{i}-место: {key} ({value[0]})')
#             protocol_dict.pop(key)
#             break


# Задача 10. Своя функция zip

# user_string = 'abcd'
# user_tuple = (10, 20, 30, 40)
#
#
# def shortest_seq_range(string, tpl):
#     return min(len(string), len(tpl))
#
#
# pairs = ((user_string[i], user_tuple[i])
#           for i in range(shortest_seq_range(user_string, user_tuple)))
#
# print(pairs)
# print(*pairs)









