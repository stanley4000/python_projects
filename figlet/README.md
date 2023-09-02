#############################
 Project as assigned in Harvard/edX 2023 CS50:
 https://cs50.harvard.edu/x/2023/problems/6/figlet/
 Code uses figlet python module from:
 https://pypi.org/project/pyfiglet/0.7/
####################################################

This program converts any input text to ascii text using the figlet python module. It was developed using Python 3.11.

The program can be run from the command line without flags, in which case a random font will assigned. in order to call a specific font name, add the arguments: -f <"font_name"> OR --font <"font_name">.

If the program is run with no arguments and a random font is assigned, the name of the font will be printed along with the output.

# Use case
$python3 figlet.py -f <"font_name">

OR

$python3 figlet.py

Input: <"text to be formatted">

# Invalid usage
In case the user enters invalid command line arguments or a non-existent font, an error message is printed and the program returns exit code '1'.