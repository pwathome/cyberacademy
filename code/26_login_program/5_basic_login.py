from hashlib import sha256
from getpass import getpass
from time import sleep


def login():
    users = []
    shadow_passowrds = []
    while True:
        try:
            with open("shadow.csv", "r") as shadow:
                for line in shadow:
                    users.append(line.split(",")[0])
                    shadow_passowrds.append(line.split(",")[1])
        except FileNotFoundError:
            print("No shadow file found, Please run 3_making_a_shadowfile.py")

        user = input("Enter your user name: ")
        if user in users:
            count = 0
            stored_password = users.index(user)
            print("Hashed password",shadow_passowrds[stored_password])

            while True:
                count += 1
                password = shadow_passowrds[stored_password]
                if password == shadow_passowrds[stored_password]:
                    print(f"welcome {user}")
                    return True, user
                elif count > 2:
                    print("Password did not match 3 times.",
                            "You will need to wait to try again.")
                    sleep(3)
                else:
                    print("Your password did not match.")
        else:
            print("No user with that username")


if __name__ == "__main__":
    login()