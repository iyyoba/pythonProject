# Exercise 1
seasons = "winter", "spring", "summer", "autumn"
month_number = int(input("Enter month number (1 - 12): "))

i = month_number // 3
if month_number == 12:
    i = 0
print("The month is in " + seasons[i] + ".")