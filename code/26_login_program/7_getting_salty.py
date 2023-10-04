from hashlib import md5, sha512
from getpass import getpass as gp


# def old_way(prompt="Enter your password: "):
#     passwd = sha512(getpass(prompt).encode("UTF-8")).hexdigest()
#     return passwd


# print(old_way())

# def salted(prompt="Enter your password: "):
#     return sha512("".join(
#         ("SaltThisHash!", getpass(prompt), "NoPwn4U")
#         ).encode("UTF-8")).hexdigest()


# print(salted())

def passwd(username, prompt="Enter your password: "):
    salt = md5(username.encode("UTF-8")).hexdigest()
    return sha512("".join(
        ("SaltTheHasNotPwn4u", gp(prompt), salt)
        ).encode("UTF-8")).hexdigest()


user1 = input("Enter user1 name: ")
user2 = input("Enter user2 name: ")
print(passwd(user1))
print(passwd(user2))

