"""
Exercise 1
"""

person = {'firstName':"Ahmed",'lastName':"Ali",'age':21,'city':"Dubai"}
print(person,end="\n")

"""
Exercise 2
"""

words = {'Terminal':'text based interface to interact with Computer.','Pointers':'data stored in memory.','Loops':'a block of code that runs based on condition.','API':'code libraries that preform a certain task.','Git':'version control program.'}

print("Terminal:\n\t" + words['Terminal'])
print("Pointers:\n\t" + words['Pointers'])
print("Loops:\n\t" + words['Loops'])
print("API:\n\t" + words['API'])
print("Git:\n\t" + words['Git'])


"""
Exercise 3
"""    

for key, value in words.items():
    print(f"{key}:\n\t{value}" + "\n")

nWords = words.update(
    {
        'Argument':"a value that is passed through a function.",'Dictionary':"a array that holds its indexes as key values.",'Function':"a block of code that excutes when called.",'Class':"user defined object custom template",'interpreter':"excutes high level language without compiling code."
    }
)
for key, value in words.items():
    print(f"{key}:\n\t{value}" + "\n")

"""
Exercise 4
"""

rivers = {
    'Nile':"Egypt",
    'Amazon':"Brazil",
    'Yangtze':"China"
}

for key, value in rivers.items():
    print(f"The {key} runs through {value}.")
for key in rivers.keys():
    print(key)
for value in rivers.values():
    print(value)

"""
Exercise 5
"""

pet1 = {
    'Animal':"Cat",
    'Owner':"Jhon"
}
pet2 = {
    'Animal':"Dog",
    'Owner':"Lara"
}
pet3 = {
    'Animal':"Fish",
    'Owner':"Aaron"
}

pets = [pet1,pet2,pet3]
for i in pets:
    print(i)