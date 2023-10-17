import sys
import datetime
import math

"""
Exercise 1
"""

print("Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are")

"""
Exercise 2
"""

print("Python version information\n" + sys.version + "\t",sys.version_info)

"""
Exercise 3
"""

todayDate = datetime.datetime.now()
print ("Current date and time : ")
print (todayDate.strftime("%Y-%m-%d %H:%M:%S"))

"""
Exercise 4
"""

intro = "The name is "
name = "Ahmed "
age = "i am 21 years old."
print(intro + name + age)

"""
Exercise 5
"""

radius = float(input("Enter radius value: "))
pi = 3.14
circleArea = pi * radius * radius
print(circleArea)