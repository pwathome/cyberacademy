from hashlib import md5


hashed = md5(input("Save what as an md5 hash: ").encode("UTF-8")).hexdigest()
with open("shadow.txt", "w") as shadow:
    shadow.write(hashed)

