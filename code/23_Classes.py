import os
# class definition
class Pet:
    def __init__(self, name, species, breed, color, age):
        self.name = name
        self.species = species
        self.breed = breed
        self.color = color
        self.age = age

# clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# get int function
def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("You can't use negative numbers")
        except ValueError:
            print("You didn't enter a number.")

def main():
    # setting variables
    pets = []
    add_another = "y"
    # staring while loop
    while add_another != "n":
        clear()
        name = input("Enter your pets name: ")
        species = input(f"What is species is {name}: ")
        breed = input(f"What breed of {species} is {name}: ")
        color = input(f"What color of {breed} is {name}: ")
        age = get_int(f"How old is {name}: ")
        pets.append(Pet(name, species, breed, color, age))
        # loop to assk to add another
        while True:
            clear()
            add_another = input("Would you like to add another pet?\n"
                                "[Y|n]: ").lower()
            if add_another in ["y", "n", ""]:
                break
            else:
                print("You need to use 'y' for yes or 'n' for no.")
    clear()
    # loop over collected pets
    for p in pets:
        print(f"{p.name} is a {p.color} {p.breed} {p.species} and is {p.age} year(s) old.")
    # writing to a file becuase it's "w"
    with open("pets.csv", "w") as file:
        file.write("name, species,breed,color,age")
        for p in pets:
            file.write(f"\n{p.name},{p.species},{p.breed},{p.color},{p.age}")
        
# runs the program
if __name__ == "__main__":
    clear()
    main()