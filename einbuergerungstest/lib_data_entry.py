import json

# Load the library from a JSON file
def load_library(items_lib):
    with open(items_lib, 'r') as file:
        return json.load(file)

# Save the library to a JSON file
def save_library(items, items_lib):
    with open(items_lib, 'w') as file:
        json.dump(items, file)

# Add the new entry to the library
def add_item(item_key, q, opt, cor):
    items[item_key] = {
        q,
        opt,
        cor
        }

#enter input
def input_item(item_key):
    question = input("Enter text of question: ")
    option_0 = input("Enter response 0: ")
    option_1 = input("Enter response 1: ")
    option_2 = input("Enter response 2: ")
    option_3 = input("Enter response 3: ")
    options = [option_0, option_1, option_2, option_3]
    correct_response = input("Enter index for correct response (0-3): ")
    # Remove any existing entry with the same key
    items.pop(item_key, None)
    add_item(item_key, question, options, correct_response)
    print(items[number])
    
# Load the existing library
items_lib = 'items_lib.json'
items = load_library(items_lib)    

# Enter data into dictionary items
number = input("Enter item number: ")
if number in items:
    if input("This item has already been included. Do you want to update it? (y/n): ") == "y":
        input_item(number)
    
else:
    input_item(number)
    
if input("Another entry? y/n:") == 'y':
    replay = True
# Save the updated library to the file
save_library(items, items_lib)


