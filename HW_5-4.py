with open('File_5.txt', 'r+', encoding='utf-8') as file:
    che = file.readlines()
    new = che
    if 'One' in new:
        new.insert('One', 'Один')
        new.remove('One')
    elif 'Two' in new:
        new.insert('Two', 'Два')
        new.remove('Two')
    elif 'Three' in new:
        new.insert('Three', 'Три')
        new.remove('Three')
    elif 'Four' in new:
        new.insert('Four', 'Четыре')
        new.remove('Four')
    print(new)

