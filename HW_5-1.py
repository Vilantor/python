# file = open('New_file.txt', 'w+', encoding='utf-8')
# while file.writelines(input('Введите текст: \n')) != '':  # не понял, как обозначить, что при вводе пустой строки ввод заканчивается...
#     continue
# else:
#     print(file.read())
#     file.close()


with open('File_1.txt', 'a+', encoding='utf-8') as file:
    file.writelines(input('Введите текст: \n'))
    while file.writelines(input('Введите текст: \n')) != ' ':  # не понял как обозначить, что при вводе пустой строки ввод заканчивается...
        continue
    else:
        print(file.read())