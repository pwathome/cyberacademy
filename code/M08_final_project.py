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

# clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

stores = []

# Store class self, name, location, money
class Store:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.money = money

# get stores name
def get_name():
    name = input("Enter store name: ")
    print("Stores name: ",name)
    return name

# get stores location
def get_location():
    location = input("Enter store location: ")
    print("Stores location",location)
    return location

# get stores money
def get_money():
    money = int(input("Enter store total: "))
    print("Stores total",money)
    return money


# read store
def get_stores(stores):
    for store in stores:
        print("store(s)",store)
    return stores
        

# create store
def create_store():
    # check for store before creating
    stores = []
    # call create store
    store = {
        "name": get_name(),
        "location": get_location(),
        "money": get_money(),
    }
    # append store to stores array
    stores.append(store)
    # print created store
    print("Created Store in create store",stores[0])

# update store

# delete store

def main():
    create_store()
    get_stores(stores)
    

# runs the program
if __name__ == "__main__":
    main()