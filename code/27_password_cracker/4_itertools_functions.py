from string import printable
from itertools import product

for x in range(1,4):
    # print(x)
    res = product(printable[:-6], repeat = x)
    # print(res)
    for i in res:
        # print(i) # prints tuples
        print("".join(i))
        