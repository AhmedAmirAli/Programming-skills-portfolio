"""
Exercise 1
"""

var = "Message"
print(var)
var = "New Message"
print(var)

"""
Exercise 2
"""

quote = "\"Be Water My Friend\" ~ Bruce Lee."
print (quote)

"""
Exercise 3
"""

name = "\tAhmed Amir Hassan Ali\n"
print(name)
print(name.lstrip('\t'))
print(name.rstrip('\n'))
print(name.strip('\t \n'))

"""
Exercise 4
"""

favNum = 99
print("Your Favorite Number is",favNum,end='.\n')

"""
Exercise 5
"""

wallet = 50
usbPrice = 6

print("You can purchase a Total number of {} USB sticks. Your remaining balance is {}£.".format(round(wallet/usbPrice),str(wallet%usbPrice)))

