#NOTE: format for list test_items: (number, "Question 2", ["Option A", "Option B", "Option C", "Option D"], correct_index)
from test_items import *
import random
random_element = random.choice(test_items)
number = random_element[0]
question = random_element[1]
#options = random_element[2][:4]'int' object is not subscriptable
correct = random_element[5]

print(f"{number}. {question}")
