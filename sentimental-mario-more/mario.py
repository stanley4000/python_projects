# Prompt user for int input <= 8
height = 0
while height > 8 or height < 1:
    height = int(input("Enter height: "))

#loop through height of pyramid
i = 0
while i < height:
    # print spaces 
    j = 0
    while j < height - i - 1:
        print(' ', end = "")
        j += 1
    # print hashes
    k = 0
    while k < i + 1:
        print("#", end = "")
        k += 1
    # separator spaces
    print("  ", end = "")
    # repeat hashes
    k = 0
    while k < i + 1:
        print("#", end = "")
        k += 1
    # repeat spaces
    j = 0
    while j < height - i - 1:
        print(' ', end = "")
        j += 1
    # Return and increment line
    print()
    i += 1
    

