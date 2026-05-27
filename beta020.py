import datetime

get_input = input("Your Age: ")

def datetime_calculator(age: int) -> str:
    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    return f"You were born in {birth_year}."

date_time_result = datetime_calculator(int(get_input))
print(date_time_result)