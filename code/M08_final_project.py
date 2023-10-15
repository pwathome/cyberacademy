
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


# enter money function
def add_money(prompt):
    while prompt != "n":
        monies = []
        add_money = input(prompt)
        if add_money == "y":
            # ask user what money they want to work with
            money_choice = input("What type of money?\n"
                              "a: hundreds, b: fifties c: twenties, d: tens, e: fives f: ones, g: quarters, h: dimes i: nickles, j: pennies\n")
            # loop over money to get money attributes
            for m in money_types:
                letter_choice = m[0]
                int_value = m[1]
                m_name = m[2]

                if money_choice == letter_choice:
                    how_many = int(input(f"How many {m_name}?: "))
                    total = how_many * int_value
                    monies.append([m_name,[how_many,total]])
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
    name = input("Enter store name: ")
    location =  input("Enter store location: ")
    money = add_money("Enter money?\n[Y|n]: ")
    # create new store with Store class
    new_store = Store(name, location, money)
    # save store to file
    with open("stores_file.txt", "w") as file:
        entry_total = 0
        file.write(new_store.name+",")
        file.write(new_store.location+",")
        # loop over money to get money
        for money_type, amount in money:
            entry_total += amount[1]
        file.write(str(entry_total))
        file.close()

        print("New store",new_store.name,"added. Total:",entry_total)
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
        question = input("Want to create a new store?\n"
              "[Y|n]: ").lower()
        if question == "y":
            create_store()
        else:
            print("Okay bye!")

# money types array
money_types = [["a", 100, "hundreds"],["b", 50, "fifties"],
               ["c", 20, "twenties"],["d", 10, "tens"],
               ["e", 5, "fives"], ["f", 1, "ones"],
               ["g", .25, "quarters"], ["h", .10, "dimes"],
               ["i", .05, "nickles"], ["j", .01, "pennies"]]

# runs the program
if __name__ == "__main__":
    main()