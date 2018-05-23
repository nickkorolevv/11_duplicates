import os
from collections import Counter


def get_input():
    dirname = input("Введите путь\n")
    return dirname


def get_similar_dirs(dirname):
    similar_dirs_buffer = []
    all_files = os.walk(dirname)
    for dir_items in list(zip(*all_files)):
        pass
    for every_item in dir_items:
        for items in every_item:
            similar_dirs_buffer.append(items)
    similar_dirs = Counter(similar_dirs_buffer)
    return similar_dirs.most_common()


def find_all_files(dirname):
    all_files_buffer = []
    for directory, dirs, files in os.walk(dirname):
        for file in files:
            path = os.path.join(directory, file)
            all_files_buffer.append(path)
    return all_files_buffer


def print_similar_files(files, all_files):
    link_buffer = []
    size_buffer = []
    for link_item in files:
        for dir_item in all_files:
            if link_item[0] in dir_item:
                size_of_file = os.path.getsize(dir_item)
                link_buffer.append(dir_item)
                size_buffer.append(size_of_file)
        if link_item[1] == 1:
            break
    for buffer_index, link in enumerate(link_buffer[:-2]):
        print(
            link,
            "Размер файла в байтах: {}"
            .format(size_buffer[buffer_index])
        )


if __name__ == "__main__":
    dirname = get_input()
    all_files = find_all_files(dirname)
    similar_files = get_similar_dirs(dirname)
    print_similar_files(similar_files, all_files)
