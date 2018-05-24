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
    similar_filenames = {}
    for keys, values in all_filenames.items():
        if len(values) > 1:
            similar_filenames.update({keys[0]: values})
    return json.dumps(similar_filenames, indent=2, ensure_ascii=False)


def print_similar_files(kind_of_files, similar_filenames):
    print(kind_of_files, similar_filenames)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dirname = sys.argv[1]
    else:
        exit("Не выбран файл")
    all_filenames = find_all_filenames(dirname)
    similar_filenames = get_similar_filenames(all_filenames)
    print_similar_files("Найденные дубликаты:", similar_filenames)
