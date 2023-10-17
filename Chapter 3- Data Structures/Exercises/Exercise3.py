"""
Exercise 1
"""

names = ["Matsumoto", "Zack", "Sarah", "Chen"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])

"""
Exercise 2
"""

print("Congrats " + names[0] + " on Winning the Tournament!")
print("Congrats " + names[1] + " on Winning the Tournament!")
print("Congrats " + names[2] + " on Winning the Tournament!")
print("Congrats " + names[3] + " on Winning the Tournament!")

"""
Exercise 3
"""

methodOfTransport = ["Car", "Jet", "Walking"]

print("My " + methodOfTransport[0] + " broke down yesterday.")
print("I will go to Sydney via " + methodOfTransport[1] + ".")
print("We prefer " + methodOfTransport[2] + " to School.")

"""
Exercise 4
"""

invList = ["Mohamed", "Carlos", "Andrew"]

print("I would like to invite Sir." + invList[0] + " to attend Dinner at My PLace one the 30th of this Month.")
print("I would like to invite Sir." + invList[1] + " to attend Dinner at My PLace one the 30th of this Month.")
print("I would like to invite Sir." + invList[2] + " to attend Dinner at My PLace one the 30th of this Month.")

"""
Exercise 5
"""

invList[0] = "Viktor"

print("I would like to invite Sir." + invList[0] + " to attend Dinner at My PLace, Tonight.")
print("I would like to invite Sir." + invList[1] + " to attend Dinner at My PLace, Tonight.")
print("I would like to invite Sir." + invList[2] + " to attend Dinner at My PLace, Tonight.")
print("Unfortunately Sir.Mohamed would not be able to join us Tonight.")

"""
Exercise 6
"""

print("Due to certain circumstances, Only 2 seats are available tonight.")

rmList = invList.pop(2)
print("We wont be able to Hold your seat for Tonight, We Apologize for the inconvenience.")

print("We would like to inform you that your seat is still Reserved for Tonights Dinner, Sir." + invList[0])
print("We would like to inform you that your seat is still Reserved for Tonights Dinner, Sir." + invList[1])

del invList[1]
del invList[0]

print(invList)

"""
Exercise 7
"""

likeToVisit = ["Niagara Falls", "Tibet", "Guilin", "Tokyo", "Zhangjiajie"]
print(likeToVisit)

print("Sorted List:",sorted(likeToVisit))
print(likeToVisit)

likeToVisit.reverse()
print("Reversed List:", likeToVisit)

likeToVisit.reverse()
print(likeToVisit)

likeToVisit.sort()
print(likeToVisit)

likeToVisit.sort(reverse=True)
print(likeToVisit)

