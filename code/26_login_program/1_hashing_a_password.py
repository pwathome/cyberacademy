from getpass import getpass
from hashlib import md5, sha256

# password = input("Enter your password: ")
# # encode password in UTF-8
# encode = password.encode("UTF-8")
# # hash encoded password with hashlib
# hashed = sha256(encode)
# # print(hashed)
# hexed = hashed.hexdigest()
# print(hexed)

def get_password(prompt="Enter your password: "):
    passwd = sha256(getpass(prompt).encode("UTF-8")).hexdigest()
    print("Encoded and hased result:",passwd)
    return passwd

pass1 = get_password()
pass2 = get_password("Re-enter your password")

if pass1 == pass2:
    print("Passwords are the same")
else:
    print("Passwords did not match")


