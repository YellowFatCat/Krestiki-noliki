import os;

clearScreen = lambda: os.system('cls'); # Очистка экрана.

def showTable(): # Вывод игрового поля на экран.
    print(splitter);
    
    for i in range(3):
        
        if (i == 0): print("C ", end = '');
        if (i == 1): print("B ", end = '');
        if (i == 2): print("A ", end = '');
        print("| ", end = '');
        
        for j in range(3):
            print(table[i][j], "| ", end = '');
            
        print("");
        print(splitter);

    print("    ", end = '');   
    for j in range(3):
        print(j + 1, "  ", end = '');
    print("\n");

def isStepTrue(STEP): # Проверка корректности хода игрока.
    '''
    Параметры:  STEP - строка, введенная пользователем для хода.
 
    Возвращает: 0, если проверка не выявила ошибок,
                1, если данные введены некорректно,
                2, если желаемая клетка уже занята.
    '''
    if (len(STEP) != 2):
        return 1;

    if((STEP[0]).upper() != "A" and str(STEP[0]).upper() != "B" and str(STEP[0]).upper() != "C"):
        return 1;

    try:
        if(int(STEP[1]) != 1 and int(STEP[1]) != 2 and int(STEP[1]) != 3):
            return 1;
    except ValueError: return 1;

    KOORD = []; 
    if (STEP[0].upper() == "C"): KOORD.append(0);
    else:
        if (STEP[0].upper() == "B"): KOORD.append(1);
        else: KOORD.append(2);
    KOORD.append(int(STEP[1]) - 1);
    if (table[KOORD[0]][KOORD[1]] != " "): return 2;

    return 0;   

def isWin(KOORD, SYMBOL): # Проверка на победу.
    '''
    Параметры:  KOORD - лист, содержащий координаты хода,
                SYMBOL - символ, которым ходит игрок ("X" или "0").

    Возвращает: True, если сделанный ход является победным,
                False, если ход победным не является.
    '''
    if (((KOORD[0] == 0) or (KOORD[0] == 2)) and ((KOORD[1] == 0) or (KOORD[1] == 2))): # Если символ поставлен в угловую клетку.

        # Проверяем строку.
        if ((table[KOORD[0]][0] == table[KOORD[0]][1]) and (table[KOORD[0]][0] == table[KOORD[0]][2])):
            return True;
            
        # Проверяем столбец.
        if ((table[0][KOORD[1]] == table[1][KOORD[1]]) and (table[0][KOORD[1]] == table[2][KOORD[1]])):
            return True;

        # Проверяем диагональ.
        if (KOORD[0] == KOORD[1]):
            if ((table[0][0] == table[1][1]) and (table[0][0] == table[2][2])): # Если символ расположен на главной диагонали.
                return True;
            else:
                if ((table[0][2] == table[1][1]) and (table[0][2] == table[2][0])): # Если символ расположен на побочной диагонали.
                    return True;
    else:
        if ((KOORD[0] == KOORD[1]) and (KOORD[0] == 1)): # Если символ поставлен в центре поля.
            if ((table[0][2] == table[2][0]) and (table[0][2] == SYMBOL)) or ((table[0][0] == table[2][2]) and (table[0][0] == SYMBOL)) or ((table[0][1] == table[2][1]) and (table[0][1] == SYMBOL)) or ((table[1][0] == table[1][2]) and (table[1][0] == SYMBOL)):
                return True;
                
        else: # Если символ поставлен не в углу и не в центре поля.
            # Проверяем строку.
            if ((table[KOORD[0]][0] == table[KOORD[0]][1]) and (table[KOORD[0]][0] == table[KOORD[0]][2])):
                return True;
            
            # Проверяем столбец.
            if ((table[0][KOORD[1]] == table[1][KOORD[1]]) and (table[0][KOORD[1]] == table[2][KOORD[1]])):
                return True;
            
    return False;

answ = -1;
while (answ != 5):
    
    clearScreen();

    # Выбор соответствующего пункта меню.
    print("Добро пожаловать в игру \"Крестики-нолики\"!\nПожалуйста, выберите необходимый пункт меню:");
    print("1 - Простая игра\n2 - Турнир\n3 - Результаты последнего турнира\n4 - О программе\n5 - Выход из игры\n");

    answ = "";
    while (answ == ""):
        answ = input("Ваш выбор: ");
        try: answ = int(answ);
        except ValueError:
            print("Пожалуйста, введите число.");
            answ = "";
            continue;
        if (answ < 1 or answ > 5):
            print("Введенное число должно лежать в интервале [1; 5] в соответствии\nс количеством пунктов меню.");
            answ = "";

    gamesCount = 0;

    if (answ == 3):
        clearScreen();

        try:
            f = open("results.txt", "r");
            arr = f.readlines();
            f.close;

            print("*** Результаты последнего матча ***\n");
            n = len(arr);
            for i in range(n):
                print(arr[i], end = "");
        except IOError:
            print("Еще не было сыграно ни одного турнира, либо данные о результатах были удалены.");

        print("\n");
        input("Нажмите любую клавишу для продолжения");

    if (answ == 4):
        clearScreen();
        print("Программа \"Крестики-нолики\", v. 1.0\n\nАвторы: Путинцева А.А., Семенова П.С., группа 1652.\nСанкт-Петербург, 2013 год.");
        print("\n");
        input("Нажмите любую клавишу для продолжения");
        
    if (answ == 1 or answ == 2):
        if (answ == 1): gamesCount = 1;
        else: gamesCount = 5;

        for index in range(gamesCount):
            clearScreen();
            if (answ == 1): print("*** Простая игра ***\n");
            else: print("*** Турнир ***\nИгра ", index + 1, "\n");
            
            # Имена игроков.
            if (answ == 1 or (answ == 2 and index == 0)):
                name1 = "";
                while (name1 == ""):
                    name1 = input("Введите имя первого игрока: ");
                    if (name1 == ""): print("Имя игрока не может быть пустой строкой.");
                    
                name2 = name1;
                while (name1 == name2 or name2 == ""):
                    name2 = input("Введите имя второго игрока: ");
                    if (name1 == name2): print("Имя", name1, "уже занято. Пожалуйста, выберите другое имя.");
                    if (name2 == ""): print("Имя игрока не может быть пустой строкой.");

            splitter = "  +---+---+---+"; # Разделитель строк в таблице.

            # Список, содержащий данные о поставленных крестиках/ноликах.
            table = [[" ", " ", " "],
                     [" ", " ", " "],
                     [" ", " ", " "]];

            clearScreen();
            if (answ == 1): print("*** Простая игра ***\n");
            else: print("*** Турнир ***\nИгра ", index+1, "\n");
            showTable();

            play = True; # Логическая переменная, показывающая, идет ли игра.
            win = False; # Логическая переменная, показывающая, есть ли выигрыш.

            # Счет игроков (для турнира).
            score1 = 0;
            score2 = 0;
            
            # ИГРА.
            while (play): # Цикл игры.
                for i in range(4):

                    # Ход первого игрока.
                    player1 = input(name1 + " (крестик): "); 
                    
                    # Проверка корректности хода.
                    while (isStepTrue(player1) != 0): # Пока координата введена некорректно.
                        if (isStepTrue(player1) == 1):
                            print("Ошибка ввода хода!\nПожалуйста, введите координату вида <буква строки><номер столбца>.");
                            print("Например, a1.");
                        else: print("К сожалению, клетка", player1, "уже занята. Выберите другую клетку.");
                        player1 = input(name1 + ": ");

                    # Распознавание введенных координат.
                    koord = []; 
                    if (player1[0].upper() == "C"): koord.append(0);
                    else:
                        if (player1[0].upper() == "B"): koord.append(1);
                        else: koord.append(2);
                    koord.append(int(player1[1]) - 1);

                    # Установка соответствующего символа (X или 0) в таблицу.
                    table[koord[0]][koord[1]] = "X";
                    clearScreen();
                    if (answ == 1): print("*** Простая игра ***\n");
                    else: print("*** Турнир ***\nИгра ", index + 1, "\n");
                    showTable();

                    # Проверка на победу.
                    if (isWin(koord, "X")):
                        print(name1, "победил!");
                        score1 += 1;
                        play = False; # Игра завершается.
                        win = True; # Результат игры - победа одного из игроков.
                        break;

                    # Ход второго игрока.
                    player2 = input(name2 + " (нолик): ");  

                    # Проверка корректности хода.
                    while (isStepTrue(player2) != 0): 
                        if (isStepTrue(player2) == 1):
                            print("Ошибка ввода хода!\nПожалуйста, введите координату вида <буква строки><номер столбца>.");
                            print("Например, a1.");
                        else: print("К сожалению, клетка", player2, "уже занята. Выберите другую клетку.");
                        player2 = input(name2 + ": ");

                    # Распознавание введенных координат.
                    del(koord);
                    koord = []; 
                    if (player2[0].upper() == "C"): koord.append(0);
                    else:
                        if (player2[0].upper() == "B"): koord.append(1);
                        else: koord.append(2);
                    koord.append(int(player2[1]) - 1);

                    # Установка соответствующего символа (X или 0) в таблицу.
                    table[koord[0]][koord[1]] = "0";
                    clearScreen();
                    if (answ == 1): print("*** Простая игра ***\n");
                    else: print("*** Турнир ***\nИгра ", index + 1, "\n");
                    showTable();

                    # Проверка на победу.
                    if (isWin(koord, "0")):
                        print(name2, "победил!");
                        score2 += 1;
                        play = False; # Игра завершается.
                        win = True; # Результат игры - победа одного из игроков.
                        break;
                    
                # Последний (девятый) ход.    
                if (play == True): 
                    player1 = input(name1 + ": "); # Ход первого игрока.
                    
                    # Проверка корректности хода.
                    while (isStepTrue(player1) != 0): # Пока координата введена некорректно.
                        if (isStepTrue(player1) == 1):
                            print("Ошибка ввода хода!\nПожалуйста, введите координату вида <буква строки><номер столбца>.");
                            print("Например, a1.");
                        else: print("К сожалению, клетка", player1, "уже занята. Выберите другую клетку.");
                        player1 = input(name1 + ": ");

                    # Распознавание введенных координат.
                    koord = []; 
                    if (player1[0].upper() == "C"): koord.append(0);
                    else:
                        if (player1[0].upper() == "B"): koord.append(1);
                        else: koord.append(2);
                    koord.append(int(player1[1]) - 1);

                    # Установка соответствующего символа (X или 0) в таблицу.
                    table[koord[0]][koord[1]] = "X";
                    clearScreen();
                    if (answ == 1): print("*** Простая игра ***\n");
                    else: print("*** Турнир ***\nИгра ", index + 1, "\n");
                    showTable();

                    # Проверка на победу.
                    if (isWin(koord, "X")):
                        print(name1, "победил!");
                        score1 += 1;
                        play = False; # Игра завершается.
                        win = True; # Результат игры - победа одного из игроков.
                        break;
                    
                play = False;

            if (not win): print("Ничья!");
            input("Нажмите любую клавишу для продолжения");
            if (answ == 2 and index == gamesCount - 1):
                print("Счет турнира:\n", name1, ": ", score1, "\n", name2, ": ", score2);
                f = open("results.txt", "w");
                line = name1 + ": " + str(score1) + "\n" + name2 + ": " + str(score2);
                f.write(line);
                f.close();
                input("Нажмите любую клавишу для продолжения");
    
