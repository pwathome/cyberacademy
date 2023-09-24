def pets(pet):
    while True:
        try:
            num = int(input(f"How many {pet}s do you have?: "))
            return num
        except ValueError:
            print("That is not a number.")

cat = pets("cat")
dog = pets("dog")

print(f"You have {cat} cats & {dog} dogs.")

