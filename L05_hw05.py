
def summary():
    try:
        with open('text_3.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))

    except ValueError:
        print('Ошибка ввода')
summary()