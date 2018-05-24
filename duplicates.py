import os
from collections import Counter, defaultdict
import json
import sys


def find_all_filenames(dirname):
    all_filenames_dict = defaultdict(list)
    for directory, dirs, filenames in os.walk(dirname):
        for filename in filenames:
            path = os.path.join(directory, filename)
            size_of_file = os.path.getsize(path)
            all_filenames_dict[(filename, size_of_file)].append(path)
    return all_filenames_dict


def get_similar_filenames(all_filenames):
    duplicate_filenames = {}
    for file_info, path in all_filenames.items():
        if len(path) > 1:
            duplicate_filenames.update({file_info[0]: path})
    return json.dumps(duplicate_filenames, indent=2, ensure_ascii=False)


def print_similar_files(kind_of_files, duplicate_filenames):
    print(kind_of_files, duplicate_filenames)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dirname = sys.argv[1]
    else:
        exit("Не выбран каталог")
    if os.path.isfile(dirname):
        exit("Ошибка! Передан файл, а не каталог")
    all_filenames = find_all_filenames(dirname)
    duplicate_filenames = get_similar_filenames(all_filenames)
    print_similar_files("Найденные дубликаты:", duplicate_filenames)

