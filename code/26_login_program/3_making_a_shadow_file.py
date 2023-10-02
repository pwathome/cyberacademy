from getpass import getpass
from hashlib import sha256

def get_passwd(prompt="Enter your password: "):
    passwd = sha256(getpass(prompt).encode("UTF-8")).hexdigest()
    return passwd


def main():
    while True:
        user_name = input("Enter your username: ")
        pass1 = get_passwd()
        pass2 = get_passwd("Confirm your password")
        
        if pass1 == pass2:
            with open("shadow.csv", "a") as s:
                s.write(f"{user_name},{pass1}\n")
                break
        else:
            print("Your password did not match,\n"
                  "please start over.")


if __name__ == "__main__":
    main()