x = ""
try:
    x = int(input("Give me a number: "))
except ValueError:
    print("You didn't give me a number")
print(x)
