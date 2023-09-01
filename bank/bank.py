###################
# Program based on Seinfeld's "bank" episode: practice problem from CS50
# Output represents payment for any greeting except "hello" (case ignored)
###################

greeting = input("Greeting: ").lower()
print(greeting)
if greeting == "hello":
    pay = 0
elif greeting[0] == "h":
    pay = 20
else: 
    pay = 100

print(f"Payment: ${pay}")