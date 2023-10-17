"""
Exercise 1
"""

def display_message():
    print("Functions.")
display_message()

"""
Exercise 2
"""

def favorite_book(title):
    print(f"One of my Favorite Books is {title}.")
favorite_book("Alice in Borderlands")

"""
Exercise 3 & 4
"""

def make_shirt(size = 'Large', text = 'I Love Python'):
    print(f"Your T-shirt size is {size} and \"{text}\" is your T-shirt design.")

make_shirt()
make_shirt("Medium", "Nike")
make_shirt("Extra Large", "めんどくせー")


"""
Exercise 5
"""

def describe_city(city, country = 'The UAE'):
    print(f"{city} is in {country}.")

describe_city("Shanghai","China")
describe_city("Dubai")
describe_city("Bremen", "Germany")