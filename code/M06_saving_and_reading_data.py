# Students will make a Python program that will save the output of a calculation as a text file. The program should ask the user if they are having a good or bad day. The program should save the 'good' or 'bad' day answer to a text file. After rerunning the program, the program should read the text file and remark about the last time the user used the program.

# Variables for the program should be named according to the data it represents. Comments need to be entered so that anyone who looks at the code can figure out what is happening. Error traps need to be used to validate data that is entered. Remember to keep the program as simple as possible, and add complexity if desired only after the core program works.

# The requirements for this program are:

#     Error validation for if there is no text file to read from (10 points)
#     Save 'good' or 'bad' to file (10 points)
#     Remark if user had a good day on rerunning the program (10 points)
#     Remark if user had a bad day on rerunning the program (10 points)
from datetime import date
import os.path


# variable to check if file exists
check_file = os.path.isfile("./how_was_your_day.txt")
# check for existing file
if check_file == False:
    question = input("Welcome to my mood checker!"
                     "Are you having a 'good' or 'bad' day? ").lower()
    # check that they used good or bad
    if question in ["good", "bad", ""]:
        # date 
        today = str(date.today())

        # write answer to a file
        with open("how_was_your_day.txt", "w") as file:
            file.write(f"{today}\n")
            file.write(question)
    else:
        print("Enter 'good' or 'bad' please!")
else:
    # open the file if one exists
    file_data = []
    with open("how_was_your_day.txt", "r") as file:
        for line in file:
            file_data.append(line)
        
        print(f"\nLast mood check was on {file_data[0]}")