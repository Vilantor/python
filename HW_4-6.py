# # 1
from itertools import count

for el in count(4):
    if el > 20:
        break
    else:
        print(el)

# 2
from itertools import cycle

a = 0
for el in cycle("Avadakedavra"):
    if a > 20:
        break
    print(el)
    a += 1