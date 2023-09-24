# variable to keep the game running
keep_calculating = "y"
# initialize while the want to keep playing loop
while keep_calculating != "n":
    while True:
        try:
            # check that user enters a valid number for number
            num1 = int(input("Give me a number: "))
            num2 = int(input("Give me another number: "))    
        except ValueError:
            print("Not a number, use [0-9]")
            continue
        else:
            # set operations and operations_choice variables
            operations = ["+", "-", "*", "/"]
            operation_choice = input("what operation would you like to perform?\n[+,-,*,/]: ")
            # check that user choice is valid 
            if operation_choice in operations:
                # set result variable so we can pass it later
                result = 0
                # checks to see which operation was picked and runs the corresponding logic
                if operation_choice == "+":
                    result = num1 + num2
                    print("Your numbers added:",result)
                elif operation_choice == "-":
                    result = num1 - num2
                    print("Your numbers subtracted:",result)
                elif operation_choice == "*":
                    result = num1 * num2
                    print("Your numbers multiplied:",result)
                elif operation_choice == "/":
                    if num2 == 0:
                        print("Cannot divivide by zero")
                    else:
                        result = num1 / num2
                        print("Your numbers divided:",result)
            else:
                print("Please choose from the provided options [+,-,*,/]")
            
            while True:
                # print("last result:",result)
                keep_calculating = input("Would you like to calculate another?\n[Y|n]: ").lower()
                if keep_calculating in ["y","n",""]:
                    break
                else:
                    print("You must enter 'y' for yes or 'n' for no")
            break 

