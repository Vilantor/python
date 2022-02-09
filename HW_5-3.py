with open('File_3.txt', 'r+', encoding='utf-8') as oklad:
    # oklad.writelines('Иванов 20000 \n')
    # oklad.writelines('Петров 45000 \n')
    # oklad.writelines('Смирнов 43000 \n')
    # oklad.writelines('Сидоров 12000 \n')
    # oklad.writelines('Реутов 15000 \n')
    # oklad.writelines('Мамонтов 32000 \n')
    # oklad.writelines('Раков 19000 \n')
    # oklad.writelines('Маков 23000 \n')
    # oklad.writelines('Собаков 29000 \n')
    # oklad.writelines('Котов 36000 \n')
    spisok = oklad.readlines()
    print(spisok)

