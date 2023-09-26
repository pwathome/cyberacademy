# def add( x,y):
#     return x + y

# print(add(3,3))

# optional arguments example
# def subtract(x,y=5):
#     return x - y

# print(subtract(6))

# def product(x=9, y=3):
#     return x * y

# print(product())
# print(product(3))
# print(product(3,7))

def get_pos(prompt="Give a positive number: "):
    while True:
        try:
            num = int(input((prompt)))
            if num < 0:
                print("You need to give a positive number")
            else:
                return num
        except ValueError:
            print("You did not enter a number")
            

cat = get_pos("Enter how many animals you have: ")
print(cat)

