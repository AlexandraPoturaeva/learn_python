# 8.2 Рекурсия
import pickle
import random
import copy


# Задача 1. Challenge

# user_num = 5  # random.randint(2, 1000)
#
#
# def factorial(number):
#     if number == 1:
#         return 1
#     return number * factorial(number - 1)
#
#
# print(f'Факториал числа {user_num} равен {factorial(user_num)}')

# Задача 2. Степень числа


# def power(a, n):
#     if n == 1:
#         return a
#     return a * power(a, n - 1)
#
#
# float_num = random.uniform(1, 100)
# int_num = random.randint(2, 10)
#
# print(float_num, '**', int_num, '=', power(float_num, int_num))

# Задача 3. Поиск элемента

# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def find_key(user_dict, key):
#     if key in user_dict:
#         return user_dict[key]
#
#     for sub_struct in user_dict.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key)
#             if result:
#                 break
#
#     else:
#         result = None
#
#     return result
#
#
# def return_all_keys(user_dict):
#     tpl = tuple(user_dict.keys())
#
#     for sub_struct in user_dict.values():
#         if isinstance(sub_struct, dict):
#             tpl += return_all_keys(sub_struct)
#
#     return tpl
#
#
# user_keys = return_all_keys(site) + ('abc', 'hdsfk', 'hfsk')
#
# for key in user_keys:
#     value = find_key(site, key)
#     if value:
#         print(f'Значение для ключа "{key}": {value}')
#     else:
#         print(f'Ключа "{key}" в структуре сайта нет.')

# 8.4 Передача изменяемых и неизменяемых данных в функцию

# Задача 1. Ошибка

# def change_dict(dct):
#     num = random.randint(1, 100)
#
#     for i_key, i_value in dct.items():
#
#         if isinstance(i_value, list):
#             i_value.append(num)
#
#         if isinstance(i_value, dict):
#             i_value[num] = i_key
#
#         if isinstance(i_value, set):
#             i_value.add(num)
#
#
# nums_list = [1, 2, 3]
#
# some_dict = {1: 'text', 2: 'another text'}
#
# uniq_nums = {1, 2, 3}
#
# common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}


# Метод 1

# common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
# change_dict(common_dict)
# print(common_dict)

# Метод 2

# common_dict_2 = copy.deepcopy(common_dict)
# change_dict(common_dict_2)
#
# print(common_dict_2)
# print(nums_list, some_dict, uniq_nums)

# Задача 2. Непонятно!

# data_for_random = [[1, 2, 3], (1, 2, 3), {1, 2, 3}, 'привет', 125, {1: 'а', 2: 'б', 3: 'в'}]
#
#
# def get_object_info(data):
#     object_type = type(data)
#     object_id = id(data)
#     if isinstance(data, (set, dict, list)):
#         feature = 'mutable'
#     else:
#         feature = 'immutable'
#     return object_type, object_id, feature
#
# print(get_object_info(random.choice(data_for_random)))

# 8.6 Именованные аргументы и значения по умолчанию

# questions = ['Вы действительно хотите выйти?', 'Удалить файл?', 'Записать файл?']
#
# def ask_user(question,
#              complaint= 'Неверный ввод. Пожалуйста, введите да или нет',
#              retries=4):
#     while True:
#         print(question)
#         answer = random.choice(['да', 'нет', 'не знаю'])
#         print(answer)
#         match answer:
#             case 'да':
#                 return 1
#             case 'нет':
#                 return 0
#         retries -= 1
#         if retries == 0:
#             print('Количество попыток истекло')
#             break
#         print(complaint)
#         print('Осталось попыток:', retries)
#
# ask_user(random.choice(questions))
# ask_user(random.choice(questions))
# ask_user(random.choice(questions))

# Задача 2. Накопление значений

# def add_num(num, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(num)
#     print(lst)
#
# add_num(5)
# add_num(10)
# add_num(15)

# Задача 3. Помощь другу

# def create_dict(data, template=None):
#     if template is None:
#         template = dict()
#
#     if isinstance(data, dict):
#         return data
#     else:
#         template[data] = data
#         return template
#
#
# def data_preparation(old_list):
#     new_list = []
#
#     for i_element in old_list:
#         if isinstance(i_element, (dict, int, float, str)):
#             new_list.append(create_dict(i_element))
#
#     return new_list
#
#
# data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
#
# data = data_preparation(data)
#
# print(data)

# 8.8 Практическая работа
# Challenge 2

# def print_num(n):
#     if n != 1:
#         print_num(n-1)
#     print(n)
#
#
# print_num(10)

# Задача 2. Свой zip 2

# user_string = 'abcd'
# user_dict = {(1, 2): 'a', 5: 'a'}
# user_list = ['d', 'e', 'f']
# user_tuple = (10, 20, 30, 40)

# Метод 1
# def zip_data(*args):
#     length = min((len(arg) for arg in args))
#     result = [
#         tuple(
#             list(arg)[i]
#             for arg in args
#           )
#         for i in range(length)
#     ]
#     return result


# Метод 2
# def zip_data(*args):
#     length = min((len(arg) for arg in args))
#     result = [
#         tuple(
#             struct[i]
#             for struct in map(list, args)
#           )
#         for i in range(length)
#     ]
#     return result
#
# final = zip_data(user_dict, user_list, user_tuple, user_string)
#
# print(final)

# Задача 3. Ряд Фибоначчи

# num_pos = 40 # random.randint(0, 1000)

# Метод 1

# def find_in_Fib_seq(pos_to_find, cur_pos=0, num_1=0, num_2=1):
#     if pos_to_find == cur_pos:
#         return num_1
#     else:
#         next_num = num_1 + num_2
#         cur_pos += 1
#         return find_in_Fib_seq(pos_to_find, cur_pos=cur_pos, num_1=num_2, num_2=next_num)
#
# print('Позиция:', num_pos, 'Число:', find_in_Fib_seq(num_pos))

# Метод 2

# def Fibonacci(pos):
#     if pos <= 1:
#         return pos
#     return Fibonacci(pos-1) + Fibonacci(pos-2)
#
# print(Fibonacci(num_pos))

# Задача 4. Поиск элемента 2

# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def find_key(user_dict, key, depth=3):
#     if depth == 0:
#         return None
#
#     if key in user_dict:
#         return user_dict[key]
#
#     for sub_struct in user_dict.values():
#         if isinstance(sub_struct, dict):
#             return find_key(sub_struct, key, depth=depth - 1)
#
#
# def return_all_keys(user_dict):
#     tpl = tuple(user_dict.keys())
#
#     for sub_struct in user_dict.values():
#         if isinstance(sub_struct, dict):
#             tpl += return_all_keys(sub_struct)
#
#     return tpl
#
#
# user_keys = return_all_keys(site) + ('abc', 'hdsfk', 'hfsk')
# user_answers = ['y', 'n']
#
# for key in user_keys:
#     print('Искомый ключ:', key)
#     answer = random.choice(user_answers)
#     print('Хотите ввести максимальную глубину? Y/N:', answer)
#
#     if answer == 'y':
#         depth = random.randint(1, 3)
#         print('Глубина:', depth)
#         value = find_key(site, key, depth)
#     else:
#         value = find_key(site, key)
#
#     if value:
#         print(f'Значение для ключа "{key}": {value}')
#     else:
#         print(None)

# Задача 5. Ускоряем работу функции

# factorial_dict = dict()
#
# def calculating_math_func(data, factorial_dict=factorial_dict):
#     if data in factorial_dict.keys():
#         result = factorial_dict[data]
#     else:
#         result = 1
#         for index in range(1, data + 1):
#             result *= index
#         factorial_dict[data] = result
#     result /= data ** 3
#     result = result ** 10
#     return result
#
# print(calculating_math_func(5))
# print(calculating_math_func(5))

# Задача 6. Глубокое копирование
# with open('C:/code/Skillbox/data/text_lists/fruits', 'rb') as f:
#     product_list = pickle.load(f)
#
#
# def print_site_structures(count=None, sites_text=None):
#     if sites_text is None:
#         sites_text = ''
#
#     if count == 0:
#         return sites_text
#     else:
#         product = random.choice(product_list)
#         print('Название продукта для нового сайта:', product)
#         structure_text = "\nСайт для " + product + ":\n" \
#                          "site = {\n" \
#                          "    'html' : {\n" \
#                          "        'head': {\n" \
#                          "            'title': 'Куплю/продам " + product + " недорого\n" \
#                          "        },\n" \
#                          "        'body': {\n" \
#                          "            'h2': 'У нас самая низкая цена на " + product + ",\n" \
#                          "            'div': 'Купить',\n" \
#                          "            'p': ‘Продать'\n" \
#                          "        }\n" \
#                          "    }\n" \
#                          "}\n"
#         count -= 1
#         sites_text += structure_text
#         print(sites_text)
#         return print_site_structures(count=count, sites_text = sites_text)
#
#
# count = random.randint(1, 10)
# print('Количество сайтов:', count)
# print_site_structures(count)

# Задача 7. Продвинутая функция sum


# def sum_improved(*args, summ=0):
#     for arg in args:
#         if isinstance(arg, (float, int)):
#             summ += arg
#         elif isinstance(arg, (list, tuple, set)):
#             for elem in arg:
#                 summ = sum_improved(elem, summ=summ)
#     return summ
#
#
# print(sum_improved([[1, 2, [3]], [1], 3]))
# print(sum_improved(1, 2, 3, 4, 5))
# print(sum_improved(1))

# Задача 8. Список списков 2

# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
#
#
# def unfold_list(data, result_list=None):
#     if result_list is None:
#         result_list = list()
#
#     if isinstance(data, list):
#         for elem in data:
#             result_list = unfold_list(elem, result_list=result_list)
#     else:
#         result_list.append(data)
#
#     return result_list
#
#
# print(unfold_list(nice_list))

# Задача 9. Ханойские башни


def hanoy(d, from_stick=1, to_stick=3, buf_stick=2):
    if d == 0:
        return
    else:
        hanoy(d - 1, from_stick, buf_stick, to_stick)
        print(f'Переложить диск {d} со стержня номер {from_stick} на стержень номер {to_stick}')
        hanoy(d - 1, buf_stick, to_stick, from_stick)


hanoy(4)
