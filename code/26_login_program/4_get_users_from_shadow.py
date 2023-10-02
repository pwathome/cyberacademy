def main():
    users = []
    shadows = []
    try: 
        with open("shadow.csv", "r") as shadow:
            for line in shadow:
                print(line, end="")
                seperator = line.split(",")
                print(seperator)
                users.append(line.split(",")[0])
                shadows.append(line.split(",")[1].strip())
    except FileNotFoundError:
        pass


    print("Users:",users)
    print("Shadows: ",shadows)


if __name__ == "__main__":
    main()
    
