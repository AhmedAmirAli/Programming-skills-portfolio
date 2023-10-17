"""
Exercise 1
"""

toppings = []
while True:
    i = input("Enter pizza topping: ")
    if i.lower() == "quit":
        break
    else:
        toppings.append(i)
        print(f"{i} have been added to your pizza toppings.")

print("Your Toppings are:")
for i in toppings:
    print(i,end="\n")
# print(', '.join(toppings))
print("Thank you for ordering from us! See you Soon.")

"""
Exercise 2
"""

while True:
    age = int(input("Enter you age: "))

    if age == 0:
        break
    elif age < 3:
        print("Your Ticket is Free!")
    elif age >= 3 and age <= 12:
        print("Your Ticket Fee is $10.")
    else:
        print("Your Ticket Fee is $15.")

"""
Exercise 3
"""

# while True:
#     print(">:D")

"""
Exercise 4 & 5
"""

sandwich_orders = ["Pastrami","Shawarma", "Pastrami","Burger","Pastrami","Burrito"]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami sandwiches.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

for i in sandwich_orders:
    print("I have made your",i,"sandwich.")
    finished_sandwiches.append(i)
print(finished_sandwiches)


