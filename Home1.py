try:
    calculator = "Калькулятор"
    print("Добпо пожаловать в", calculator, sep=" -- ", end="!\n")
    while True:
        input_case = int(input("Выбери тип операции от 1 до 6:\n1 +\n2 -\n3 *\n4 /\n5 %\n6 //\n"))
        if 1 <= input_case <= 6:
            break
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
except ZeroDivisionError:
    result = "На 0 делить нельзя"
except ValueError:
    result = "Тебе следует ввести число"
print(result)