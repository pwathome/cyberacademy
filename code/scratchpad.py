# get money function
def add_money():
    money_types = {
        "hundreds": {
                "key": "a",
                "value": 100},
        "fifties": {
                "key": "b",
                "value": 50},
        "twenties": {
                "key": "c",
                "value": 20},
        "tens": {
                "key": "d",
                "value": 10},
        "one's": {
                "key": "e",
                "value": 1}
        }


    monies = []
    # print(money_types["hundreds"]["key"])
    # choice = money_types["hundreds"]["key"]
    # print(money_types.keys())
    # if question in ["a","b","c","d","e"]:
    for money in money_types.keys():
        # hard coded choice for now
        question = "a"
        print(money_types[money]["key"])
        key = money_types[money]["key"]
        value = money_types[money]["value"]

        # # match money choice with selection key
        # money_choice = money_types[money]
        # # print(money_choice)
        # # cache selection
        selection = question
        # print("Selection: ",selection)
        # # print("Which money type?: ",selection)
        if selection in ["a"]:
            print("Working with:",money)
            print("Worth:",money_types[money]["value"])
            how_many = 2
            total = how_many * money_types[money]["value"]
            print(f"Total for {money}'s: {total}")
            # print(money_types.keys())
            monies.append([{money: how_many},total])

            print(monies)
            return monies

        return monies

add_money()
