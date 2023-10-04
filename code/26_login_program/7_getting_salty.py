# from hashlib import md5, sha256
# from getpass import getpass


# def old_way(prompt="Enter your password: "):
#     passwd = sha256(getpass(prompt).encode("UTF-8")).hexdigest()
#     return passwd


# print(old_way())

# def salted(prompt="Enter your password: "):
#     return sha256("".join(
#         ("SaltThisHash!", getpass(prompt), "NoPwn4U")
#         ).encode("UTF-8")).hexdigest()


# print(salted())

