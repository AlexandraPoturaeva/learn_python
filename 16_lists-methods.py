import random
from random import randint


# 16.2 Работа со списками: методы insert, remove, index

# Задача 1. Зоопарк

# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
#
# print('Зоопарк:', zoo)
#
# zoo.insert(zoo.index('kangaroo'), 'bear')
#
# print('Завезли медведя:', zoo)
#
# zoo.remove('elephant')
#
# print('Увезли слона:', zoo)
#
# print('Лев сидит в клетке №', zoo.index('lion') + 1, '\nОбезьяна сидит в клетке №', zoo.index('monkey') + 1)

# Задача 2. Сокращения

# workers_count = randint(3, 20)
#
# print('Количество сотрудников:', workers_count)
#
# wages_list = []
#
# print('Зарплаты сотрудников:')
#
# for i in range(1, workers_count + 1):
#     wage = random.randrange(0, 100000, 20000)
#     wages_list.append(wage)
#     print(i, '-', wage)
#
# while 0 in wages_list:
#     wages_list.remove(0)
#
# print('Сокращено сотрудников:', workers_count - len(wages_list), '\nОсталось сотрудников:', len(wages_list))
#
# print('Зарплаты:', wages_list, '\nМаксимальная зп:', max(wages_list), '\nМинимальная зп:', min(wages_list))

# Задача 3. Кино

def make_random_words_list(word_list, max_cnt):
    random_words_list = []
    for _ in range(0, max_cnt):
        word = word_list[randint(0, len(word_list) - 1)]
        random_words_list.append(word)
    return random_words_list


# film_list = ['Аватар', 'Мстители: Финал', 'Титаник', 'Звёздные войны: Пробуждение силы',
#              'Мстители: Война бесконечности', 'Человек-паук: Нет пути домой', 'Мир юрского периода', 'Король Лев',
#              'Мстители', 'Форсаж 7', 'Холодное сердце 2', 'Топ Ган: Мэверик', 'Мстители: Эра Альтрона',
#              'Чёрная пантера', 'Гарри Поттер и Дары Смерти. Часть 2', 'Звёздные войны: Последние джедаи',
#              'Мир юрского периода 2', 'Холодное сердце', 'Красавица и чудовище', 'Суперсемейка 2', 'Форсаж 8',
#              'Железный человек 3', 'Миньоны', 'Первый мститель: Противостояние', 'Аквамен',
#              'Властелин колец: Возвращение короля', 'Человек-паук: Вдали от дома', 'Капитан Марвел',
#              'Трансформеры 3: Тёмная сторона Луны', '007: Координаты «Скайфолл»', 'Трансформеры: Эпоха истребления',
#              'Парк юрского периода', 'Тёмный рыцарь: Возрождение легенды', 'Джокер',
#              'Звёздные войны: Скайуокер. Восход', 'История игрушек 4', 'История игрушек: Большой побег',
#              'Пираты Карибского моря: Сундук мертвеца', 'Король Лев', 'Изгой-один. Звёздные войны: Истории', 'Аладдин',
#              'Пираты Карибского моря: На странных берегах', 'Гадкий я 3', 'В поисках Дори',
#              'Звёздные войны. Эпизод I: Скрытая угроза', 'Алиса в Стране чудес', 'Зверополис',
#              'Гарри Поттер и философский камень', 'Хоббит: Нежданное путешествие', 'Тёмный рыцарь',
#              'Мир юрского периода: Господство', 'Гарри Поттер и Дары Смерти. Часть 1', 'Гадкий я 2', 'Книга джунглей',
#              'Джуманджи: Зов джунглей', 'Хоббит: Битва пяти воинств', 'Пираты Карибского моря: На краю света',
#              'Хоббит: Пустошь Смауга', 'Доктор Стрэндж: В мультивселенной безумия', 'Властелин колец: Две крепости',
#              'Гарри Поттер и Орден Феникса', 'В поисках Немо', 'Гарри Поттер и Принц-полукровка', 'Шрек 2',
#              'Богемская рапсодия', 'Битва при Чосинском водохранилище', 'Властелин колец: Братство Кольца',
#              'Гарри Поттер и Кубок огня', 'Человек-паук 3: Враг в отражении', 'Ледниковый период 3: Эра динозавров',
#              '007: Спектр', 'Человек-паук: Возвращение домой', 'Гарри Поттер и Тайная комната',
#              'Ледниковый период 4: Континентальный дрейф', 'Тайная жизнь домашних животных',
#              'Бэтмен против Супермена: На заре справедливости', 'Война волков 2', 'Миньоны: Грювитация',
#              'Звёздные войны. Эпизод III: Месть ситхов', 'Голодные игры: И вспыхнет пламя', 'Стражи Галактики. Часть 2',
#              'Головоломка', 'Веном', 'Тор: Рагнарёк', 'Начало', 'Трансформеры: Месть падших',
#              'Сумерки. Сага: Рассвет — Часть 2', 'Человек-паук', 'Чудо-женщина', 'Привет, мамruen',
#              'День независимости', 'Фантастические твари и где они обитают', 'Шрек Третий', 'Тайна Коко',
#              'Джуманджи: Новый уровень', 'Гарри Поттер и узник Азкабана',
#              'Пираты Карибского моря: Мертвецы не рассказывают сказки', 'Инопланетянин',
#              'Миссия невыполнима: Последствия']
#
# user_top_films = []
# commands = ['добавить', 'вставить', 'удалить', 'выйти']
#
# while True:
#     print('Ваш текущий топ фильмов:', user_top_films)
#     film = film_list[randint(0, len(film_list) - 1)]
#     print('Название фильма:', film)
#     print('Команды: добавить, вставить, удалить, выйти')
#     command = commands[randint(0, len(commands) - 1)]
#     print(command)
#     if command == 'добавить':
#         if film in user_top_films:
#             print('Ошибка. Такой фильм уже есть в Вашем списке.')
#         else:
#             user_top_films.append(film)
#     elif command == 'вставить':
#         if film in user_top_films:
#             print('Ошибка. Такой фильм уже есть в Вашем списке.')
#         else:
#             print('На какое место?', end = ' ')
#             place = randint(1, len(user_top_films) + 1)
#             print(place)
#             user_top_films.insert(place - 1, film)
#     elif command == 'удалить':
#         if film in user_top_films:
#             user_top_films.remove(film)
#         else:
#             print('Ошибка. Такого фильма нет в Вашем списке.')
#     elif command == 'выйти':
#         break

# 16.3 Работа с несколькими списками. Методы extend и count

# Задача 1. Задачи компаний

# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
#
# first_company = [0, 0, 0]
#
# second_company = [1, 0, 0, 1, 1]
#
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company + second_company + third_company)
#
# print('Общий список задач:', main)
# print('Количество невыполненных задач:', main.count(0))

# Задача 2. Вредоносное ПО

import string
import random


# def make_random_word():
#     word = ''
#     punctuation_marks = ['!', '?']
#     letters_count = randint(3, 8)
#     for _ in range(letters_count):
#         letter = random.choice(string.ascii_lowercase)
#         word += letter
#     punc_marks_count = randint(0, 4)
#     for _ in range(0, punc_marks_count):
#         punc_mark = punctuation_marks[randint(0, 1)]
#         word += punc_mark
#     return word + ' '


# def make_random_message():
#     message = ''
#     word_cnt = randint(1, 5)
#     for _ in range(word_cnt):
#         word = make_random_word()
#         message += word
#     return message
#
#
# message_1 = make_random_message()
# message_2 = make_random_message()
# message_3 = ''
# print('Первое сообщение:', message_1, '\nВторое сообщение:', message_2)
#
# message_1_list, message_2_list = list(message_1), list(message_2)
#
#
# def punc_marks_cnt(message):
#     punc_marks_cnt = message.count('!') + message.count('?')
#     return punc_marks_cnt
#
#
# m_1_punc_cnt, m_2_punc_cnt = punc_marks_cnt(message_1_list), punc_marks_cnt(message_2_list)
#
# if m_1_punc_cnt == m_2_punc_cnt:
#     print('Ой')
# else:
#     if m_1_punc_cnt > m_2_punc_cnt:
#         message_3 += (message_1 + message_2)
#     elif m_1_punc_cnt < m_2_punc_cnt:
#         message_3 += (message_2 + message_1)
#     print('\nТретье сообщение:', message_3)

# Задача 3. Пакеты

# packs_amount = randint(2, 10)
# message = []
# trash_packs_count = 0
#
# for i in range(1, packs_amount + 1):
#     pack = []
#     print('Пакет номер', i)
#     for index in range(1, 5):
#         bite = randint(-1, 1)
#         print(i, 'бит:', bite)
#         pack.append(bite)
#     mist_cnt = pack.count(-1)
#     if mist_cnt <= 1:
#         message.extend(pack)
#     else:
#         print('Много ошибок в пакете')
#         trash_packs_count += 1
#
# print('Полученное сообщение:', message, '\nКол-во ошибок в сообщении:', message.count(-1),
#       '\nКол-во потерянных пакетов:', trash_packs_count)

# 16.4 Вложенные списки

# Задача 1. Матрица

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i_list in matrix:
#     for i_elem in i_list:
#         print(i_elem, end= ' ')
#     print('')

# Задача 2. Олимпиада

# while True:
#     participants_count = randint(10, 50)
#     team_size = randint(2, 10)
#     num = 1
#     print('Число участников:', participants_count, '\nЧеловек в команде:', team_size)
#     teams_list = []
#     if participants_count % team_size == 0:
#         for _ in range(participants_count // team_size):
#             teams_list.append(list(range(num, num + team_size)))
#             num += team_size
#         print('Список команд:', teams_list)
#         break
#     else:
#         print(participants_count, ' участников невозможно поделить на команды по', team_size, 'человек')

# Задача 3. Лавка

# goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
#
# fruits = ['Абрикос', 'Авокадо', 'Австромиртус', 'Азимина', 'Айва', 'Акебия', 'Аки', 'Алыча', 'Ананас', 'Аннона',
#           'Апельсин', 'Араза', 'Арбуз', 'Архат', 'Астрокариум', 'Баккорея', 'Баккорея', 'Баккорея', 'Бакупари', 'Банан',
#           'Билимби', 'Бирсонима', 'Бойзенова ягода', 'Боярышник', 'Бромелия', 'Бунхозия', 'Вампи', 'Виноград', 'Вишня',
#           'Воаванга', 'Восковница', 'Гандария', 'Гарциния', 'Генипа', 'Гетеромелес', 'Гилоцереус', 'Гранадилла',
#           'Гранат', 'Гревия', 'Грейпфрут', 'Грумичама', 'Груша', 'Гуава', 'Гуайява', 'Давидсония', 'Дакриодес',
#           'Джамбоза', 'Джамболан', 'Джамбу', 'Джекфрут', 'Дуриан', 'Дыня', 'Жаботикаба', 'Звёздчатое яблоко', 'Имбу',
#           'Инга', 'Инжир (фига)', 'Ирга', 'Каимито', 'Какао', 'Канистель', 'Канталупа', 'Капулин', 'Карамбола',
#           'Кариокар', 'Карисса', 'Квини', 'Кепель', 'Кешью', 'Кивано', 'Киви', 'Кизил', 'Кокколоба', 'Кокона', 'Кокос',
#           'Корлан', 'Королёк', 'Криптокария', 'Ксимения', 'Кудрания', 'Кумкват', 'Купуасу', 'Куруба', 'Лайм', 'Лангсат',
#           'Лардизабала', 'Лимон', 'Личи', 'Лонган', 'Лукума', 'Луло', 'Лума', 'Малина', 'Манго', 'Мангостан',
#           'Мандарин', 'Маракуйя', 'Маранг', 'Мелоди', 'Минеола', 'Мирциария', 'Момбин', 'Момордика', 'Мунтингия',
#           'Мушмула', 'Наранхилья', 'Нектарин', 'Опунция', 'Оробланко', 'Пальма', 'Пандан', 'Папайя', 'Папеда',
#           'Пассифлора', 'Переския', 'Персик', 'Питайя (питахайя)', 'Питецеллобиум', 'Питомба', 'Платония', 'Плумкот',
#           'Помароза', 'Помелит', 'Помело', 'Померанец', 'Пулазан', 'Пурума', 'Ракум-салакка', 'Рамбутан', 'Рангпур',
#           'Родомирт', 'Роллиния', 'Салак', 'Сантол', 'Саподилла', 'Сапота', 'Саусеп', 'Сахарное яблоко', 'Свити',
#           'Сизигиум', 'Сикана', 'Сирсак', 'Склерокария', 'Слива', 'Страстоцвет', 'Стрихнос', 'Тамарилло', 'Тамаринд',
#           'Угни', 'Учува', 'Фальза', 'Фейхоа', 'Фига', 'Физалис', 'Фикус', 'Филлантус', 'Хурма', 'Цедра', 'Чалта',
#           'Чемпедак', 'Черёмуха', 'Черешня', 'Черимойя', 'Чомпу', 'Чулюпа', 'Чупа-чупа', 'Шелковица', 'Шефердия',
#           'Эвтерпа', 'Элеокарпус', 'Яблоко',
#           ]
#
# shipment = [fruits[randint(0, len(fruits))], random.randrange(50, 300, 10)]
#
# goods.append(shipment)
# print('Новый ассортимент:', goods)
#
# for i in range(len(goods)):
#     goods[i][1] *= 1.08
#
# print('Новый ассортимент с увел. ценой:', goods)

# 16.5 Практическая работа

# Задача 1. Страшный код

# Метод 1

# main_list = [1, 5, 3]
# list_1 = [1, 5, 1, 5]
# list_2 = [1, 3, 1, 5, 3, 3]
#
# main_list.extend(list_1)
# print('Количество цифр 5 при первом объединении:', main_list.count(5))
#
# # for _ in range(main_list.count(5)):
# #     main_list.remove(5)
# #
# # main_list.extend(list_2)
# #
# # print('Количество цифр 3 при втором объединении:', main_list.count(3))
# #
# # print('Итоговый список:', main_list)
#
# # Метод 2
#
# main_list = list(filter((5).__ne__, main_list))
#
# main_list.extend(list_2)
#
# print('Количество цифр 3 при втором объединении:', main_list.count(3))
#
# print('Итоговый список:', main_list)

# Задача 2. Шеренга

# class_1 = list(range(160, 178, 2))
# class_2 = list(range(162, 183, 3))
# print('Класс 1:', class_1, '\nКласс 2:', class_2)
#
# class_1.extend(class_2)
# class_1.sort()
# print('Отсортированный список учеников:', class_1)

# Задача 3. Детали

shop = [
    ['каретка', 1200],
    ['шатун', 1000],
    ['седло', 300],
    ['педаль', 100],
    ['седло', 1500],
    ['рама', 12000],
    ['обод', 2000],
    ['шатун', 200],
    ['седло', 2700]
]
#
# detail = shop[randint(0, len(shop) - 1)][0]
# print('Название детали:', detail)
#
# detail_count = 0
# total_details_cost = 0
#
# for item in shop:
#     if item[0] == detail:
#         detail_count += 1
#         total_details_cost += item[1]
#
# print('Количество деталей:', detail_count, '\nОбщая стоимость:', total_details_cost)

# Задача 4. Вечеринка

# names = ['Александр', 'Агата', 'Аделина', 'Адель', 'Айдар', 'Александра', 'Алексей', 'Алёна', 'Алина', 'Алиса', 'Алия',
#          'Алла', 'Альберт', 'Альбина', 'Амалия', 'Амелия', 'Амина', 'Амир', 'Анастасия', 'Анатолий', 'Ангелина',
#          'Андрей', 'Анжелика', 'Анна', 'Антон', 'Антонина', 'Ариана', 'Арина', 'Арсен', 'Арсений', 'Артём', 'Артемий',
#          'Артур', 'Богдан', 'Борис', 'Вадим', 'Валентина', 'Валерий', 'Валерия', 'Варвара', 'Василий', 'Василина',
#          'Василиса', 'Вера', 'Вероника', 'Виктор', 'Виктория', 'Виолетта', 'Виталий', 'Виталина', 'Влад', 'Влада',
#          'Владимир', 'Владислав', 'Владислава', 'Всеволод', 'Вячеслав', 'Галина', 'Георгий', 'Герман', 'Глеб', 'Гордей',
#          'Григорий', 'Давид', 'Дамир', 'Даниил', 'Данил', 'Данила', 'Даниэль', 'Дарина', 'Дарья', 'Демид', 'Денис',
#          'Диана', 'Дмитрий', 'Ева', 'Евгений', 'Евгения', 'Егор', 'Екатерина', 'Елена', 'Елизавета', 'Елисей', 'Есения',
#          'Жанна', 'Зарина', 'Захар', 'Злата', 'Иван', 'Игнат', 'Игорь', 'Ильдар', 'Илья', 'Инна', 'Ирина', 'Камилла',
#          'Карина', 'Каролина', 'Кира', 'Кирилл', 'Константин', 'Кристина', 'Ксения', 'Лариса', 'Лев', 'Леонид', 'Лиана',
#          'Лидия', 'Лилия', 'Любовь', 'Людмила', 'Мадина', 'Майя', 'Макар', 'Максим', 'Марат', 'Маргарита', 'Марина',
#          'Мария', 'Марк', 'Марсель', 'Марьяна', 'Матвей', 'Мелания', 'Милана', 'Милена', 'Мирон', 'Мирослав',
#          'Мирослава', 'Михаил', 'Надежда', 'Назар', 'Наталия', 'Наталья', 'Наташа', 'Нелли', 'Ника', 'Никита',
#          'Николай', 'Нина', 'Одиссей', 'Оксана', 'Олег', 'Олеся', 'Ольга', 'Павел', 'Петр', 'Платон', 'Полина',
#          'Радмир', 'Рамиль', 'Регина', 'Ринат', 'Роберт', 'Родион', 'Роман', 'Ростислав', 'Руслан', 'Рустам', 'Савва',
#          'Савелий', 'Самир', 'Самира', 'Светлана', 'Святогор', 'Святослав', 'Семен', 'Сергей', 'Снежана', 'София',
#          'Софья', 'Станислав', 'Степан', 'Стефания', 'Таисия', 'Тамара', 'Тамерлан', 'Татьяна', 'Тимофей', 'Тимур',
#          'Тихон', 'Ульяна', 'Федор', 'Филипп', 'Эвелина', 'Эдуард', 'Элина', 'Эльвира', 'Эльмира', 'Эмилия', 'Эмиль',
#          'Юлиана', 'Юлия', 'Юрий', 'Ян', 'Яна', 'Яромир', 'Ярослав', 'Ярослава', 'Ясмина',
#          ]
#
# guests = make_random_words_list(names, 5)
#
# actions = ['пришёл', 'ушёл', 'пора спать']
# action = 'начнём'
#
#
# while action != 'пора спать':
#     action = actions[randint(0, 2)]
#     print('Сейчас на вечеринке', len(guests), 'человек:', guests)
#     print('Гость пришёл или ушёл?', action)
#     if action == 'пришёл':
#         new_guest_name = names[randint(0, len(names) - 1)]
#         print('Имя гостя:', new_guest_name)
#         if len(guests) < 6:
#             print('Привет, ' + new_guest_name + '!')
#             guests.append(new_guest_name)
#         else:
#             print('Прости, ' + new_guest_name + ', но мест нет')
#     elif action == 'ушёл':
#         if len(guests) == 0:
#             print('Все гости ушли.')
#         else:
#             old_guest_name = guests[randint(0, len(guests) - 1)]
#             print('Имя гостя:', old_guest_name)
#             print('Пока, ' + old_guest_name + '!')
#             guests.remove(old_guest_name)
#
#
# print('Вечеринка закончилась. Все легли спать.')

# Задача 5. Песни

# violator_songs = [
#     ['World in My Eyes', 4.86],
#     ['Sweetest Perfection', 4.43],
#     ['Personal Jesus', 4.56],
#     ['Halo', 4.9],
#     ['Waiting for the Night', 6.07],
#     ['Enjoy the Silence', 4.20],
#     ['Policy of Truth', 4.76],
#     ['Blue Dress', 4.29],
#     ['Clean', 5.83]
# ]
#
# violator_songs_copy = violator_songs.copy()
#
# selected_songs_num = randint(1, len(violator_songs))
# print('Сколько песен выбрать?', selected_songs_num)
#
# print('Выбор песен:')
# selected_songs = []
#
# for i in range(1, selected_songs_num + 1):
#     song = violator_songs_copy[randint(0, len(violator_songs_copy) - 1)]
#     print(i, '-', song[0])
#     selected_songs.append(song)
#     violator_songs_copy.remove(song)
#
# songs_length_sum = 0
#
# for i in range(0, len(selected_songs)):
#     songs_length_sum += selected_songs[i][1]
#
# print('Общее время звучания песен:', songs_length_sum, 'минуты')

# Задача 6. Уникальные элементы

# list_1 = []
# list_2 = []
#
# num_cnt_list_1 = 3
# num_cnt_list_2 = 7
#
#
# def make_num_list(count, list):
#     for i in range(1, count + 1):
#         num = randint(1, 10)
#         print(str(i) + ') ' + str(num))
#         list.append(num)
#
#
# print('Числа для первого списка:')
# make_num_list(num_cnt_list_1, list_1)
#
# print('\nЧисла для второго списка:')
# make_num_list(num_cnt_list_2, list_2)
#
# list_1.extend(list_2)
#
# num_count_list = []
#
# for num in list_1:
#     count = list_1.count(num)
#     num_count_list.append([num, count])
#
# print(num_count_list)
#
# while len(num_count_list) != 0:
#     num_to_remove = num_count_list[0][0]
#     list_to_remove = num_count_list[0]
#     count = num_count_list[0][1]
#     for _ in range(count):
#         num_count_list.remove(list_to_remove)
#     for _ in range(count - 1):
#         list_1.remove(num_to_remove)
#
# print('Новый первый список с уникальными элементами:', list_1)

# Задача 7. Ролики

# def make_num_list(start, stop, count, list):
#     for i in range(1, count + 1):
#         num = randint(start, stop)
#         print(str(i) + ') ' + str(num))
#         list.append(num)
#
# skates_cnt = randint(4, 10)
# pers_cnt = randint(4, 10)
#
# skates_size_list = []
# pers_size_list = []
#
# print('Количество коньков:', skates_cnt)
# print('Размер коньков:')
# make_num_list(35, 45, skates_cnt, skates_size_list)
#
# print('\nКоличество людей:', pers_cnt)
# print('Размер ноги:')
# make_num_list(35, 45, pers_cnt, pers_size_list)
#
# match_list = []
# non_match_list = []
#
#
# while len(pers_size_list) != 0 and len(skates_size_list) != 0:
#     foot_max = max(pers_size_list)
#     skate_max = max(skates_size_list)
#     if foot_max <= skate_max:
#         match_list.append([foot_max, skate_max])
#         pers_size_list.remove(foot_max)
#         skates_size_list.remove(skate_max)
#     else:
#         non_match_list.append(foot_max)
#         pers_size_list.remove(foot_max)
#
# non_match_list.extend(pers_size_list)
#
# print('Наибольшее кол-во людей, которые могут взять ролики:', len(match_list))
# print('Список размеров (размер ноги, размер коньков):', match_list)
# print('Размеры ног, на которые коньков не нашлось:', non_match_list)

# Задача 8. Считалка

# Метод 1

# pers_cnt =7# randint(4, 10)
# pers_list = list(range(1, pers_cnt + 1))
# count_num = 6# randint(1, 10)
# print('Количество человек:', pers_cnt, '\nЧисло в считалке:', count_num)
# print('Значит, выбывает каждый ' + str(count_num) + '-й человек')
# start_num_index = 0
#
# while len(pers_list) != 1:
#     print('')
#     print('Текущий круг людей:', pers_list)
#     print('start_num_index', start_num_index)
#     print('Начало счёта с номера', pers_list[start_num_index])
#     num_to_remove_index = ((start_num_index + (count_num % len(pers_list)) - 1) % len(pers_list))
#     print('Выбывает человек под номером', pers_list[num_to_remove_index])
#     pers_list.pop(num_to_remove_index)
#     start_num_index = num_to_remove_index - len(pers_list)
#     print('num_to_remove_index', num_to_remove_index)
#
# print('\nОстался человек под номером', pers_list[0])

# Метод 2

# pers_cnt = randint(4, 10)
# pers_list = list(range(1, pers_cnt + 1))
# count_num = randint(1, 10)
# print('Количество человек:', pers_cnt, '\nЧисло в считалке:', count_num)
# print('Значит, выбывает каждый ' + str(count_num) + '-й человек')
# start_num_index = 0
#
# while len(pers_list) != 1:
#     print('')
#     print('Текущий круг людей:', pers_list)
#     print('start_num_index', start_num_index)
#     print('Начало счёта с номера', pers_list[start_num_index])
#     num_to_remove_index = (start_num_index + count_num - 1) % len(pers_list)
#     print('Выбывает человек под номером', pers_list[num_to_remove_index])
#     pers_list.pop(num_to_remove_index)
#     start_num_index = num_to_remove_index % len(pers_list)
#     print('num_to_remove_index', num_to_remove_index)
#
# print('\nОстался человек под номером', pers_list[0])

# Задача 9. Друзья

# friends_cnt = randint(3, 10) # определяем рандомом количество друзей
# debt_papers_num = randint(3, 10) # определяем рандомом количество расписок
#
# friends_list = list(range(1, friends_cnt + 1)) # составляем список друзей
# friends_list_copy = friends_list.copy() # делаем копию списка друзей, чтобы дальше использовать её в цикле для исключения повторения друзей в одной расписке (чтобы один друг не был и кредитором, и должником)
# print('Количество друзей:', len(friends_list))
# debts_list = [] # сосздаём пустой список, в который ниже в цикле будет добавляться информация из долговых расписок
#
# for i in range(1, debt_papers_num + 1): # печатаем на экране расписку и добавляем из неё информацию в debts_list
#     print('\n' + str(i) + '-я расписка:')
#     creditor = friends_list[randint(0, friends_cnt - 1)] # определяем рандомом кредитора
#     friends_list_copy.remove(creditor) # удаляем из копии списка друзей кредитора, чтобы он не стал дебитором
#     debtor = friends_list_copy[randint(0, friends_cnt - 2)] # определяем рандомом дебитора
#     debt = random.randrange(1, 1000) # определяем рандомом сумму долга
#     debts_list.append([creditor, debtor, debt]) # добавляем информацию из расписки в debts_list в виде вложенного списка new_debt_info
#     print('Кому:', creditor, '\nОт кого:', debtor, '\nСколько:', debt)
#     friends_list_copy = friends_list.copy() # возвращаем копию списка друзей в первоначальный вид для следующего цикла
#
# friend_balance_list = [] # создаём пустой список, куда будем складывать информацию о балансе друзей
# friend_cred = 0 # кредит друга
# friend_debt = 0 # дебет друга
#
# for friend in friends_list: # идём по списку друзей
#     for i_debt in debts_list: # идём по списку с информацией из долговых расписок
#         if i_debt[0] == friend:
#             friend_cred += i_debt[2] # суммируем кредит друга
#         if i_debt[1] == friend:
#             friend_debt += i_debt[2] # суммируем дебет друга
#     friend_balance_list.append([friend, friend_cred - friend_debt]) # добавляем информацию о балансе друга в список
#     friend_cred = 0
#     friend_debt = 0
#
# print('\nБаланс друзей:')
# for i_info in friend_balance_list:
#     print(str(i_info[0]) + ': ' + str(i_info[1]))

# Задача 10. Симметричная последовательность

# Метод 1 (мой)

# number_cnt = randint(3, 10)
# print('Количество чисел:', number_cnt)
#
# number_list = []
# print('Последовательность:')
#
# for _ in range(number_cnt):
#     number = randint(0, 9)
#     number_list.append(number)
#
# print(number_list)
#
# i = 0
#
# if number_list == number_list[::-1]:
#     print('Последовательность уже является симметричной. Новых чисел приписывать не нужно.')
# else:
#     while number_list != number_list[::-1]:
#         number_list.insert(number_cnt, number_list[i])
#         i += 1
#
# print('Нужно приписать чисел:', i)
# print('Сами числа:', number_list[number_cnt::])

# Метод 2 (из разбора ДЗ)

def is_palindrome(num_list):
    reverse_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i_num])
    if num_list == reverse_list:
        return True
    else:
        return False


nums = [1, 2, 3, 4, 5]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Исходный список:', nums)
print('Нужно чисел для палиндрома:', len(answer))
print('Список этих чисел:', answer)
