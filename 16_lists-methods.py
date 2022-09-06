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

# import string
# import random
#
#
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
#
#
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



