from art import logo
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide
#I'm unsure why we don't need to include () after function names here.
def calculator():
#NOTE: this function is here to facilitate RECURSION (essentailly restarting the program)
    should_continue = True
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    while should_continue == True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.:")
        if response == 'y':
            should_continue = True
            num1 = answer
        else:
            should_continue = False
            calculator()
           
calculator()
