my_tuple = ("This", "is", "a", "test!")
joined = ""
for i in my_tuple:
    joined += i

print(joined)

other_tuple = ("This", "is", "a", "test!")
print("".join(other_tuple))
print(" ".join(other_tuple))
print("-".join(other_tuple))