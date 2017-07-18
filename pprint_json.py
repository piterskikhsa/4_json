import json
from pprint import pprint


def load_data(filepath):
    f = open(filepath, 'r', encoding='UTF-8')
    json_data = f.read()
    f.close()
    data = json.loads(json_data)
    return data


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    file_path = input("ВВедите имя файла: ")
    json_data = load_data(file_path)
    pretty_print_json(json_data)

