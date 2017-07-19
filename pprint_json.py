import json
import os



def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='UTF-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    file_path = input("ВВедите имя файла: ")
    json_content = load_json_data(file_path)
    if json_content:
        pretty_print_json(json_content)
    else:
        print('Данные не загружены, повторите попытку!')