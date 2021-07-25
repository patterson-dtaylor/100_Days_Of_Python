calculator_power = True
first_calculation = True
total = 0

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator(function=None, num1=0, num2=0):
    if function == "+":
        return add(num1, num2)
    elif function == "-":
        return subtract(num1, num2)
    elif function == "*":
        return multiply(num1, num2)
    elif function == "/":
        return divide(num1, num2)

def calculator_functionality(result, recaculate="no"):
    if recaculate == "yes":
        function = input("What function would you like to use? (+,-,*,/) ")
        num1 = result
        num2 = float(input("What is the second number you want to use? "))
        answer = calculator(function, num1, num2)
        print((f"The answer is {answer}."))
        return answer
    elif recaculate == "no":
        function = input("What function would you like to use? ")
        num1 = float(input("What is the first number you want to use? "))
        num2 = float(input("What is the second number you want to use? "))
        answer = calculator(function, num1, num2)
        print((f"The answer is {answer}."))
        return answer 

while calculator_power:
    if first_calculation:
        total = 0
        result = calculator_functionality(total)
        total += result
    user_choice = input(f"Would you like to use {result} in a new equation, startover, or poweroff (yes, no, off) ")
    if user_choice == "yes":
        first_calculation = False
        result = calculator_functionality(total, recaculate="yes")
        total = 0 
        total += result
    if user_choice == "no":
        first_calculation = True
    elif user_choice == "off":
        print("Powering off...")
        break