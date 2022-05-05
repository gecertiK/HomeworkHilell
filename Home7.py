# Для задания 1-7 за основу можете взять код из предідущих ДЗ.

# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

my_list = ["rty", "asd", "zxc", "fgh"]


def some_list(my_list):
    my_new_list = []
    for count, strings in enumerate(my_list):
        if count % 2 == 1:
            my_new_list.append(strings[::-1])
        else:
            my_new_list.append(strings)
    return my_new_list


sorted_list = some_list(my_list)
print(sorted_list)

# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

my_list = ["aty", "sda", "zxac", "afgah"]


def some_list(my_list):
    my_new_list = []
    for strings in my_list:
        if "a" in strings[0]:
            my_new_list.append(strings)
    return my_new_list


sorted_list = some_list(my_list)
print(sorted_list)

# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["bca", "sad", "zxc", "afgah"]


def some_list(my_list):
    my_new_list = []
    for strings in my_list:
        if "a" in strings:
            my_new_list.append(strings)
    return my_new_list


sorted_list = some_list(my_list)
print(sorted_list)

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

my_list = [1, 2, 3, "11", "22", 33]


def some_strigs(my_list):
    new_my_list = []
    for strings in my_list:
        if isinstance(strings, str):
            new_my_list.append(strings)
    return new_my_list


sorted_strigs = some_strigs(my_list)
print(sorted_strigs)

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

my_str = "asbbasdf"


def some_symb(my_str):
    new_my_str = []
    for strings in set(my_str):
        if my_str.count(strings) == 1:
            new_my_str.append(strings)
    return new_my_str


sorted_symb = some_symb(my_str)
print(sorted_symb)

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str = "qaqsdfrty"
my_str1 = "qqwerty"


def some_symb(my_str, my_str1):
    my_new_list = set(my_str).intersection(my_str1)
    return my_new_list


sorted_symb = some_symb(my_str, my_str1)
print(sorted_symb)

# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str = "aaaasdf1"
my_str1 = "asdfff1"


def some_symb(my_str, my_str1):
    my_str_list = []
    my_new_list = set(my_str).intersection(my_str1)
    for strings in my_new_list:
        if my_str.count(strings) == 1 and my_str1.count(strings) == 1:
            my_str_list.append(strings)
    return my_str_list


sorted_symb = some_symb(my_str, my_str1)
print(sorted_symb)

# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

import random, string

names = ["king", "miller", "kean", "asd", "qwds"]
domains = ["net", "com", "ua", "at", "ru"]


def gen_email(names, domains):
    random_name = random.choice(names)
    random_value = random.randint(100, 999)
    random_abc = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 7)))
    random_domain = random.choice(domains)
    return f"{random_name}.{random_value}@{random_abc}.{random_domain}"


email = gen_email(names, domains)
print(email)