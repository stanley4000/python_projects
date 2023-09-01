#############################
# Project as assigned in CS50:
# https://cs50.harvard.edu/x/2023/problems/6/figlet/
####################################################

import sys
from pyFiglet import Figlet

# Check for correct usage (e.g., python figlet.py || python figlet.py -f <fontname> || python figlet.py --<fontname>)
args = len(sys.argv) - 1 
# Check for correct number of arguments
if args != 0 and args != 2: 
    print("Invalid Usage")
    sys.exit()
# print(f"arguments: {args}") #print for debugging

# Check if flag is valid
elif args != 0 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
    print("Invalid usage")
    sys.exit()

# TODO: validate font choice
# Assign font
if args > 0:
    font = sys.argv[2]
# TODO: choose random font
else:
    font = 'slant'
# print(f"font = {font}") #print for debugging

# Prints input in selected font
f = Figlet(font=font)

text = f.renderText(input("Input: "))
print(f"Output:\n{text}")
