"""
Exercise 1
"""

alien_color = "green"

print("You have just earned 5 Points!") if alien_color else 0

"""
Exercise 2
"""

if alien_color:
    print("You have earned 5 Points!")
else:
    print("You have earned 10 Points!")


if not alien_color:
    print("You have earned 5 Points!")
else:
    print("You have earned 10 Points!")

"""
Exercise 3
"""
alien_color = "red"

if alien_color == "green":
    print("You have earned 5 Points!")
elif alien_color == "yellow":
    print("You have earned 10 Points!")
else:
    print("You have earned 15 Points!")

alien_color = "yellow"

if alien_color == "green":
    print("You have earned 5 Points!")
elif alien_color == "yellow":
    print("You have earned 10 Points!")
else:
    print("You have earned 15 Points!")

"""
Exercise 4
"""

age = 20

if age < 2:
    print("You are a Baby.")
elif age >= 2 and age < 4:
    print("You are an Toddler")
elif age >= 4 and age < 13:
    print("You are a Kid")
elif age >= 13 and age < 20:
    print("You are a Teenager")
elif age >= 20 and age < 65:
    print("You are a Adult")
elif age >= 65:
    print("You are a Elder")

"""
Exercise 5
"""

favorite_fruits = ["Apples", "BlueBerries", "Oranges"]

if 'Apples' in favorite_fruits:
    print("You really like Apples!")

if 'WaterMelon' in favorite_fruits:
    print("You really like WaterMelon!")

if 'Oranges' in favorite_fruits:
    print("You really like Orange!")

if 'Grapes' in favorite_fruits:
    print("You really like Grapes!")

if 'BlueBerries' in favorite_fruits:
    print("You really like BlueBerries!")