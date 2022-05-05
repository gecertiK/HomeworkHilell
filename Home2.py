# 1) ###########################################################
value = 55
new_value = value / 2 if value < 100 else -value
print(new_value)
# 2) ###########################################################
value = 148
new_value = 1 if value < 100  else "0"
print(new_value)
# 3) ###########################################################
value = 23
new_value = value = True if value < 100  else False
print(new_value)
# 4) ###########################################################
my_str = "qwe"
index_len = 5
result = my_str * 2 if len(my_str) < index_len else my_str
print(result)
# 5) ###########################################################
my_str = "qwertw"
index_len = 5
result = my_str + my_str[::-1] if len(my_str) < index_len else my_str
print(result)
# 6) ###########################################################
print("Добпо пожаловать в калькулятор.")
while True:
    try:
        input_case = int(input("Выбери тип операции от 1 до 6:\n1 +\n2 -\n3 *\n4 /\n5 %\n6 //\n"))
        if 1 <= input_case <= 6:
            value_1 = int(input("Введи первое число:"))
            value_2 = int(input("Введи второе число:"))
            if input_case == 1:
                result = value_1 + value_2
            elif input_case == 2:
                result = value_1 - value_2
            elif input_case == 3:
                result = value_1 * value_2
            elif input_case == 4:
                result = value_1 / value_2
            elif input_case == 5:
                result = value_1 % value_2
            elif input_case == 6:
                result = value_1 // value_2
            print(result)
            print("Продолжить вычисления?")
            question = input("Да или Нет\n")
            if question != "Да":
                print("Завершение")
                break
    except ZeroDivisionError:
        print("На 0 делить нельзя")
    except ValueError:
        print("Тебе следует ввести число")