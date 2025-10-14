from datetime import datetime


def calculate_age(date_birth):
    date_now = datetime.now()
    date_birth = datetime.strptime(date_birth, '%d-%m-%Y')

    date_birth_year = int(date_birth.strftime('%Y'))
    date_now_year = int(date_now.strftime('%Y'))
    date_birth_month = int(date_birth.strftime('%m'))
    date_now_month = int(date_now.strftime('%m'))
    date_birth_day = int(date_birth.strftime('%d'))
    date_now_day = int(date_now.strftime('%d'))

    age = date_now_year - date_birth_year
    if date_now_month < date_birth_month:
        age -= 1
    elif date_now_month == date_birth_month and date_now_day < date_birth_day:
        age -= 1
    return age


date_birth = input("Enter your date of birth (dd-mm-yyyy): ")
print(f"You are {calculate_age(date_birth)} years old.")
