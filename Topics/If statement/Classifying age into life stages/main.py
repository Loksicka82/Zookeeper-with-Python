# Read the user's age
age = int(input())

# Check the age and print the corresponding category
# TODO: Write your if statement here
if age < 18:
    print('Minor')
if age >= 18:
    if age < 65:
        print("Adult")
if age >=65:
    print("Senior")