# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list = ["rty", "asd", "zxc", "fgh"]
my_new_list = []
for count, strings in enumerate(my_list):
    if count % 2 == 0:
        my_new_list.append(strings[::-1])
    else:
        my_new_list.append(strings)
print(my_new_list)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ["aty", "sda", "zxac", "afgah"]
my_new_list = []
for strings in my_list:
    if "a" in strings[0]:
        my_new_list.append(strings)
print(my_new_list)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["bc", "sad", "zxc", "afgah"]
my_new_list = []
for strings in my_list:
    if "a" in strings:
        my_new_list.append(strings)
print(my_new_list)

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а)Создать список и поместить туда имя самого молодого человека.
# Если возраст совпадает - поместить все имена самых молодых.

persons = [{"name": "david", "age": 2}, {"name": "david1234", "age": 5}, {"name": "Johna", "age": 15},
           {"name": "alexander", "age": 2}]
name_max_len = persons[0]["age"]
max_names = []
for person in persons:
    if person["age"] < name_max_len:
        name_max_len = person["age"]
        max_names = [person["name"]]
    elif person["age"] == name_max_len:
        max_names.append(person["name"])
print(max_names)
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
persons = [{"name": "david", "age": 15}, {"name": "david1234", "age": 45}, {"name": "Johna", "age": 15},
           {"name": "alexander", "age": 25}]
name_max_len = persons[0]["name"]
max_names = []
for person in persons:
    if len(person["name"]) > len(name_max_len):
        name_max_len = person["name"]
        max_names = [person["name"]]
    elif len(person["name"]) == len(name_max_len):
        max_names.append(person["name"])
print(max_names)
# в)Посчитать среднее количество лет всех людей из начального списка.
persons = [{"name": "Jhn", "age": 15}, {"name": "Joha", "age": 45}, {"name": "Johna", "age": 15},
           {"name": "Jackaaa", "age": 25}]
name_list = []
for dictionary in persons:
    name_list.append(dictionary["age"])
    average = sum(name_list) / len(name_list)
print(average)

# 5) Даны два словаря my_dict_1 и my_dict_2.

my_dict_1 = {"product": "MacBook", "price": 32000, "brand": "Apple"}
my_dict_2 = {"product": "HP", "price": 15000}
my_dict_3 = {}
my_dict_4 = {}

# а) Создать список из ключей, которые есть в обоих словарях.
dict_key = list(set(my_dict_1).intersection(my_dict_2))
print(dict_key)
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
dict_key1 = list(my_dict_1.keys() - my_dict_2.keys())
print(dict_key1)
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
for key, value in my_dict_1.items():
    if key not in my_dict_2.keys():
        my_dict_3[key] = value
print(my_dict_3)
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
for key_1, value_1 in my_dict_1.items():
    if key_1 in my_dict_2.keys():
        my_dict_4[key_1] = [value_1, my_dict_2[key_1]]
    else:
        my_dict_4[key_1] = value_1
for key_2, value_2 in my_dict_2.items():
    if key_2 not in my_dict_1.keys():
        my_dict_4[key_2] = value_2
print(my_dict_4)