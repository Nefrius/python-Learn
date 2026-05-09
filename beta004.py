def get_number(numberOne):
    try:
        number = int(numberOne)
        return number
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None
    
numberOne = input("Enter a number: ")
number = get_number(numberOne)

def square_number():
    return number ** 2

result = square_number()

print (f"The square of {number} is: {result}")
