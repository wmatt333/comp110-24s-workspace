"""Demonstrate Basic List Syntax"""

#Initialize an empty list
grocery_list: list[str] = list() #<- list constructor
grocery_list: list[str] = [] #<- literal (also a list constructor)

print(grocery_list)

#Adding items
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("After appending")
print(grocery_list)

#Create an already popualated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print(grocery_list2)
grocery_list2.append("eggs") #add another item
print(grocery_list2)

#Indexing
print("First item of list")
print(grocery_list[0])

#Modifying by Index
print("Before change: ")
print(grocery_list)
print("After change")
grocery_list[1] = "almond milk"
print(grocery_list)

#Measuring Length
print("Length of list: ")
print(len(grocery_list))

#Removing an Item
grocery_list.pop(1)
print("After removing almond milk: ")
print(grocery_list)

#Function
def display(word: list[str]) -> None:
    print(word)

display(grocery_list)
display(["Alyssa", "Erin", "AK"])

#Create a list
def create(word1: str, word2:str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return(my_list)

print(create("Hello", "World"))