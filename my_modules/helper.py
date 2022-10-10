import pickle
import string
import random
from random import randint


def make_random_text_list(text_list_type, cnt):
    with open('./data/text_lists/' + text_list_type, 'rb') as f:
        text_list_for_random = pickle.load(f)
    random_text_list = []
    for _ in range(0, cnt):
        word = text_list_for_random[randint(0, len(text_list_for_random) - 1)]
        random_text_list.append(word)
    return random_text_list


def make_random_letters_sequence():
    word = ''
    letters_count = randint(1, 8)
    for _ in range(letters_count):
        letter = random.choice(string.ascii_lowercase)
        word += letter
    return word
