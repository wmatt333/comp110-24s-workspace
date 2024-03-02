"""Practice with Dictionaries and for Loops"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
    if in_stock[key] == True: #Don't need the == True because the if statement is already checking for True/False
        print(key)