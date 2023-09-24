# file = open("saved_file.txt", "w")
# file.write("Hello World!")
# file.close()

# this is how you write
# with open("saved_file.txt", "w") as file:
#     file.write("Hello World!\n")
#     file.write("I am saved to the file system\n")
    
# this is how you append
with open("saved_file.txt", "a") as file:
    file.write("Hello World!\n")
    file.write("I am saved to the file system\n")
    
