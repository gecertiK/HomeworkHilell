# Все пункты сделать как отдельные функции и их вызовы.

# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# .net.biz.info.org.tel.travel.aero.pro.xxx.name.mobi
# и возвращает их в виде списка строк (названия возвращать без точки).

domains_txt = "/Users/gecert/PycharmProjects/domains.txt"


def domains_txt(domains_txt):
    with open(domains_txt, "r") as name:
        text = name.read()
        domen_name = text.replace(".", "").split("\n")
    return domen_name


domains_list = domains_name_txt(domains_txt)
print(domains_list)

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

names_txt = "/Users/gecert/PycharmProjects/names.txt"


def domains_names_txt(names_txt):
    with open(names_txt, "r") as name:
        surnames = [line.split('\t')[1] for line in name.readlines()]
    return surnames


surnames_list = domains_names_txt(names_txt)
print(surnames_list)

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]

authors_txt = "/Users/gecert/PycharmProjects/authors.txt"


def domains_authors_txt(authors_txt):
    with open(authors_txt, "r") as fileDates:
        arr = [{"data": line.split(" -")[0]} for line in fileDates.readlines() if len(line) > 0]
    return arr


arr_date = domains_authors_txt(authors_txt)
print(arr_date)

# def domains_name(authors_txt):
#     with open(authors_txt, "r") as name:
#         dates = [line.split(" -")[0] for line in name.readlines()]
#         arr = []
#         for data in dates:
#             arr.append({"data": data})
#     return arr