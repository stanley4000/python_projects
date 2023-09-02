#############################
# Project as assigned in Harvard/edX 2023 CS50:
# https://cs50.harvard.edu/x/2023/problems/6/figlet/
# Code uses figlet python port from:
# https://pypi.org/project/pyfiglet/0.7/
####################################################

import sys
from pyfiglet import Figlet, FigletFont
from random import randint


# Check for correct usage (e.g., python figlet.py || python figlet.py -f <fontname> || python figlet.py --<fontname>)
args = len(sys.argv) - 1 
# Check for correct number of arguments
if args != 0 and args != 2: 
    print("Invalid Usage")
    sys.exit(1)
# print(f"arguments: {args}") # print for debugging

# Check if flag is valid
elif args != 0 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
    print("Invalid usage")
    sys.exit(1)

# Assign command line font or assign random font
# NOTE: FigletFont getFonts method returns font names as strings in a list
font_list = FigletFont.getFonts()
if args > 0:
    font = sys.argv[2]
else:
    index = randint(1, len(FigletFont.getFonts()))
    font = font_list[index]
    random_font = True

# Validate font choice
if not font in font_list:
    print("Invalid font choice")
    sys.exit(1)

# Prints input in selected font
f = Figlet(font=font)

text = f.renderText(input("Input: "))
print(f"Output:\n{text}")
#prints name of font if randomly assigned
if random_font:
    print(f"font = {font}")
