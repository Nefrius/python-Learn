def get_valid_number():
    while True:
        try:
            number = int(input("Enter a valid number: "))
            if number <= 0:
                print("The number is zero or negative. Please enter a positive number.")
            else:
                print("The number is positive.")
                return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def number_multiple_five(number):
    return number * 5

number = get_valid_number()
result = number_multiple_five(number)
print(f"The result of multiplying the number by 5 is: {result}")