from hashlib import md5


with open("shadow.txt", "r") as shadows:
    with open("code/27_password_cracker/password-list-all.txt", "r") as passwords:
        for shadow in shadows:
            for password in passwords:
                hashed = md5(password.strip().encode("UTF-8")).hexdigest()
                print(f"checking {hashed}")
                if hashed == shadow:
                    print(f"Match found.\nPassword is: {password}")
                    break

            