while True:
    print("Привет! Это простой калькулятор. \nДоступные операции: +, -")
    oparation = input("Выберите операцию: ")

    while oparation not in ("+", "-"):
        print("Недопустимая операция. Пожалуйста, введите только '+' или '-'.")
        oparation = input("Выберите операцию: ")

    first_num = float(input("Введите первое число: "))
    second_num = float(input("Введите второе число: "))

    if oparation == "+":
        result = first_num + second_num
    else:
        result = first_num - second_num

    print("Ответ:", result)

    restart = input("Хотите ли Вы продолжить? (да/нет): ")
    while restart.lower() not in ("да", "нет"):
        print("Недопустимое значение. Пожалуйста, введите только 'да' или 'нет'")
        restart = input("Хотите ли Вы продолжить? (да/нет): ")
    if restart.lower() != "да":
        break
