import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("See you in 3", end="",flush=True)
time.sleep(1)
print("2", end="", flush=True)
time.sleep(1)
print("1", end="", flush=True)
time.sleep(1)
print("Lets Jam!")

