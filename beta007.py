def create_user():
    user = {
        "userName": input("Enter your name: "),
        "age": None,
    }
    
    get_Age = input("Enter your age: ")
    try:
        user["age"] = int(get_Age)
    except ValueError:
        print("Invalid input for age. Please enter a valid number.")
        user["age"] = None
        
    print("\nUser Profile:")
    for key, value in user.items():
        print(f"{key}: {value}")

create_user()