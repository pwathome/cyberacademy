# takes in a question parameter and checks if its an integer
def is_num(question):
    while True:
        try:
            x = int(input(question))
            break
        except ValueError:
            print("That is not a number")
            continue
    return x
# cat class definition
class cat():
    def __init__(self):
        self.name = input("\nWhat is your pet's name?\n")
        self.type = input(f"What type of pet is {self.name}?\n").lower()
        self.color = input(f"What color is {self.name}?\n").lower()
        self.age = is_num(f"How old is {self.name}?\n")
# main function that gets called
def main():
    # initialize varialbles
    pet = []
    response = "y"
    name = input("Hello! What is your name?\n")
    while response != "n":
        # add the newly created pet to the pet array
        pet.append(cat())
        while True:
            response = input("\nDo you have another pet? Y|n: ").lower()
            if response == "y" or response == "":
                break
            elif response == "n":
                break
            else:
                print("\nYou did not make a correct response, please use a 'Y' for yes and a 'n' for no.")
                continue
    # get the length of pets array
    num_pets = len(pet)
    # open a file to write out pet data
    with open('My_Pet_List.txt','w') as file:
        # if theres at least one pet write it to the file
        if num_pets == 1:
            file.write(f"{name} has one pet, it's name is {pet[0].name}.\n\n")
        else:
            # otherwise do this
            file.write(f"{name} has {num_pets} pets. Those pet's names are:")
            count = 0
            for i in pet:
                count += 1
                if count == 1:
                    file.write(f" {i.name}")
                elif count != 1:
                    file.write(f", {i.name}")
            file.write(".\n\n")
        for i in pet:
            file.write(f"{i.name} is a {i.color} {i.type} and is {i.age} years old.\n")
# would run if the statement was true
if __name__ != "__main__":
    main()
else: 
    exit

