# Написать класс и реализовать его методы: (основа - ДЗ № 11)
import os

path = "home"


# 1. Инициализация класса с одним параметром - имя директории.


class NameOfDir:
    def __init__(self, path):
        self.path = path



# 2. Написать метод экземпляра класса, который создает атрибут экземпляра класса в ввиде словаря
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))

    def scan_folder(self):
        list_dir = os.listdir(self.path)
        name1 = []
        name2 = []
        for filename in list_dir:
            find_files = os.path.join(self.path, filename)
            if os.path.isfile(find_files):
                name1.append(find_files)
        for dirnames in list_dir:
            find_dir = os.path.join(self.path, dirnames)
            if os.path.isdir(find_dir):
                name2.append(find_dir)
        return {"filenames": name1, "dirnames": name2}




# 3. Написать метод экземпляра класса, которая получает булевое значение (True/False).
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.

    def sort_dict(self, folders, sort_ABC=True):
        for arr in folders.values():
            arr.sort()
            if not sort_ABC:
                arr.reverse()
        return folders


# 4. Написать метод экземпляра класса, которая получает строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.

    def add_file_dir(self, folders, name_str):
        if "." in name_str:
            folders["filenames"].append(name_str)
        else:
            folders["dirnames"].append(name_str)
        return folders




nameOfDir = NameOfDir("home")
folders = nameOfDir.scan_folder()
print(folders)

sort_folders = nameOfDir.sort_dict(folders, True)
print(sort_folders)

name_str = "qwe.txt"

sor_file_dir = nameOfDir.add_file_dir(folders, name_str)
print(sor_file_dir)