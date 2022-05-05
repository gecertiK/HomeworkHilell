# 1. Дано целое число (int). Определить сколько нулей в этом числе.

my_number = 1234567000765432199900
my_number_str = str(my_number)
result = my_number_str.count("0")
print(result)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

number = 1002000
number_str = str(number)
print(len(number_str) - len(number_str.rstrip('0')))

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list1 = ["a", 3, 5, 7, 9, 11, 45, "b"]
my_list2 = [2, 4, 6, "abc", 10, 12]
my_result = my_list1[::2] + my_list2[1::2]
print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 2, 3, 4]
new_list = my_list[1:] + [my_list[0]]
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4]
return_value = my_list.pop(0)
my_list.append(return_value)
print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

some_txt = "43 больше чем 34 но меньше чем 56"
digit_txt = [int(digit) for digit in some_txt.split() if digit.isdigit()]
print(sum(digit_txt))

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit, r_limit = "o", "g"
l_index = my_str.find(l_limit) + 1
r_index = my_str.rfind(r_limit)
sub_str = my_str[l_index: r_index]
sub_str = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]
print(sub_str)


# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str = "abcd"
box = ""
my_list = []
for strings in my_str:
    box += strings
    if len(box) == 2:
        my_list.append(box)
        box = ""
if len(box) == 1:
    box += "_"
    my_list.append(box)
print(my_list)

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0
for index in range(1, len(my_list) - 1):
    if my_list[index] > sum([my_list[index - 1], my_list[index + 1]]):
        counter += 1
print(counter)

# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list = [1, 2, 3, "11", "22", 33]
new_my_list = []
for strings in my_list:
    if isinstance(strings, str):
        new_my_list.append(strings)
print(new_my_list)

new_my_list = [strings for strings in my_list if isinstance(strings, str)]
print(new_my_list)

# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str = "asbbasdf"
new_my_str = []
for strings in set(my_str):
    if my_str.count(strings) == 1:
        new_my_str.append(strings)
new_my_str = [txt for txt in my_str if my_str.count(txt) == 1]
print(new_my_str)

# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str = "qaqsdfrty"
my_str1 = "qqwerty"
my_new_list = set(my_str).intersection(my_str1)
print(my_new_list)

# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str = "aaaasdf1"
my_str1 = "asdfff2"
my_str_list = []
my_new_list = set(my_str).intersection(my_str1)
for strings in my_new_list:
    if my_str.count(strings) == 1 and my_str1.count(strings) == 1:
        my_str_list.append(strings)
print(my_str_list)