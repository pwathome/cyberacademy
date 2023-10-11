# The final project will take what was learned in class and will be used create a program for the following situation:

# You are the manager of several [stores].  You need to keep track of the amount of money that comes in from all of the [stores]. To accommodate this situation you decide to make a python program that will ask you the [name] (or) [location] of each [store] you manage. 
# 
# For each store, the program will ask that you enter in the following values: 100's, 50's, 20's, 10's 5's, 1's, quarters, dimes, nickles, and pennies, the program will take those values and add them to give the store total. The 
# 
# program will then take all the store totals and will calculate a grand total for all stores. Finally the program should ask the user if they want to save the information, if the user answers yes, the program should save the data to a .txt file.

# 100's, 
# 50's,
# 20's,
# 10's
# 5's,
# 1's,
# quarters,
# dimes,
# nickles,
# pennies

# Variables for the program should be named according to the data it represents. Comments need to be entered so that anyone who looks at the code can figure out what is happening. Error traps need to be used to validate data that is entered. Remember to keep the program as simple as possible, and add complexity if desired only after the core program works.

#     The program is free of syntax errors (25 points)
#     The program is free of logic errors (25 points)
#     The program adds currency values for each store (25 points)
#     The program adds store totals for a grand total (25 points)
#     The program catches all errors (25 points)
#     The program creates a text file with the correct information (25 points)
#     The program makes use of relevant variable names (15 points)
#     The program makes good use of comments (10 points)

# import os
import os
from os import path
from datetime import datetime

# clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")
# variable to check if file exists
stores_file = os.path.isfile("stores_file.txt")
# empty stores array for storing them after we read the file
stores = []
print("File exist?:",stores_file)
# Store class self, name, location, money
class Store:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.money = money


# get stores name
def get_name(prompt):
    name = input(prompt)
    return name


# get stores location
def get_location(prompt):
    location = input(prompt)
    return location


# enter money function
def add_money(prompt):
    while prompt != "n":
        monies = []
        # ask user what money they want to work with
        add_money = input(prompt)
        if add_money == "y":
            money_choice = input("What type of money?\n"
                              "a: hundreds, b: fifties \n")

            for money in money_types:
                key = money_types[money]["key"]
                value = money_types[money]["value"]

                if money_choice in ["a"]:
                    print("Working with:",money)
                    print("Worth:",value)
                    how_many = int(input(f"How many {money}?: "))
                    total = how_many * value
                    monies.append([money,[how_many,total]])
        else:
            print("No monies okay bye!")
        return monies


# get stores
def get_stores():
    if stores_file == False:
        print("No store file exits!")
    else:    
        with open("stores_file.txt") as file:
            for store in file:
                stores.append(store)
        return stores


# create store
def create_store():
    name = get_name("Enter store name: ")
    location =  get_location("Enter store location: ")
    money = add_money("Enter money?\n[Y|n]: ")
    # create new store with Store class
    new_store = Store(name, location, money)

    with open("stores_file.txt", "w") as file:
        entry_total = 0
        file.write(new_store.name+",")
        file.write(new_store.location+",")
        
        for money_type, amount in money:
            entry_total += amount[1]
            print("What was written",money_type,amount[1], entry_total)
            file.write(money_type)
            file.write(str(amount[1])+",")
        
        file.write(str(entry_total))
        file.close()
        clear()
        print("New store",new_store.name,"created. Total:",entry_total)
    return new_store


def main():
    # check for stores file
    if stores_file == False:
        # ask user if they want to create a new store
        question = input("No stores exist\n"
              "Create one ?\n[Y|n]: ").lower()
        if question == "y":
            create_store()
        else:
            print("Okay bye!")
            print(get_stores())
    else:
        print("Stores:",get_stores())
        # ask user if they want to add another store
        question = input("Want to add another store?\n"
              "[Y|n]: ").lower()
        if question == "y":
            create_store()
        else:
            print("Okay bye!")


money_types = {
        "hundreds": {
                "key": "a",
                "value": 100},
        "fifties": {
                "key": "b",
                "value": 50},
        # "twenties": {
        #         "key": "c",
        #         "value": 20},
        # "tens": {
        #         "key": "d",
        #         "value": 10},
        # "one's": {
        #         "key": "e",
        #         "value": 1},
        # "quarters": {
        #         "key": "f",
        #         "value": 0.25},
        # "dimes": {
        #         "key": "g",
        #         "value": 0.10},
        # "nickles": {
        #         "key": "h",
        #         "value": 0.05},
        # "pennies": {
        #         "key": "i",
        #         "value": 0.01}
        }


# runs the program
if __name__ == "__main__":
    main()