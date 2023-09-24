my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "gundam"]
# for i in my_list:
#     print(i)
my_other_list = ["A","B","C","D","E","F","G"]
for i, j in zip(my_list, my_other_list):
    print(j,"is for",i)