def MainMenu():
    print("Функции которые вам доступны:\nКалькулятор(с)\nПлощадь(s)\nОбьём(v)")
    function = input("Введите букву функции которая вам нужна:\n")

    if function == "c" or function == "C":
        Calc()

    if function == "s" or function == "S":
        Square()

    if function == "v" or function == "V":
        Volume()