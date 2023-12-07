with open('data_1.txt', 'r') as f1:
    lines = f1.readlines()
    if len(lines) >= 2:
        target_line = lines[2]
        with open('data_2.txt', 'w') as f2:
            f2.write(target_line)
            print('Строка успешно скопирована из файла 1 в файл 2')
    else:
        print('Ошибка: недостаточно строк в файле 1')