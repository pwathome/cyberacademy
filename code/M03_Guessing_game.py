# Randomly generate a number between 1 and 100 (10 points)
# Not accept numbers less then 1 (5 points)
# Not accept numbers greater then 100 (5 points)
# Let the user know if the guess is to high or to low (5 points)
# Have a limit of 5 trys (5 points)
# Exit the game if the number is guessed with a 'you win' type remark (5 points)
# Exit the game if the number of trys goes over the limit with a 'you lose' type remark (5 points)

import random
number = random.randint(1,100)
game_round = 0
guess = int(input("Enter any number between 1 and 100: "))
guessed_numbers = []
# print("Answer",number)
while game_round <= 3:
    if guess <= 0 or guess > 100:
        print("Please only number between 1 and 100")
        break
    else:
        if guess < number:
            game_round += 1
            guessed_numbers.append(guess)
            print("Too low! You have",5 - game_round,"chances left","\nGuessed numbers:",guessed_numbers)
            guess = int(input("Enter number again: "))
        if guess > number:
            game_round += 1
            guessed_numbers.append(guess)
            print("Too high! You have",5 - game_round,"chances left","\nGuessed numbers:",guessed_numbers,)
            guess = int(input("Enter number again: "))
        if guess == number:
            print("you win")
        else:
            print("you loose")
