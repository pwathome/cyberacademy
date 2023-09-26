#code by cory, colton, stuart, paul, darvyn
#SDEV Monday 1PM Class

import random
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def template(question):
    print(question[0])

    options = question[1]
    correct_answer = options [0]

    random.shuffle(options)
    correct_index = options.index(correct_answer)

    for let, num in letter.items():
        print(let + ":", options[num])

    while True:
        answer = input("What is your answer?: ").lower()
        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("You must enter a, b, c, or d.")

    clear()

    if letter[answer] == correct_index:
        print("You got the correct answer!\n")
        return 1
    else:
        print("You got the wrong answer. :(\n ")
        return 0


def calc_grade(count):
    if count >= 9:
        return "A"
    elif count >= 8:
        return "B"
    elif count >= 7:
        return "C"
    elif count >= 6:
        return "D"
    else:
        return "F"
    

def main():
    count = 0
    for question in questions:
        count += template(question)
    print("You got a(n)", calc_grade(count))


questions = [
    ["What color dragon am I thinking of?", ["Orange", "Blue", "Purple", "Red"]],
    ["What is my favorite cheese?", ["Colby Jack", "Mozerlla", "Guda", "American"]],
    ["What color shirt am I wearing today?", ["Blue", "Green", "Grey", "White"]],
    ["What is the color of the sky?", ["Sky Blue", "Auquatic Blue", "Baby Blue", "Dark Blue"]],
    ["What is your favorite tree?", ["Pine Tree", "Oak Tree", "Walnut Tree", "Maple Tree"]],
    ["Are unicorns real?", ["Yes", "No", "Maybe", "I Dont Know"]],
    ["What side of the bed did I wake up on?", ["Right", "Left", "Wrong", "Right"]],
    ["How old is old?", ["53", "22", "16", "46"]],
    ["Who typed this code?", ["Darvyn", "Stuart", "Cory", "Paul", "Colton"]],
    ["Questions make me?", ["Sad", "Mad", "Happy", "Scared"]],
]


letter  = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3
}


if __name__ == "__main__":
    clear()
    main()