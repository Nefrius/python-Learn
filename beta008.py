def get_number():
    return input("Enter a number: ")

def multiple_number(number):
    return number * 2

def show(number):
    print(f"The multiple of the number is: {number}")
    
number = get_number()
try:
    number = int(number)
    result = multiple_number(number)
    show(result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
