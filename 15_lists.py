# 15.1 Списки и их инициализация

# Задача 1. Таблица степеней
from random import randint

#
# numbers = [3, 7, 5]
# again = 1
#
# while again == 1:
#     #number = int(input('Новое число: '))
#     number = randint(1, 1000)
#     print('Новое число:', number)
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#     for i in numbers:
#         print(i ** 2, i ** 3, i ** 4)
#     print()
#     again = randint(0, 1)
#     print('Добавить ещё число? (0 - нет, 1 - да)', again)


# Задача 2. Очень простая задача

# numbers = []
#
# for i in range(0, 101):
#     numbers.append(i)
#
# print(numbers)

# Задача 3. Контроль

# Метод 1

#
# workers_count = randint(10, 30)
# print('Кол-во сотрудников в офисе:', workers_count)
#
# workers_ID = []
#
# for num in range(1, workers_count + 1):
#     id = randint(1, 30)
#     print(str(num) + ') ID сотрудника: ' + str(id))
#     workers_ID.append(id)
#
# worker_ID_find = randint(1, 30)
# print('Какой ID ищем?', worker_ID_find)
#
# result = 0
# for id in workers_ID:
#     if worker_ID_find == id:
#         result = 1
#
# if result == 1:
#     print('Сотрудник на месте')
# else:
#     print('Сотрудник не работает!')

# Метод 2

# workers_count = randint(10, 30)
# print('Кол-во сотрудников в офисе:', workers_count)
#
# workers_ID = []
#
# for num in range(1, workers_count + 1):
#     id = randint(1, 30)
#     print(str(num) + ') ID сотрудника: ' + str(id))
#     workers_ID.append(id)
#
# worker_ID_find = randint(1, 30)
# print('Какой ID ищем?', worker_ID_find)

# try:
#     result = workers_ID.index(worker_ID_find)
#     if result:
#         print('Сотрудник на месте')
# except ValueError:
#     print('Сотрудник не работает!')

# if worker_ID_find in workers_ID:
#     print('Сотрудник на месте')
# else:
#     print('Сотрудник не работает!')

# 15.2 Индексы. Работа с элементами списка

# Задача 1. Гугл

# Метод 1

# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# maximum = 0
#
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#
# minimum = maximum
#
# for i in nums_list:
#     if minimum >= i:
#         minimum = i
#
#
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)

# Метод 2

# nums_list = []
# N = randint(1, 20)
# print('Кол-во чисел в списке: ')
#
# for _ in range(N):
#     num = randint(-100, 100)
#     print('Очередное число:', num)
#     nums_list.append(num)
#
# maximum = nums_list[0]
# minimum = nums_list[0]
#
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#     if minimum > i:
#         minimum = i
#
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)

# Метод 3

# nums_list = []
# N = randint(1, 20)
# print('Кол-во чисел в списке: ')
#
# for _ in range(N):
#     num = randint(-100, 100)
#     print('Очередное число:', num)
#     nums_list.append(num)
#
# print('Максимальное число в списке:', max(nums_list))
# print('Минимальное число в списке:', min(nums_list))

# Задача 2. Кратность

# nums_count = randint(3, 10)
# print('Кол-во чисел в списке:', nums_count)
# numbers = []
# numbers_indexes_sum = 0
#
# for i in range(1, nums_count + 1):
#     number = randint(1, 10000)
#     print('Число ' + str(i) + ': ', number)
#     numbers.append(number)
# print('')
#
# divisor = randint(2, 10)
# print('Делитель:', divisor)
# print('')
#
# for i_num in range(nums_count):
#     if numbers[i_num] % divisor == 0:
#         print('Индекс числа ' + str(numbers[i_num]) + ': ' +  str(i_num))
#         numbers_indexes_sum += i_num
#
# if numbers_indexes_sum > 0:
#     print('Сумма индексов:', numbers_indexes_sum)
# else:
#     print('Все эти числа не делятся без остатка на', divisor)

# Задача 3. Собачьи бега

# dogs_count = randint(5, 20)
# print('В бегах участвует собак:', dogs_count)
# dog_scores_list = []
#
# print('Очки:')
#
# for i in range(1, dogs_count + 1):
#     dog_scores = randint(1, 100)
#     print(str(i) + ' - ', dog_scores)
#     dog_scores_list.append(dog_scores)
#
# maximum = max(dog_scores_list)
# minimum = min(dog_scores_list)
#
# print('Максимальное количество очков:', maximum)
# print('Минимальное количество очков:', minimum)
# print('')
#
# difference = maximum - minimum
#
# # for i in range(dogs_count):
# #     if dog_scores_list[i] == maximum:
# #         dog_scores_list[i] -= difference
# #     elif dog_scores_list[i] == minimum:
# #         dog_scores_list[i] += difference
#
# dog_scores_list[dog_scores_list.index(maximum)] -= (difference + 1)
# dog_scores_list[dog_scores_list.index(minimum)] += difference
# dog_scores_list[dog_scores_list.index(minimum - 1)] += 1
#
# print('Исправленное распределение очков:')
# for i in range(1, dogs_count + 1):
#     print(str(i) + ' - ', dog_scores_list[i - 1])

# 15.3 Списки: работа со строками

# Задача 1. Текстовый редактор: возвращение

# # text = input('Введите строку: ')
#
import string
import random

#
# words_count = randint(2, 10)
#
# words_list = []
# word = ''
#
# for _ in range(words_count):
#     letters_count = randint(3, 7)
#     for _ in range(letters_count):
#         letter = random.choice(string.ascii_letters)
#         word += letter
#     words_list.append(word)
#     word = ''
#
# # print(words_list)
#
# text = words_list[0]
#
# for i in range(1, words_count):
#     text += (': ' + words_list[i])
#
# print('Введённая строка:', text)
#
# text_list = list(text)
# replacements_indexes = []
# sym_count = -1
# replacements_count = 0
#
# for sym in text_list:
#     sym_count += 1
#     if sym == ':':
#         replacements_indexes.append(sym_count)
#         replacements_count += 1
# # print(replacements_indexes)
#
# print('Исправленная строка: ', end='')
#
# for i in replacements_indexes:
#     text_list[i] = ';'
#
# for sym in text_list:
#     print(sym, end='')
#
# print('\nКоличество замен:', replacements_count)

# Задача 2. Соседи

# text = ''
# symbols_count = randint(4, 10)
#
# for _ in range(symbols_count):
#     letter = random.choice(string.ascii_letters)
#     text += letter
#
# print('Введённая строка:', text)
#
# # text = input('Введите строку: ')
#
# # sym_number = int(input('Номер символа: '))
#
# sym_number = randint(2, symbols_count - 1)
#
# print('Номер символа:', sym_number)
#
# text_list = list(text)
#
# left_sym = text_list[sym_number - 2]
# right_sym = text_list[sym_number]
# find_sym = text_list[sym_number - 1]
#
# print('Символ слева:', left_sym)
# print('Символ справа:', right_sym)
#
# #if (left_sym == find_sym and right_sym != find_sym) or (right_sym == find_sym and left_sym != find_sym):
# if (left_sym == find_sym != right_sym) or (right_sym == find_sym != left_sym):
#     print('Есть ровно один такой же символ')
# #elif left_sym == find_sym and right_sym == find_sym:
# elif left_sym == find_sym == right_sym:
#     print('Есть два таких же символа')
# else:
#     print('Таких же символов нет')

# Задача 3. Улучшенная лингвистика

# words_to_find_list = []
# words_count = [0, 0, 0]
#
# for i in range(1, 4):
#     word = input('Введите ' + str(i) + '-е слово: ')
#     words_to_find_list.append(word)
#
# print('Введите текст по словам:')
# text = input('Слово из текста: ')
# while text != 'end':
#     for i in range(3):
#         if text == words_to_find_list[i]:
#             words_count[i] += 1
#     text = input('Слово из текста: ')
#
# print('\nПодсчёт слов в тексте:')
# for i in range(3):
#     print(words_to_find_list[i] + ': ' + str(words_count[i]))

# Метод 2

words_to_random = ['цельность', 'опоражнивание', 'сотоварищ', 'закаменелость', 'гунтер', 'камышит',
                   'рационалистичность', 'классная', 'оладья', 'хроматин', 'допустимость', 'разряжённость', 'красавица',
                   'шасла', 'обыкновение', 'норд-норд-вест', 'зашлаковка', 'антивитамин', 'обсолка', 'сакс',
                   'показательность', 'оркестрование', 'бойлерная', 'обращаемость', 'нормировщица', 'бездельничание',
                   'буревал', 'вискозиметр', 'казашка', 'инерция', 'водобой', 'сиротство', 'муссирование', 'шёпот',
                   'оправдание', 'ушкуй', 'гной', 'цыкание', 'призванный', 'прусик', 'озимость', 'баобаб', 'оттоманка',
                   'улем', 'линолеумщик', 'стенописец', 'пластование', 'рокфор', 'модельщик', 'омёт',
                   'либеральничество', 'подзащитный', 'докалка', 'бракосочетание', 'флюсование', 'бадминтонист',
                   'прижимание', 'триединство', 'мокшанка', 'ночёвка', 'персона', 'возмутительность', 'мензурка',
                   'проколка', 'шитьё', 'найтов', 'расплывчатость', 'арбитраж', 'ритуал', 'гемоглобин',
                   'примораживание', 'полуфабрикат', 'эгоист', 'расстреливание', 'стеблевание', 'протагонистка',
                   'теленомус', 'вулканолог', 'пролетаризирование', 'анероид', 'прокапчивание', 'планшайба', 'солерос',
                   'отпускница', 'пессимистичность', 'маца', 'хрустение', 'жизнеустройство', 'переколка', 'убежище',
                   'психофизиология', 'ярь-медянка', 'реставратор', 'велюр', 'портрет', 'огурец', 'граб',
                   'одутловатость', 'девочка', 'мозаичист', 'лужичанка', 'недодержка', 'серб', 'своевольная',
                   'добровольность', 'позеленение', 'хлыстовщина', 'пересыхание', 'лаконичность', 'пырник',
                   'проблематичность', 'сваривание', 'нить', 'кожеед', 'вспыхивание', 'труппа', 'оттяжка', 'праща',
                   'нематериальность', 'фитопланктон', 'вылов', 'взаимность', 'комара', 'типичное', 'тождественность',
                   'бизон', 'прилаживание', 'параметрит', 'густолесье', 'зарница', 'местообитание', 'обрывистость',
                   'сиповатость', 'бомбардирование', 'застопоривание', 'подготовительница', 'вруб', 'светолюбивость',
                   'хамит', 'перескабливание', 'половщик', 'псевдоучёность', 'пересечённость', 'оккупация', 'плющильня',
                   'переизбрание', 'обмазка', 'жестикулирование', 'лебяжина', 'божественность', 'независимость', 'шваб',
                   'предпочтительность', 'дезертирство', 'суеверие', 'тундрянка', 'чеченка', 'сочевичник', 'киянка',
                   'пермячка', 'бронекатер', 'хлебопечение', 'воронение', 'фал', 'песня', 'федералист', 'прокус',
                   'гунн', 'каландр', 'отдалённость', 'электропилка', 'кочевница', 'садовница', 'нарастание',
                   'отметина', 'персонаж', 'бездумность', 'исцелительница', 'мрачность', 'супоросость', 'цевьё',
                   'клирик', 'выщипывание', 'прививка', 'чересседельник', 'окольничий', 'фильтрат', 'обитательница',
                   'добивание', 'ламаркизм', 'гонт', 'академгородок', 'расшатывание', 'судопроизводство',
                   'обездоленность', 'финно-угроведение', 'стругание', 'захоронение', 'фронт', 'угольщик',
                   ]

words_to_find_list = []
text = []

print('Список слов для подсчёта их частоты употребления в тексте:')

for i in range(1, 4):
    word = words_to_random[randint(0, len(words_to_random) - 1)]
    print(str(i) + ') ' + word)
    words_to_find_list.append(word)

print('\nТекст:')

for i in range(3, 20):
    word = words_to_random[randint(0, len(words_to_random) - 1)]
    print(word, end=' ')
    text.append(word)

print('\n\nПодсчёт слов в тексте: ')

my_dict = {i: text.count(i) for i in words_to_find_list}

for key, value in my_dict.items():
    print(key + ': ' + str(value))


# 15.6 Практическая работа

# Задача 1. Генерация списка

# number = randint(1, 100)
# print('Число:', number)
# odd_numbers_list = []
#
# for num in range(1, number + 1, 2):
#     odd_numbers_list.append(num)
#
# print('Список из нечётных чисел от 1 до', number, ':', odd_numbers_list)

# Задача 2. Турнир

# participant_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
#
# participant_count = len(participant_list)
#
# first_day_list = []
#
# for i in range(0, participant_count - 1, 2):
#     first_day_list.append(participant_list[i])
#
# print('Первый день:', first_day_list)

# Задача 3. Клетки

# cell_number = randint(1, 10)
# print('Количество клеток:', cell_number)
# cell_efficiency_list = []
# wrong_list = []
#
# for cell in range(1, cell_number + 1):
#     cell_efficiency = randint(0, 10)
#     print('Эффективность', cell, 'клетки:', cell_efficiency)
#     cell_efficiency_list.append(cell_efficiency)
#
# #print(cell_efficiency_list)
#
# for i in range(1, cell_number + 1):
#     if cell_efficiency_list[i - 1] < i:
#         wrong_list.append(cell_efficiency_list[i - 1])
#
# print('Неподходящие значения:')
#
# for num in wrong_list:
#     print(num, end= ' ')

# Задача 4. Видеокарты

# Метод 1

# amount = randint(1, 20)
# print('Количество видеокарт:', amount)
# model_list = []
# model_list_new = []
#
# for i in range(1, amount + 1):
#     model = random.randrange(1000, 9999, 10)
#     model_list.append(model)
#     print(i, ':', model)
#
# print('Старый список видеокарт:', model_list)
#
# new_model = max(model_list)
#
# for i in range(amount):
#     if model_list[i] != new_model:
#         model_list_new.append(model_list[i])
#
# print('Новый список видеокарт:', model_list_new)

# Метод 2

# amount = randint(1, 20)
# print('Количество видеокарт:', amount)
# model_list = []
#
# for i in range(1, amount + 1):
#     model = random.randrange(1000, 9999, 10)
#     model_list.append(model)
#     print(i, ':', model)
#
# print('Старый список видеокарт:', model_list)
#
# new_model = max(model_list)
#
# model_list.remove(new_model)
#
# print('Новый список видеокарт:', model_list)

# Задача 5. Кино

# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
#          'Отступники', 'Деревня']
#
# favor_films = []
# film_avail = 0
#
# amount_fav_films = int(input('Сколько фильмов хотите добавить? '))
#
# for i in range(amount_fav_films):
#     favor_film = input('Введите название фильма: ')
#     for film in films:
#         if favor_film == film:
#             film_avail = 1
#             break
#     if film_avail == 1:
#         favor_films.append(favor_film)
#     if film_avail == 0:
#         print('Ошибка: фильма', favor_film, 'у нас нет :(')
#     film_avail = 0
#
# print('')
#
# print('Ваш список любимых фильмов: ', end='')
# print(favor_films[0], end='')
#
# for i in range(1, len(favor_films)):
#     print(',', favor_films[i], end='')

# Задача 6. Анализ слова

# word = input('Введите слово: ')
#
# letters_list = list(word)
# letter_times = 0
# unique = 0
#
# for letter in letters_list:
#     find_letter = letter
#     for letter in letters_list:
#         if letter == find_letter:
#             letter_times += 1
#     if letter_times == 1:
#         unique += 1
#     letter_times = 0
#
# print('Количество уникальных букв:', unique)

# Задача 7. Контейнеры

# cont_amount = randint(1, 20)
# min_weight = randint(50, 100)
# cont_weight_list = [min_weight]
#
# print('Количество контейнеров: ', cont_amount)
# print('Вес контейнеров:')
# print('1 -', min_weight)
#
# for i in range(2, cont_amount + 1):
#     cont_weight = min_weight + randint(1, 10)
#     cont_weight_list.append(cont_weight)
#     print(i, '-', cont_weight)
#     min_weight = cont_weight
#
# new_cont_weight = randint(1, 200)
# new_cont_num = 0
# print('Вес нового контейнера:', new_cont_weight)
#
# for i in range(cont_amount):
#     if new_cont_weight < cont_weight_list[i]:
#         new_cont_num = i + 1
#         break
#
# print('Номер нового контейнера:', new_cont_num)

# Задача 8. Бегущие цифры

# amount = randint(3, 10)
# # print(amount)
# numbers_list = []
# new_order_nums_list = []
#
# for i in range(amount):
#     number = randint(-10, 10)
#     numbers_list.append(number)
#
# print('Изначальный список:', numbers_list)
#
# shift = randint(1, amount - 1)
# print('Сдвиг:', shift)
#
# for i in range(-shift, amount - shift):
#     number = numbers_list[i]
#     new_order_nums_list.append(number)
#
# print('Сдвинутый список:', new_order_nums_list)

# Задача 9. Анализ слова 2
