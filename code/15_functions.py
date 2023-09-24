def get_num():
    while True:
        try:
            x = int(input("Give me a number: "))
            return x
            break
        except ValueError:
            print("You didn't give me a number: ")

num1 = get_num()
num2 = get_num()
print(num1,num2)

