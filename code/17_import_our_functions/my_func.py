def get_num():
    while True:
        try:
            num = int(input("Give me a num: "))
            return num
        except ValueError:
            print("That's not a number!")

# __main__ is the over all main function
if __name__ == "__main__":
    print(__name__)
