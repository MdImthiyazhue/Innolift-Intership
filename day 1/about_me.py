# Developer Profile Card
from datetime import date

# Personal Information
name = "Mohamed Imthiyas"
learning = "Python"
favorite_subject = "Data Science"
has_coded_before = True
Goal="Strategy Analyst"

# List variable
hobbies = ["Formula 1", "Aviation", "Programming"]

# Float variable
cgpa = 9.3

# Bonus Challenge: Calculate approximate age in days
birth_date = date(2007, 2, 22)
today = date.today()
age_in_days = (today - birth_date).days
age = age_in_days // 365

# Display Profile Card
print("=" * 40)
print("        MY DEVELOPER PROFILE CARD")
print("=" * 40)

print(f"Name               : {name}")
print(f"Age                : {age}")
print(f"Learning           : {learning}")
print(f"Favorite Subject   : {favorite_subject}")
print(f"Has Coded Before?  : {has_coded_before}")
print(f"Goal               : {Goal}")
print(f"Hobbies            : {', '.join(hobbies)}")
print(f"CGPA               : {cgpa}")
print(f"Approx. Age (Days) : {age_in_days}")

print("=" * 40)

# Print data types
print(f"Type of age: {type(age)}")
print(f"Type of hobbies: {type(hobbies)}")