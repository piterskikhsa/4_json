import json
import os
from pprint import pprint


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='UTF-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    file_path = input("ВВедите имя файла: ")
    json_content = load_json_data(file_path)
    if json_content:
        pretty_print_json(json_content)
