import json

# Load the library from a JSON file
def load_library(items_lib):
    try:
        with open(items_lib, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty dictionary
        return {}

# Save the library to a JSON file
def save_library(items, items_lib):
    with open(items_lib, 'w') as file:
        json.dump(items, file)

exit_flag = False

while not exit_flag:
    # Enter data into library
    number = int(input("Enter item number: "))
    question = input("Enter text of question: ")
    option_0 = input("Enter response 0: ")
    option_1 = input("Enter response 1: ")
    option_2 = input("Enter response 2: ")
    option_3 = input("Enter response 3: ")
    options = [option_0, option_1, option_2, option_3]
    correct_response = input("Enter index for correct response (0-3): ")

    # Load the existing library
    items_lib = 'items_lib.json'
    items = load_library(items_lib)

    # Remove any existing entry with the same key
    items.pop(str(number), None)

    # Add the new entry to the library
    items[number] = {
        'question': question,
        'options': options,
        'correct_response': correct_response
    }

    # Save the updated library to the file
    save_library(items, items_lib)

    print(items[number])

    # Ask if the user wants to enter more data
    choice = input("Do you want to enter more data? (yes/no): ")
    if choice.lower() != 'yes':
        exit_flag = True