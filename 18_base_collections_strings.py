# 18.2 Форматирование строк: format и f-strings
# Задача 1. Заказ
import random
import string
from random import randint
from random import shuffle

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

# 18.6 Практическая работа

# Задача 1. Меню ресторана

# dishes_avail_list = helper.make_random_text_list('russian_dishes', random.randint(5, 10))
# dishes_avail_text = ';'.join(dishes_avail_list).lower()
# print('Доступное меню:', dishes_avail_text)
# print('На данный момент в меню есть:', dishes_avail_text.replace(';', ', '))

# Задача 2. Самое длинное слово

# text = ' '.join(helper.make_random_text_list('words', random.randint(5, 10)))
# print('Текст:', text)
#
# words_list = text.split()
# max_length_word = max(words_list, key=len)
# print('Самое длинное слово:', max_length_word, '\nДлина этого слова:', len(max_length_word))

# Задача 3. Файлы

# file_extensions = ['.txt', '.jpg', '.docx', '.ttx', '.doxc', '.xtt', '.doc']
# file_extensions_right = ['.txt', '.docx']
# special_syms = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
# file_beginings = special_syms.copy()
# file_beginings.append('')
#
# while True:
#     file_name = random.choice(file_beginings) + 'new_file' + random.choice(file_extensions)
#     print('Название файла:', file_name)
#     if file_name.startswith(tuple(special_syms)):
#         print('Ошибка: название начинается на один из специальных символов.')
#     if not file_name.endswith(tuple(file_extensions_right)):
#         print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
#     else:
#         print('Файл назван верно.')
#         break

# Задача 4. Заглавные буквы

# user_text = ' '.join([helper.make_random_letters_sequence_up_low() for _ in range(random.randint(3, 8))])
# print('Текст:', user_text)
#
# final_text = user_text.title()
# print('Результат:', final_text)

# Задача 5. Пароль

# while True:
#     password = helper.make_random_letters_sequence_up_low() + str(random.randint(0, 999))
#     print('Придумайте пароль:', password)
#     length = len(password)
#     digits_cnt = len([i for i in password if i.isdigit()])
#     upper_cnt = len([i for i in password if i.isupper()])
#     if length < 8 or digits_cnt < 3 or upper_cnt < 1:
#         print('Пароль ненадёжный. Попробуйте ещё раз.')
#     else:
#         print('Это надёжный пароль!')
#         break

# Задача 6.

# text = 'aaAAbbсaaaA' #helper.make_random_letters_sequence_up_low()
# print('Cтрока:', text)
# text_divided = []
# start = 0
#
# for i in range(1, len(text)):
#     if text[i] != text[start]:
#         text_divided.append(text[start:i])
#         start = i
# text_divided.append(text[start:])
#
# result = ''.join([i[0] + str(len(i)) for i in text_divided])
#
# print('Закодированная строка:', result)

# Задача 7.

# ip = random.choice(['128.16.35.a4', '240.127.56.340', '34.56.42,5', '128.0.0.255'])
# print('Введённый IP-адрес:', ip)
#
# ip_list = ip.split('.')
# accordance = True
#
# for i in ip_list:
#     if not i.isdigit():
#         accordance = False
#         if i.isalnum():
#             print(i, '- это не целое число.')
#         else:
#             print('Адрес — это четыре числа, разделённые точками.')
#     elif i.isdigit() and not 0 <= int(i) <= 255:
#         accordance = False
#         print(i, 'не находится в диапазоне от 0 до 255.')
#
# if accordance:
#     print('IP-адрес корректен.')

# Задача 8. Бегущая строка

# strings = ['abcd', 'cdab', 'cdba', 'bcda', 'dabc', 'bdac', 'cbda']
# first_string = random.choice(strings)
# strings.remove(first_string)
# second_string = random.choice(strings)
# print('Первая строка:', first_string,
#       '\nВторая строка:', second_string)
#
# first_string_list = list(first_string)
# second_string_list = list(second_string)
#
# equals = 0
# shift = 1
#
# for _ in range(0, len(first_string_list) - 1):
#     second_string_shift = [second_string_list[(i-shift) % len(second_string_list)] for i in range(len(second_string_list))]
#     if second_string_shift == first_string_list:
#         print('Первая строка получается из второй со сдвигом', shift)
#         equals = 1
#         break
#     else:
#         shift += 1
#
# if equals == 0:
#     print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


# Задача 9

word_list = [helper.make_random_letters_sequence_up_low() for _ in range(30)]
word_list_punc = [helper.make_random_letters_sequence_up_low() + random.choice(string.punctuation) for _ in range(30)]
punc_list = [helper.make_random_punc_sequence() for _ in range(30)]
list_for_random = word_list + word_list_punc + punc_list
shuffle(list_for_random)
# user_text_list = [random.choice(list_for_random) for _ in range(random.randint(2, 10))]
user_text_string = 'Хотя ,. возм:ожно и нет.'#' '.join(user_text_list)
user_text_list = user_text_string.split(' ')


print('Сообщение:', user_text_string)
final_text_list = []


def is_word_only_punc(word):
    check = True
    for i in word:
        if i.isalpha():
            check = False
            break
    return check


def reverse_word_with_punc(word):
    words = []
    start = 0
    i_count = 0
    for i in word:
        if i in string.punctuation:
            words.append(word[i_count - 1:start:-1] + word[start] + i)
            start = i_count
        i_count += 1
    words.append(word[i_count - 1:start:-1])
    final_word = ''.join(words)
    return final_word


for word in user_text_list:
    if word.isalpha():
        word_final = word[::-1]
    else:
        if is_word_only_punc(word):
            word_final = word
        else:
            word_final = reverse_word_with_punc(word)
    final_text_list.append(word_final)

final_text_string = ' '.join(final_text_list)

print(final_text_string)

# Задача 10. Истина
#
# text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt ' \
#        'cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf ' \
#        'dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt ' \
#        'foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip ' \
#        'fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf ' \
#        'sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu ' \
#        'nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b ' \
#        'hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
#
# word_list = text.split() # разбиваем текст на слова (разделитель - пробел)
#
# sentences = [] # разбиваем word_list на предложения ('/' - это зашифрованная точка. Слова, содержащие точку, завершают предложения)
# start = 0
# for i in range(len(word_list)):
#     if word_list[i].find('/') != -1:
#         sentences.append(word_list[start:i + 1])
#         start = i + 1
#
# text_list = [[[chr(ord(i) - 1) for i in n] for n in sentence] for sentence in sentences] #расшифровываем буквы
#
# shift = 3 #сдвигаем буквы в словах на n знаков, начиная с 3 (в каждом предложении сдвиг увеличивается на 1)
# correct_text = []
# for sentence in text_list:
#     correct_sentence = []
#     for word in sentence:
#         correct_word = [word[(i-shift) % len(word)] for i in range(len(word))]
#         print(correct_word)
#         correct_sentence.append(''.join(correct_word))
#     correct_text.append(' '.join(correct_sentence))
#     shift += 1
#
# for i in correct_text:
#     print(i)
