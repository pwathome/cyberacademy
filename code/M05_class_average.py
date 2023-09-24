# import os
import os

# clear function
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# get_name function that will prompt user to enter a name
def get_name():
    name = input("Enter a students name: ")
    return name

# get_grade function that will prompt user to enter a grade
def get_grade(student):
    while True:
        grade = input(f"Enter {student}'s letter grade: ").lower()
        if grade in ["a", "b", "c", "d", "e", "f"]:
            return grade
        else:
            print("Please enter a letter grade (a, b, c, d, e or f)")

# class_loop function that will loop over each "class"
def class_loop():
    # cont variable is the flag if the user want to keep going. Otherwise the
    # while loop breaks
    cont = "y"
    # section array that we'll push the student and their grade into
    section = []
    # while loop
    while cont != "n":
        # setting the name and grade variables as the functions defined above
        name = get_name()
        grade = get_grade(name)
        # we append the name and grade as and array
        section.append([name, grade])
        while True:
            # clear the screen and ask the user if they want to enter another student
            # otherwise we return the section
            clear()
            cont = input("Do you want to enter another student?\n"
                         "[Y|n]: ")
            if cont in ["y", "n", ""]:
                break
            else:
                print("Enter y for yes and n for no")
    return section


# average function that loops over the section, uses the conversion 
# key, value pair variable to get the class average
def average(section):
    total = 0
    conversion = {"a":4, "b":3, "c":2, "d":1, "f":0}
    for student in section:
        total += conversion[student[1]]
    avg = total / len(section)
    return avg

# output function that loops over the section, prints each students name and # # grade then calls the average function to grab that data to print as well
def output(section):
    for student in section:
        print(f"{student[0]} has a(n) {student[1].upper()}")
    avg = average(section)
    print(f"The class average is {avg:.2f}")

# main function that starts the program
def main():
    section = class_loop()
    output(section)

# if check to make sure we're running the right program
if __name__ == "__main__":
    main()
    
# Group project coded with Stuart

