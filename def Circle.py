def Square():
    while True:
        import math
        R = float(input('Введите радиус круга:\n'))
        S = math.pi * R * R
        print('Площадь круга:', S)
        ex = input('Хотите продолжить(c), выйти в меню(m), закрыть программу(e)?:\n')

        if ex == 'e' or ex == 'E' or ex == 'е' or ex == 'Е':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break

        if ex == 'c' or ex == 'C' or ex == 'с' or ex == 'С':
            print('Нажмите Enter чтобы продолжить!')
            Square()

        if ex == 'm' or ex == 'M' or ex == 'м' or ex == 'м':
            MainMenu()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time
            time.sleep(5)
            break