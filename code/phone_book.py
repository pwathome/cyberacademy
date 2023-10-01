from os import system, name
from time import sleep
import re

class Contact:
    def __init__(self,fname,lname,number,email):
        self.fname = fname
        self.lname = lname
        self.number = number
        self.email = email
        

def clear():
    system("cls" if name == "nt" else "clear")
    
    
def add_contact():
    contacts = []
    add_another = "y"
    while add_another != "n":
        clear()
        correct = "n"
        while correct == "n":
            fname = input("Enter first name: ")
            lname = input(f"Enter {fname}'s last name: ")
            number = int(input(f"Enter {fname}'s phone number: "))
            email = input(f"Enter {fname}'s email")
            clear()
            print(f"Name:{fname}, {lname}\n"
                  f"Phone number: {number}\n"
                  f"Email: {email}\n")
            correct = input("Is this information correct?\n"
                            "[Y|n]: ").lower()
            
            while True:
                if correct in ["y", "n", ""]:
                    contacts.append(Contact(fname,lname,number,email))
                    break
                elif correct == "n":
                    break
                else:
                    print("You need to use 'y' or 'n'")

    while True:
        add_another = input("Add another entry?\n"
                            "[Y|n]: ").lower()
        if add_another in ["y", "n", ""]:
            break
        else:
            print("You need to use 'y' or 'n'")
    clear()
    for i in contacts:
        print(f"{i.fname}{i.lname}{i.number}{i.email}\n")
        
        
add_contact()