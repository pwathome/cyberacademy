"""
Loop:
    List of names and food cost
    Populate list using user input

find the average food price

zip the lists

tell each person if its too high or low

Group: [Stuart, Paul, Colton, Cory]
"""

# import os
import os
# define clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# define get cost function
def get_cost():
    while True:
        try:
            cost = float(input("Enter their food price: "))
            if cost < 0:
                print("You can not pay negative money. Try again.")
            else:
                break
        except ValueError:
            print("You did not enter a number.")
    return cost


names = []
costs = []
cont = "y"

while cont != "n":
    names.append(input("Enter a name: "))
    costs.append(get_cost())
    while True:
        cont = input("Do you have another name\n"
                    "[Y|n]: ").lower()
        
        if cont in ["y", "n", ""]:
            break
        else:
            print("You must enter 'y' for yes or 'n' for no")
    
average_cost = sum(costs) / len(costs)

for name, cost in zip(names, costs):
    if cost > average_cost:
        print(f"{name} paid more than the average. They paid ${(cost - average_cost):.2f} more than average.")
    elif cost < average_cost:
        print(f"{name} paid less than the average. They paid ${(average_cost - cost):.2f} less than average.")
    else:
        print(f"{name} paid the exact same as average.")
        
