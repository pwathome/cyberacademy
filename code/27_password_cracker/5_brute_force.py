from hashlib import md5
from string import printable
from itertools import product


with open("shadow.txt", "r") as shadows:
    for shadow in shadows:
        for x in range(1,4):
            res = product(printable[:-6], repeat = x)
            for i in res:
                password = md5("".join(i).encode("UTF-8")).hexdigest()
                print(password)
                if password == shadow:
                    print("".join(i))
                    # print(f"In{password}")
                    break
                
    