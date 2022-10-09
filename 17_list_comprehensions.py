from random import randint

# 17.2 List comprehensions

# Задача 1. Кубы и квадраты

# left_num = randint(0, 10)
# right_num = left_num + randint(1, 10)
#
# cubes = [x ** 3 for x in range(left_num, right_num + 1)]
# squares = [x ** 2 for x in range(left_num, right_num + 1)]
#
# print('Левая граница:', left_num, '\nПравая граница:', right_num)
# print('Список кубов чисел в диапазоне от ' + str(left_num) + ' до ' + str(right_num) + ':', cubes)
# print('Список квадратов чисел в диапазоне от ' + str(left_num) + ' до ' + str(right_num) + ':', squares)

# Задача 2. Сообщение

import string
import random


def make_random_letters_sequence():
    word = ''
    letters_count = randint(8, 15)
    for _ in range(letters_count):
        letter = random.choice(string.ascii_lowercase)
        word += letter
    return word


# user_text = make_random_letters_sequence()
# user_sym = random.choice(string.punctuation)
#
# print('Строка:', user_text, '\nДополнительный символ:', user_sym)
#
# double_symbol_text = [x * 2 for x in user_text]
# double_symbol_text_plus_sym = [x + user_sym for x in double_symbol_text]
#
# print('\nСписок удвоенных символов:', double_symbol_text)
# print('Склейка с дополнительным символом:', double_symbol_text_plus_sym)

# Задача 3. Повышение цен

# prices_current = [round(random.uniform(0, 100), 2) for _ in range(0, 5)]
# percent_first_year = randint(1, 100)
# percent_second_year = randint(1, 100)
# print('Текущие цены:', prices_current, '\nПовышение цен на первый год, %:', percent_first_year,
#       '\nПовышение цен на второй год, %:', percent_second_year)
#
#
# def get_new_price(price, percent):
#     return round(price * (1 + percent / 100), 2)
#
#
# prices_first_year = [get_new_price(i_price, percent_first_year) for i_price in prices_current]
# prices_second_year = [get_new_price(i_price, percent_second_year) for i_price in prices_first_year]
#
# print('Сумма цен за каждый год:', round(sum(prices_current), 2), round(sum(prices_first_year), 2),
#       round(sum(prices_second_year), 2))

# 17.3 List comprehensions с условиями. Модуль random

# Задача 1. Список чётных чисел

# left_num = randint(1, 50)
# right_num = left_num + randint(1, 50)
#
# even_nums = [x for x in range(left_num, right_num + 1) if x % 2 == 0]
#
# print('Список чётных чисел от ' + str(left_num) + ' до ' + str(right_num) + ':', even_nums)

# Задача 2. Магазин

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
#
# correct_prices = [(price if price > 0 else 0) for price in original_prices]
#
# print('Исправленные цены:', correct_prices)

# Задача 3. Отряды

# squad_1 = [randint(50, 80) for _ in range(10)]
# squad_2 = [randint(30, 60) for _ in range(10)]
#
# squad_3_condition = [('Погиб' if (squad_1[i_damage] + squad_2[i_damage] > 100) else 'Выжил') for i_damage in range(10)]
#
# print('Урон первого отряда:', squad_1, '\nУрон второго отряда:', squad_2,
#       '\nСостояние третьего отряда:', squad_3_condition)

# 17.4 Срезы списков

# Задача 1. Анализ цен

# original_prices = [randint(-100, 100) for _ in range(randint(3, 20))]
# new_prices = [(price if price > 0 else 0) for price in original_prices]
#
# print('Пакет данных:', original_prices)
# print("Мы потеряли:",  sum(new_prices) - sum(original_prices))

# Задача 2. Срезы

# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
#
# print(nums[:5])
# print(nums[:-2])
# print(nums[::2])
# print(nums[1::2])
# print(nums[::-1])
# print(nums[-1::-2])

# Задача 3. Удаление части

# num_list = [randint(-100, 100) for _ in range(randint(5, 15))]
# num_list_to_cut = num_list[:]
# num_2 = randint(0, len(num_list) - 1)
# num_1 = num_2 - randint(1, num_2 - 1)
#
# num_list_to_cut[num_1:num_2 + 1] = []
# print('Изначальный список:', num_list)
# print('Нужно удалить числа с индексами с', num_1, 'по', num_2)
# print('Результат:', num_list_to_cut)

# 17.7 Практическая работа

# Задача 1. Гласные буквы

# vowels_in_rus_lst = ['А', 'а', 'Е', 'е', 'Ё', 'ё', 'И', 'и', 'О', 'о', 'У', 'у', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']
#
words_to_random = ['цельность', 'опоражнивание', 'сотоварищ', 'закаменелость', 'гунтер', 'камышит',
                   'рационалистичность', 'классная', 'оладья', 'хроматин', 'допустимость', 'разряжённость',
                   'красавица', 'шасла', 'обыкновение', 'норд-норд-вест', 'зашлаковка', 'антивитамин', 'обсолка',
                   'сакс',
                   'показательность', 'оркестрование', 'бойлерная', 'обращаемость', 'нормировщица',
                   'бездельничание',
                   'буревал', 'вискозиметр', 'казашка', 'инерция', 'водобой', 'сиротство', 'муссирование', 'шёпот',
                   'оправдание', 'ушкуй', 'гной', 'цыкание', 'призванный', 'прусик', 'озимость', 'баобаб',
                   'оттоманка',
                   'улем', 'линолеумщик', 'стенописец', 'пластование', 'рокфор', 'модельщик', 'омёт',
                   'либеральничество', 'подзащитный', 'докалка', 'бракосочетание', 'флюсование', 'бадминтонист',
                   'прижимание', 'триединство', 'мокшанка', 'ночёвка', 'персона', 'возмутительность', 'мензурка',
                   'проколка', 'шитьё', 'найтов', 'расплывчатость', 'арбитраж', 'ритуал', 'гемоглобин',
                   'примораживание', 'полуфабрикат', 'эгоист', 'расстреливание', 'стеблевание', 'протагонистка',
                   'теленомус', 'вулканолог', 'пролетаризирование', 'анероид', 'прокапчивание', 'планшайба',
                   'солерос',
                   'отпускница', 'пессимистичность', 'маца', 'хрустение', 'жизнеустройство', 'переколка', 'убежище',
                   'психофизиология', 'ярь-медянка', 'реставратор', 'велюр', 'портрет', 'огурец', 'граб',
                   'одутловатость', 'девочка', 'мозаичист', 'лужичанка', 'недодержка', 'серб', 'своевольная',
                   'добровольность', 'позеленение', 'хлыстовщина', 'пересыхание', 'лаконичность', 'пырник',
                   'проблематичность', 'сваривание', 'нить', 'кожеед', 'вспыхивание', 'труппа', 'оттяжка', 'праща',
                   'нематериальность', 'фитопланктон', 'вылов', 'взаимность', 'комара', 'типичное',
                   'тождественность',
                   'бизон', 'прилаживание', 'параметрит', 'густолесье', 'зарница', 'местообитание', 'обрывистость',
                   'сиповатость', 'бомбардирование', 'застопоривание', 'подготовительница', 'вруб',
                   'светолюбивость',
                   'хамит', 'перескабливание', 'половщик', 'псевдоучёность', 'пересечённость', 'оккупация',
                   'плющильня',
                   'переизбрание', 'обмазка', 'жестикулирование', 'лебяжина', 'божественность', 'независимость',
                   'шваб',
                   'предпочтительность', 'дезертирство', 'суеверие', 'тундрянка', 'чеченка', 'сочевичник', 'киянка',
                   'пермячка', 'бронекатер', 'хлебопечение', 'воронение', 'фал', 'песня', 'федералист', 'прокус',
                   'гунн', 'каландр', 'отдалённость', 'электропилка', 'кочевница', 'садовница', 'нарастание',
                   'отметина', 'персонаж', 'бездумность', 'исцелительница', 'мрачность', 'супоросость', 'цевьё',
                   'клирик', 'выщипывание', 'прививка', 'чересседельник', 'окольничий', 'фильтрат', 'обитательница',
                   'добивание', 'ламаркизм', 'гонт', 'академгородок', 'расшатывание', 'судопроизводство',
                   'обездоленность', 'финно-угроведение', 'стругание', 'захоронение', 'фронт', 'угольщик',
                   ]


def make_random_text(word_list):
    random_text = ''
    for _ in range(0, randint(1, 8)):
        word = word_list[randint(0, len(word_list) - 1)]
        random_text += word + ' '
    return random_text


#
#
# text = make_random_text(words_to_random)
# print('Текст:', text)
#
# vowels_in_text = [x for x in text if x in vowels_in_rus_lst]
#
# print('Список гласных букв:', vowels_in_text)
# print('Длина списка:', len(vowels_in_text))

# Задача 2. Генерация

# list_length = randint(5, 20)
# print('Длина списка:', list_length)
#
# num_list = [(1 if x % 2 == 0 else x % 5) for x in range(list_length)]
# print('Результат:', num_list)

# Задача 3. Случайные соревнования

# team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
# team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
# print('Первая команда:', team_1, '\nВторая команда:', team_2)
#
# winners = [(team_1[x] if team_1[x] > team_2[x] else team_2[x]) for x in range(20)]
# print('Победители:', winners)

# Задача 4. Тренируемся со срезами

# alphabet = 'abcdefg'
#
# print(alphabet[:])
# print(alphabet[::-1])
# print(alphabet[::2])
# print(alphabet[1::2])
# print(alphabet[:1])
# print(alphabet[:-2:-1])
# print(alphabet[3:4])
# print(alphabet[-3:])
# print(alphabet[3:5])
# print(alphabet[4:2:-1])

# Задача 5. Разворот

# word = make_random_letters_sequence()
#
# word_list = list(word)
# if word_list.count('h') < 2:
#     for _ in range(word_list.count('h'), 2):
#         word_list.insert(randint(0, len(word_list)), 'h')
#
# final_word_with_2h = ''
#
# for letter in word_list:
#     final_word_with_2h += letter
#
# print('Строка:', final_word_with_2h)
#
# h_indexes = [i for i, x in enumerate(word_list) if x == 'h']
#
# print('Развёрнутая последовательность между первым и последним h:', final_word_with_2h[h_indexes[1] - 1:h_indexes[0]:-1])

# Задача 6. Сжатие списка

# num_count = randint(5, 15)
# num_lst = [randint(0, 2) for _ in range(num_count)]
#
# print('Количество чисел в списке:', num_count, '\nСписок до сжатия:', num_lst)
# null_count = num_lst.count(0)
#
# for i in range(0, num_count):
#     if num_lst[i] == 0:
#         num_lst.remove(0)
#         num_lst.append(0)
#
# print('Промежуточный список с нулями в конце:', num_lst)
# print('Список после сжатия:', num_lst[:num_count-null_count:])

# Задача 7. Двумерный список

# num_lst = [[i + x for x in range(0, 12, 4)] for i in range(1, 5)]
# print(num_lst)

# Задача 8. Развлечение

# stick_count = randint(5, 20)
# throw_count = randint(1, 4)
# print('Количество палок:', stick_count, '\nКоличество бросков:', throw_count)
# stick_list = ['|' for _ in range(1, stick_count + 1)]
#
# for i in range(1, throw_count + 1):
#     right_i = randint(1, len(stick_list))
#     left_i = right_i - randint(0, right_i - 1)
#     print('Бросок ' + str(i) + '. Сбиты палки с номера ' + str(left_i) + ' по номер ' + str(right_i) + '.')
#     downed_sticks_cnt = right_i - left_i + 1
#     downed_sticks_list = ['.' for _ in range(downed_sticks_cnt)]
#     stick_list[left_i - 1:right_i] = downed_sticks_list
#
#
# print('Результат:', end=' ')
# for i_sym in stick_list:
#     print(i_sym, end='')

# Задача 9. Список списков

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# Метод 1 (мой)
# final_list = [j[y] for j in (i[x] for i in nice_list for x in range(3)) for y in range(3)]

# Метод 2 (из разбора дз)

# final_list = [digit for each_list in nice_list for each_list_2 in each_list for digit in each_list_2]
#
# print('Ответ:', final_list)

# Задача 10. Шифр Цезаря

text = make_random_text(words_to_random)
shift = randint(1, 32)
print('Сообщение:', text, '\nСдвиг:', shift)

# Метод 1 (мой)

# rus_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
#                 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# text_lst = list(text)

# letters_num_text = [rus_alphabet.index(i) if i in rus_alphabet else -1 for i in text_lst ]
#
# letters_num_text_shift = [i if i < 0 else (i + shift) % 33 for i in letters_num_text]
#
# text_encrypted_lst = [rus_alphabet[i] if i >= 0 else ' ' for i in letters_num_text_shift]
#
# final_text = ''
#
# for i in text_encrypted_lst:
#     final_text += i
#
# print('Зашифрованное сообщение:', final_text)

# Метод 2 (из разбора ДЗ)

rus_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def caesar_cipher(user_text, user_shift):
    char_list = [(rus_alphabet[(rus_alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in
                 user_text]
    text_encrypted = ''
    for i_char in char_list:
        text_encrypted += i_char
    return text_encrypted


text_encrypted = caesar_cipher(text, shift)
print('Зашифрованное сообщение:', text_encrypted)
