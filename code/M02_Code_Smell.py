uncle_sam = 1.08
pay_the_server = 1.15
food_stuff = input("How much was your meal? ")
corprate_cut = float(uncle_sam) * float(food_stuff)
pocket_book_pain = corprate_cut * pay_the_server
print("You need to leave " + str(pocket_book_pain) + " on the table to cover tax and tip.")
