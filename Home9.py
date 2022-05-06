# Все пункты являются частью одного задания, поэтому можно использовать функции несколько раз и не дублировать код.
# Если хотите, можете использовать значения по умолчанию и аннотацию типов.
#
# 1. Написать функцию, которая получает один параметр - имя директории и возвращает словарь вида
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
import os

path = "home"



def scan_folder(path):
    list_dir = os.listdir(path)
    name1 = []
    name2 = []
    for filename in list_dir:
        find_files = os.path.join(path, filename)
        if os.path.isfile(find_files):
            name1.append(find_files)
    for dirnames in list_dir:
        find_dir = os.path.join(path, dirnames)
        if os.path.isdir(find_dir):
            name2.append(find_dir)
    return {"filenames": name1, "dirnames": name2}


folders = scan_folder(path)
print(folders)


# 2. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1
# и булевое значение (True/False) - можно сделать параметром по умолчанию.
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.

def sort_dict(folders, sort_ABC=True):
    for arr in folders.values():
        arr.sort()
        if not sort_ABC:
            arr.reverse()
    return folders


sort_folders = sort_dict(folders, False)
print(sort_folders)

# 3. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.
name_str = "qwe.txt"
def add_file_dir(folders, name_str):
    if "." in name_str:
        folders["filenames"].append(name_str)
    else:
        folders["dirnames"].append(name_str)
    return folders
sor_file_dir = add_file_dir(folders, name_str)
print(sor_file_dir)
