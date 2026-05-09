user_profile = {}

get_Name = input("Enter your name: ")
user_profile["userName"] = get_Name

get_Age = input("Enter your age: ")
try:
    user_profile["age"] = int(get_Age)
except ValueError:
    print("Invalid input for age. Please enter a valid number.")
    user_profile["age"] = None
    
get_Favorite_Game = input("Enter your favorite game: ")
user_profile["favoriteGame"] = get_Favorite_Game

print("\nUser Profile:")
for key, value in user_profile.items():
    print(f"{key}: {value}")
    