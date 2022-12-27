import pickle
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

# 6.6 Практическая работа
# Задача 1. Песни 2

# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# }
#
# songs_list = list(violator_songs.keys())
# duration = 0
#
# while True:
#     songs_list_copy = songs_list.copy()
#     song_num = randint(0, len(songs_list))
#     print('Сколько песен выбрать? (0 - выход)', song_num)
#     if song_num == 0:
#         break
#     else:
#         for i in range(song_num):
#             song = random.choice(songs_list_copy)
#             songs_list_copy.remove(song)
#             print(f'Название {i + 1}-й песни: {song}')
#             duration += violator_songs[song]
#         print('Общее время звучания песен: {:.2f}'.format(duration), 'минуты.')
#         duration = 0

# Задача 2. География

# with open('./data/text_lists/countries', 'rb') as f:
#     countries_id = pickle.load(f)
#
# with open('./data/text_lists/cities', 'rb') as f:
#     cities_country_id = pickle.load(f)
#
# country_num = randint(0, 5)
#
# while country_num != 0:
#     user_dict = {}
#     print('Количество стран:', country_num)
#     user_cities_list = []
#     for i in range(country_num):   #гененируем пользовательский текст (страны и города, которые в этой стране находятся)
#         text = ''
#         country = random.choice(list(countries_id.keys()))
#         cities = [key for key in cities_country_id if cities_country_id[key] == countries_id[country]]
#         text += country
#         if len(cities) >= 3:
#             cities_num = 3
#         else:
#             cities_num = len(cities)
#         for _ in range(cities_num):
#             city = random.choice(cities)
#             text += ' ' + city
#             cities.remove(city)
#         print(f'{i+1}-я страна: {text}')
#         text_list = text.split(' ')
#         user_cities_list.extend(text_list[1::])
#         user_dict[text_list[0]] = text_list[1::]
#     for i in range(3):
#         city = random.choice(user_cities_list)
#         for key, value in user_dict.items():
#             if city in value:
#                 city_country = key
#         print(f'{i+1}-й город: {city}'
#               f'\nГород {city} расположен в стране {city_country}')
#     country_num = randint(0, 5)

# Задача 3. Криптовалюта

# data = {
#     "address": "0x544444444444",
#     "ETH": {
#         "balance": 444,
#         "totalIn": 444,
#         "totalOut": 4
#     },
#     "count_txs": 2,
#     "tokens": [
#         {
#             "fst_token_info": {
#                 "address": "0x44444",
#                 "name": "fdf",
#                 "decimals": 0,
#                 "symbol": "dsfdsf",
#                 "total_supply": "3228562189",
#                 "owner": "0x44444",
#                 "last_updated": 1519022607901,
#                 "issuances_count": 0,
#                 "holders_count": 137528,
#                 "price": False
#             },
#             "balance": 5000,
#             "totalIn": 0,
#             "total_out": 0
#         },
#         {
#             "sec_token_info": {
#                 "address": "0x44444",
#                 "name": "ggg",
#                 "decimals": "2",
#                 "symbol": "fff",
#                 "total_supply": "250000000000",
#                 "owner": "0x44444",
#                 "last_updated": 1520452201,
#                 "issuances_count": 0,
#                 "holders_count": 20707,
#                 "price": False
#             },
#             "balance": 500,
#             "totalIn": 0,
#             "total_out": 0
#         }
#     ]
# }
#
# print(data.keys())
# print(data.values())
#
# data['ETH']['total_diff'] = 100
#
# data['tokens'][0]['fst_token_info'].update({'name': 'doge'})
#
# data['ETH'].update({'totalOut': data['tokens'][0].pop('total_out')})
#
# data['tokens'][1]['sec_token_info']['total_price'] = data['tokens'][1]['sec_token_info'].pop('price')

# Задача 4. Товары

# goods = {
#     'Лампа': '12345',
#     'Стол': '23456',
#     'Диван': '34567',
#     'Стул': '45678',
# }
#
#
# store = {
#     '12345': [
#         {'quantity': 27, 'price': 42},
#     ],
#     '23456': [
#         {'quantity': 22, 'price': 510},
#         {'quantity': 32, 'price': 520},
#     ],
#     '34567': [
#         {'quantity': 2, 'price': 1200},
#         {'quantity': 1, 'price': 1150},
#     ],
#     '45678': [
#         {'quantity': 50, 'price': 100},
#         {'quantity': 12, 'price': 95},
#         {'quantity': 43, 'price': 97},
#     ],
# }
#
# for good in list(goods.keys()):
#     count = sum([store[goods[good]][n]['quantity']
#                  for n in range(len(store[goods[good]]))])
#     total_price = sum([store[goods[good]][n]['quantity'] * store[goods[good]][n]['price']
#                        for n in range(len(store[goods[good]]))])
#     print(f'{good} - {count} штук, стоимость {total_price} руб.')

# Задача 5. Гистограмма частоты 2

# text = ' '.join(helper.make_random_text_list('words', 20))
# print('Текст:', text)
# hist = histogram(text)
#
# print('Оригинальный словарь частот:')
# for i_sym in sorted(hist.keys()):
#     print(i_sym, ':', hist[i_sym])
#
#
# freq_set = set(hist.values())
# hist_invert = {freq: [key for key in hist.keys() if hist[key] == freq] for freq in freq_set}
#
# print('\nИнвертированный словарь частот:')
# for freq in sorted(hist_invert.keys()):
#     print(freq, ':', hist_invert[freq])

# Задача 6. Словарь синонимов

# with open('./data/text_lists/synonims', 'rb') as f:
#     synonyms_pairs_list = pickle.load(f)
#
# print(synonyms_pairs_list)
#
# word_list = [pair[:pair.index(' ')].lower() for pair in synonyms_pairs_list]
# print(word_list)
#
# answer = 1
# user_syn_dict = dict()
#
# while answer == 1:
#     n = randint(10, 30)
#     print('Количество пар слов:', n)
#     for i in range(1, n + 1):
#         pair = random.choice(synonyms_pairs_list).lower()
#         print(f'{i}-я пара: {pair}')
#         pair_list = pair.split(' — ')
#         user_syn_dict[pair_list[0]] = pair_list[1]
#     while True:
#         user_word = random.choice(word_list)
#         print('Слово:', user_word)
#         if user_word in user_syn_dict.keys():
#             print('Синоним:', user_syn_dict[user_word])
#             break
#         else:
#             print('Такого слова нет в словаре.')
#     answer = randint(1, 2)

# Задача 7. Пицца

# with open('./data/text_lists/names', 'rb') as f:
#     names = pickle.load(f)
#
# with open('./data/text_lists/russian_dishes', 'rb') as f:
#     dishes = pickle.load(f)
#
# client_names = [random.choice(names) for _ in range(10)] # генерируем списки имён клиентов и ассортимент блюд кафе
# cafe_dishes = [random.choice(dishes) for _ in range(5)]
#
# order_num = randint(5, 15) # генерируем число заказов
# order_text = ''
# order_client_dict = dict()
#
# print('Количество заказов:', order_num)
#
# for i in range(1, order_num + 1):
#     name = random.choice(client_names) # генерируем текстовую строку заказа (order_text)
#     dish = random.choice(cafe_dishes)
#     dish_num = str(randint(1, 5))
#     order_text = name + ' ' + dish + ' ' + dish_num
#     print(f'{i}-й заказ: {order_text}')
#
#     i_name = order_text[:order_text.index(' '):] # вычленяем из текстовой строки заказа ключи и значения для словаря
#     i_dish = order_text[order_text.index(' ')+1:-2]
#     i_dish_num = int(order_text[-1])
#
#     if i_name in order_client_dict.keys(): # составляем словарь заказов
#         if i_dish in order_client_dict[i_name].keys():
#             order_client_dict[i_name][i_dish] += i_dish_num
#         else:
#             order_client_dict[i_name].update({i_dish: i_dish_num})
#     else:
#         order_client_dict[i_name] = dict()
#         order_client_dict[i_name][i_dish] = i_dish_num #order_dict.copy()
#
# for key, value in order_client_dict.items():
#     print('\n' + key + ':')
#     for dish in value.keys():
#         print(f'   {dish}: {value[dish]}')

# Задача 8. Угадай число

# max_num = randint(5, 30)
# hidden_num = randint(1, max_num)
#
# possible_nums_set = {num for num in range(1, max_num + 1)}
# yes_nums_set = possible_nums_set
#
# print('Максимальное число:', max_num,
#       '\nЗагаданное число:', hidden_num)
#
# commands = ['Попробуем ещё раз', 'Попробуем ещё раз', 'Попробуем ещё раз', 'Помогите!']
# command = 'Попробуем ещё раз!'
#
# while True:
#     match command:
#         case 'Попробуем ещё раз':
#             stop_num = randint(1, len(possible_nums_set))
#             start_num = stop_num - randint(1, stop_num)
#             step = randint(1, 3)
#             guess_set = {num for num in list(possible_nums_set)[start_num:stop_num:step]}
#             print('Нужное число есть среди этих чисел?', *sorted(guess_set))
#             if hidden_num in guess_set:
#                 print('Да')
#                 yes_nums_set.intersection_update(guess_set)
#                 if len(guess_set) == 1:
#                     print('Число отгадано!')
#                     break
#             else:
#                 print('Нет')
#                 possible_nums_set.difference_update(guess_set)
#         case 'Помогите!':
#             print(command)
#             print('Артём мог загадать следующие числа:', *possible_nums_set.intersection(yes_nums_set))
#             break
#     command = random.choice(commands)

# Задача 9. Родословная

# pairs = ['Alexei Peter_I', 'Anna Peter_I', 'Elizabeth Peter_I', 'Peter_II Alexei', 'Peter_III Anna',
#          'Paul_I Peter_III', 'Alexander_I Paul_I', 'Nicholaus_I Paul_I']
#
# pers_high_dict = dict()
# gen_tree = dict()
# # gen_tree = dict()
#
# for i in range(1, len(pairs) + 1):
#     print(f'{i}-я пара: {pairs[i - 1]}')
#     pair_list = pairs[i - 1].split()
#     if pair_list[1] not in gen_tree.keys():
#         gen_tree[pair_list[1]] = set()
#     gen_tree[pair_list[1]].add(pair_list[0])
#
# print(gen_tree)
#
# children = set().union(*gen_tree.values())
#
# for key in gen_tree.keys():
#     if key not in children:
#         parent = key
#         pers_high_dict[key] = 0
#
# heigh = 1
#
#
# def get_heigh(parent, heigh):
#     if parent in gen_tree.keys():
#         for child in gen_tree[parent]:
#             pers_high_dict.update({child: heigh})
#             get_heigh(child, heigh + 1)
#
#
# get_heigh(parent, heigh)
#
# for key, value in sorted(pers_high_dict.items()):
#     print(key, value)

# Задача 10. Снова палиндром

word = 'aacddd'  # helper.make_random_letters_sequence()
print('Слово:', word)


def is_palindrome(word):
    hist_dict = dict()
    for i_sym in word:
        hist_dict[i_sym] = hist_dict.get(i_sym, 0) + 1
    odd = 0
    for value in hist_dict.values():
        if value % 2 != 0:
            odd += 1
            if odd > 1:
                return 'Нельзя сделать палиндромом'
    if odd <= 1:
        return 'Можно сделать палиндромом'


print(is_palindrome(word))

