x = int(input("Give me a number for x: "))
y = int(input("Give me a number for y: "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

if x >= y:
    print("x is greater than or equal to y")
else:
    print("x is less than y")

if x == 0:
    print("x equals 0")
elif y == 0:
    print("y equals 0")
else:
    print("x and y are not 0")

if x != 0:
    print("x is not 0")
elif y != 0:
    print("y is not 0")

if "yes" != "no":
    print("it is not opposite day")
