import re

with open("contacts.csv", "r") as file:
    searchable = file.read()
    query = input("Search for what: ")
    pattern = re.compile(rf".*{query}.*")
    matches = pattern.findall(searchable)
    
    for match in matches:
        print(match)
