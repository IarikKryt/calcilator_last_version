def volume():
    while True:
        Vex = input('Обьём квадрата(С), или обьём параллелепипеда(P):\n')

        if Vex == 'P' or Vex == 'p':
            x = input('Введите высоту:\n')
            y = input('Введите ширину:\n')
            z = input('Введите глубину:\n')
            f = float(x) * float(y) * float(z)
            print('Результат' + str(f))
            ex = input('Хотите продолжить?(Да/Нет):\n')

            if ex == 'Нет' or ex == 'нет':
                print('Программа закроется через 5 секунд!!!')
                import time

                time.sleep(5)
                break

            if ex == 'Да' or ex == 'да':
                print('Нажмите Enter чтобы продолжить!')
                input()

            else:
                print('Ты что за ахинею написал. Программа отказывается это делать!!!')
                print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
                import time

                time.sleep(5)
                break

        if Vex == 'c' or Vex == 'C':
            cube = input('Введите сторону куба: ')
            vcube = float(cube) ** 3
            print ('Oбьём вашего куба равен: ' +str(vcube))
            ex = input('Хотите продолжить?(Да/Нет):\n')

        if ex == 'Нет' or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break

        if ex == 'Да' or ex == 'да':
            print('Нажмите Enter чтобы продолжить!')
            input()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time

            time.sleep(5)
            break

volume()