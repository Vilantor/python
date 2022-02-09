with open('File_2.txt', 'r+', encoding='utf-8') as fl:
    # fl.writelines('Привет, как дела\n')
    # fl.writelines('Hello sup?\n')
    # fl.writelines('Hola\n')
    n = 0
    line = fl.readline()
    while  :
    n += 1
    print(line)






