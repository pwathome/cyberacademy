menu_items = {
    "Burger": 7.99,
    "Cheese Burger": 9.99,
    "Fries": 3.79,
    "Drink": 1.08
}
menu_items["Hotdog"] = 3.99
# using built in update method to update the defined dictionary above
menu_items.update({
    "Fries": 2.99,
    "Drink": 0.99
})

# # print menu item keys 
# for i in menu_items.keys():
#     print(i)

# # # print menu item values
# for i in menu_items.values():
#     print(i)

# print the keys and values in a dictionary    
# print(menu_items.items())
# for key, value in menu_items.items():
    # print(key, value)
    
# give the value for a given key
# print(menu_items["Fries"])

def get_key(arg, dictionary):
    for key, value in dictionary.items():
        if value == arg:
            return key

# x = get_key(0.99,menu_items)
# print(x)

# sample order
order = ["Burger", "Fries", "Drink", "Cheese Burger", "Fries", "Drink", "Drink",
         "Burger", "Fries", "Drink", "Hotdog", "Drink", "Burger", "Cheese Burger",
         "Hotdog", "Fries", "Drink", "Cheese Burger"]

# empty dictionary to track orders
counting = {}
total = 0
for item in order:
    counting[item] = counting.get(item, 0) + 1

for key, value in counting.items():
    # print("key value pair",key, value)
    # print("menu_items[key]",menu_items[key])
    total += menu_items[key] * value
print(f"Total:{total:.2f}")


# use cases
# IP address counting
# general analysis