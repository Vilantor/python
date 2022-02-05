# my_list = [12, 25, 634, 13, 76, 23, 136, 964, 145]

# new_list = []

def new_list(a):
    while a < 100:
        new_list.append(a for a in my_list if a[i] < a[i+1])
        a += 1
        return new_list(a)

my_list = [12, 25, 634, 13, 76, 23, 136, 964, 145]


print(new_list())

