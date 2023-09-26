from datetime import datetime
import os.path

# variable to check if file exists
mood_file = os.path.isfile("./how_was_your_day.txt")
def ask_question():
    print("Welcome to mood checker!")
    while True:
        question = input("Are you having a 'good' or 'bad' day? ").lower()
        # check that they used good or bad
        if question in ["good", "bad", ""]:
            # initialize todays time & date
            today = datetime.now().ctime()
            # write answer to a file
            with open("how_was_your_day.txt", "w") as file:
                file.write(f"{today}\n")
                file.write(question)
                file.close()
                return
        else:
            print("Enter 'good' or 'bad' please!")


# check for existing file first
if mood_file == False:
    ask_question()
else:
    # initialize empty file_date array
    file_data = []
    # open the file and loop through lines
    with open("how_was_your_day.txt", "r") as file:
        for line in file:
            # append lines to file_data array
            file_data.append(line)
        # close file
        file.close()
    # prints last saved date
    print(f"\nLast mood check was on {file_data[0]}")
    # ask user if they want to check mood
    check_again = input("Would you like to do another mood check?\n"
                        "[Y|n]:").lower()

    if check_again == "y":
        ask_question()
    else:
        print("Okay have a fantastic day!")

