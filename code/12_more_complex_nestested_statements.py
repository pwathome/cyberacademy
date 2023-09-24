# setting the empty friends list
friends = []

question = "y"

while question != "n":
    friends.append(input("Name a friend: "))
    
    while True:
        question = input("Would you like to add another?\n[Y|n]: ").lower()
        
        if question in ["y", "n", ""]:
            break
        else:
            print("You must enter 'y' for yes or 'n' fot no")

print(friends)
