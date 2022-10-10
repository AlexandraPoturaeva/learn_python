# 18.2 Форматирование строк: format и f-strings
# Задача 1. Заказ
import random

from my_modules import helper

names = ['Александр', 'Агата', 'Аделина', 'Адель', 'Айдар', 'Александра', 'Алексей', 'Алёна', 'Алина', 'Алиса', 'Алия',
         'Алла', 'Альберт', 'Альбина', 'Амалия', 'Амелия', 'Амина', 'Амир', 'Анастасия', 'Анатолий', 'Ангелина',
         'Андрей', 'Анжелика', 'Анна', 'Антон', 'Антонина', 'Ариана', 'Арина', 'Арсен', 'Арсений', 'Артём', 'Артемий',
         'Артур', 'Богдан', 'Борис', 'Вадим', 'Валентина', 'Валерий', 'Валерия', 'Варвара', 'Василий', 'Василина',
         'Василиса', 'Вера', 'Вероника', 'Виктор', 'Виктория', 'Виолетта', 'Виталий', 'Виталина', 'Влад', 'Влада',
         'Владимир', 'Владислав', 'Владислава', 'Всеволод', 'Вячеслав', 'Галина', 'Георгий', 'Герман', 'Глеб', 'Гордей',
         'Григорий', 'Давид', 'Дамир', 'Даниил', 'Данил', 'Данила', 'Даниэль', 'Дарина', 'Дарья', 'Демид', 'Денис',
         'Диана', 'Дмитрий', 'Ева', 'Евгений', 'Евгения', 'Егор', 'Екатерина', 'Елена', 'Елизавета', 'Елисей', 'Есения',
         'Жанна', 'Зарина', 'Захар', 'Злата', 'Иван', 'Игнат', 'Игорь', 'Ильдар', 'Илья', 'Инна', 'Ирина', 'Камилла',
         'Карина', 'Каролина', 'Кира', 'Кирилл', 'Константин', 'Кристина', 'Ксения', 'Лариса', 'Лев', 'Леонид', 'Лиана',
         'Лидия', 'Лилия', 'Любовь', 'Людмила', 'Мадина', 'Майя', 'Макар', 'Максим', 'Марат', 'Маргарита', 'Марина',
         'Мария', 'Марк', 'Марсель', 'Марьяна', 'Матвей', 'Мелания', 'Милана', 'Милена', 'Мирон', 'Мирослав',
         'Мирослава', 'Михаил', 'Надежда', 'Назар', 'Наталия', 'Наталья', 'Наташа', 'Нелли', 'Ника', 'Никита',
         'Николай', 'Нина', 'Одиссей', 'Оксана', 'Олег', 'Олеся', 'Ольга', 'Павел', 'Петр', 'Платон', 'Полина',
         'Радмир', 'Рамиль', 'Регина', 'Ринат', 'Роберт', 'Родион', 'Роман', 'Ростислав', 'Руслан', 'Рустам', 'Савва',
         'Савелий', 'Самир', 'Самира', 'Светлана', 'Святогор', 'Святослав', 'Семен', 'Сергей', 'Снежана', 'София',
         'Софья', 'Станислав', 'Степан', 'Стефания', 'Таисия', 'Тамара', 'Тамерлан', 'Татьяна', 'Тимофей', 'Тимур',
         'Тихон', 'Ульяна', 'Федор', 'Филипп', 'Эвелина', 'Эдуард', 'Элина', 'Эльвира', 'Эльмира', 'Эмилия', 'Эмиль',
         'Юлиана', 'Юлия', 'Юрий', 'Ян', 'Яна', 'Яромир', 'Ярослав', 'Ярослава', 'Ясмина',
         ]

# client_name = random.choice(names)
# client_order_num = random.randint(10000, 20000)
# print('Имя:', client_name, '\nНомер заказа:', client_order_num)
# print('Здравствуйте, {name}! Ваш номер заказа: {num}. Приятного дня!'.format(
#     name=client_name,
#     num=client_order_num
# ))

# Задача 2. Долги

# friend_name = random.choice(names)
# friend_debt = random.randint(100, 1000)
# print('Имя:', friend_name, '\nДолг:', friend_debt)
#
# print('{0}! {0}, привет! Как дела, {0}! Где мои {1} рублей? {0}!'.format(
#     friend_name,
#     friend_debt
# ))

# Задача 3. IP-адрес

# ip_address = '{0}.{1}.{2}.{3}'
# numbers = [random.randint(0, 225) for _ in range(4)]
# print(ip_address.format(*numbers))

# 18.3 Методы строк: split и join

# Задача 1. Улучшенная лингвистика 2

# words_to_find_list = helper.make_random_text_list('words', 3)
# text_where_to_find = helper.make_random_text_list('words', 20)
#
# words_to_find_str = ' '.join(words_to_find_list)
# text_where_to_find_str = ' '.join(text_where_to_find)
#
# print('Список слов для подсчёта их частоты употребления в тексте:', words_to_find_str, '\nТекст:', text_where_to_find_str)

# # Метод 1
#
# words_freq_dict = {i: text_where_to_find.count(i) for i in words_to_find_list}
# for key, value in words_freq_dict.items():
#     print(key + ': ' + str(value))
#
# # Метод 2
# words_count = [str(text_where_to_find_str.count(word)) for word in words_to_find_list]
# words_count_info_list = [': '.join([words_to_find_list[i], words_count[i]]) for i in range(3)]
# words_count_info_text = '\n'.join(words_count_info_list)
# print(words_count_info_text)

# Задача 2. Бабушка

# text = ''
#
# for _ in range(random.randint(3, 7)):
#     text += (helper.make_random_letters_sequence() + (' ' * random.randint(1, 4)))
#
# print('Текст:', text)
#
# correct_text = ' '.join(text.split())
#
# print(correct_text)

# Задача 3. Разделители символов

# grats_template = 'С днём рождения, {name}! Тебе уже {age} лет!'
#
# persons_count = random.randint(1, 10)
#
# names_list = helper.make_random_text_list('names_male', persons_count)
# surnames_list = helper.make_random_text_list('russian_surnames', persons_count)
#
# birthday_pers_list = [' '.join([names_list[i], surnames_list[i]]) for i in range(persons_count)]
# birthday_pers_text = ', '.join(birthday_pers_list)
# print('Список людей через запятую:', birthday_pers_text)
#
# age_list = [str(random.randint(10, 100)) for i in range(persons_count)]
# age_text = ' '.join(age_list)
# print('Возраст людей через пробел:', age_text)

# Метод 1
# for i_pers in range(persons_count):
#     print(grats_template.format(name = birthday_pers_list[i_pers], age = age_list[i_pers]))

# Метод 2

# for index, person in enumerate(birthday_pers_list):
#     print(grats_template.format(name=person, age=age_list[index]))

# Метод 3

# for age, name in zip(age_list, birthday_pers_list):
#     print(grats_template.format(name=name, age=age))
#
# persons_and_age_list = [' '.join([birthday_pers_list[i], age_list[i]]) for i in range(persons_count)]
# persons_and_age_text = ', '.join(persons_and_age_list)
# print('\nИменинники:', persons_and_age_text)

# 18.4 Методы строк: startswith, endswith, upper, lower

# Задача 1. Шифр Цезаря 2

# words_list = [helper.make_random_letters_sequence_up_low() for _ in range(random.randint(10, 30))]
# text = ' '.join(words_list)
# shift = random.randint(1, 26)
# print('Сообщение:', text, '\nСдвиг:', shift)
#
# text_lowercase = text.lower()
#
# eng_alphabet = [chr(index) for index in range(ord("a"), ord("z") + 1)]
#
#
# def caesar_cipher(user_text, user_shift):
#     char_list = [(eng_alphabet[(eng_alphabet.index(sym) + user_shift) % 26] if sym != ' ' else ' ') for sym in user_text]
#     return ''.join(char_list)
#
#
# text_encrypted = caesar_cipher(text_lowercase, shift)
# print('Зашифрованное сообщение:', text_encrypted)

# Задача 2. Путь к файлу

# paths_list = ['C:/user/docs/folder/new_file.txt', 'D:/user/docs/folder/new_file.txt',
#               'C:/user/docs/folder/new_file.jpg', 'D:/user/docs/folder/new_file.jpg']
#
# path = random.choice(paths_list)
# disk = random.choice(['C', 'D'])
# file_extension = random.choice(['.txt', '.jpg'])
#
# print('Путь к файлу:', path,
#       '\nНа каком диске должен лежать файл:', disk,
#       '\nТребуемое расширение файла:', file_extension)
#
# if not path.startswith(disk):
#     print('Ошибка. Неверно указан диск.')
# elif not path.endswith(file_extension):
#     print('Ошибка. Неверно указано расширение файла.')
# else:
#     print('Путь корректен!')

# Задача 3. Удаление части

# text = ' '.join([helper.make_random_letters_sequence_up_low() for _ in range(random.randint(1, 10))])
# print('Текст:', text)

# Метод 1 (мой)

# low_count = 0
# upper_count = 0

# for sym in text:
#     if sym.islower():
#         low_count +=1
#     elif sym.isupper():
#         upper_count +=1

# Метод 2 (из разбора дз)

# low_count = len([letter for letter in text if letter.islower()])
# upper_count = len([letter for letter in text if letter.isupper()])
#
# print('Количество заглавных букв:', upper_count,
#       '\nКоличество строчных букв:', low_count,
#       '\nРезультат: ', end='')
#
# if low_count > upper_count:
#     print(text.lower())
# elif low_count == upper_count:
#     print('Количество заглавных и строчных букв одинаковое. Текст форматировать не нужно.')
# else:
#     print(text.upper())




