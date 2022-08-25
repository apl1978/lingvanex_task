import os
from itertools import product

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXTS_DIR_NAME = 'texts'
TEXTS_FILE_NAME = 'PythonTest.txt'
EN_FILE_NAME = 'English.txt'
RU_FILE_NAME = 'Russian.txt'

file_path = os.path.join(BASE_PATH, TEXTS_DIR_NAME, TEXTS_FILE_NAME)
file_en = os.path.join(BASE_PATH, TEXTS_DIR_NAME, EN_FILE_NAME)
file_ru = os.path.join(BASE_PATH, TEXTS_DIR_NAME, RU_FILE_NAME)


def delete_file_if_exists(file_path: str):
    if os.path.isfile(file_path):
        os.remove(file_path)


def write_to_file(data: str, file_path: str):
    with open(file_path, 'a', encoding='utf-8') as file_save:
        file_save.write(f'{data}\n')


def parse_file(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            first_char = line[0]
            if (not first_char == '#') and (not ord(first_char) == 10):
                my_list = line.strip().split('\t')
                for pair in product(my_list[0].split(';'), my_list[1].split(';')):
                    write_to_file(pair[0].strip(), file_en)
                    write_to_file(pair[1].strip(), file_ru)


if __name__ == '__main__':
    delete_file_if_exists(file_en)
    delete_file_if_exists(file_ru)
    parse_file(file_path)
