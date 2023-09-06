# Validates credit card number, as per Luhn's algorithm
# https://cs50.harvard.edu/x/2023/psets/1/credit/

from cs50 import get_int

# Get cc as an int (note: instructions indicate to use cs50 library get_int())
number = get_int("Enter card number: ")
num_string = str(number)

# Note: code for checksum is too complicated. Should probably be rewritten to avoid extra steps.

# multiply every other digit (starting with [-2]) by 2
mult_digits = []
count = 0
while count <= (len(num_string) / 2) - 1:
    mult_digits.append(int(num_string[-2 * (count + 1)]) * 2)
    count += 1
# add all digits of result, add to remaining digits, check that last digit is 0
sum = 0
count = 0
while count <= len(mult_digits) - 1:
    if mult_digits[count] < 10:
        sum += mult_digits[count]
        count += 1
    else:
        sum += 1 + mult_digits[count] % 10
        count += 1

count = 0
while (count + 1) * (-2) + 1 >= (len(num_string) * -1):
    sum += int(num_string[(count + 1) * (-2) + 1])
    count += 1

# # Print variables for debugging
# print(f"checksum = {sum}")
# digits = len(num_string)
# print(f"digits = {digits}")
# print(num_string[0])
# print(num_string[1])

# Checksum (last digit must be 0)
if not sum % 10 == 0:
    check_card = "INVALID"

elif (
    (len(num_string) == 15)
    and (num_string[0] == "3")
    and ((num_string[1]) == "4" or (num_string[1] == "7"))
):
    check_card = "AMEX"

elif (
    len(num_string) == 16
    and num_string[0] == "5"
    and int(num_string[1]) > 0
    and int(num_string[1]) < 6
):
    check_card = "MASTERCARD"

elif ((len(num_string) == 13 or len(num_string) == 16)) and num_string[0] == "4":
    check_card = "VISA"

else:
    check_card = "INVALID"

print(check_card)

