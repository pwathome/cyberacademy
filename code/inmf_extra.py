import random

class Car:
    def __init__(self, make):
        self.make = make


def main():
    cars = []
    add_another = "y"
    
    while add_another != "n":
        make = input("Give me a make of car: ")
        cars.append(Car(make))

        while True:
            add_another = input("Would you like to add another one?\n"
                           "[Y|n]: ").lower()
            if add_another in ["y", "n", ""]:
                break
            else:
                print("use 'y' for yes or 'n' for no")
                
    random_pick = random.choice(cars)
    print("The randomly selected car is:",random_pick.make)    

    with open("cars.csv", "w") as file:
        file.write("Make")
        for car in cars:
            file.write(f"\n{car.make}")
    print("List saved to CSV!")


# runs the program
if __name__ == "__main__":
    main()
    
