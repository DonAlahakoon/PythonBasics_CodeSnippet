# Declaring varibales
name = "Mike"       #Strings
age = 3.0           #Integer
gpa = 3.5           #Decimal
is_tall = True      #Bolean

name = "John";

#Printing
# print("Your name is "+name)
# print("Your name is", name)

# Casting and Converting
print(int(3.14))
print(float(4))
print((str(True)))
print(int("50") + int("70"))
print("\n")

#Strings

greeting = "Hello"

print(len(greeting))
print(greeting[0])
print(greeting.find("llo")) #finds and tell whether the string is inside greeting if so return index
print(greeting.find("z"))   # return index if available
print(greeting[2:])
print(greeting[2:3])
print("\n")

#numbers

print(2*3)
print(2**3)
print(10%3)
print((1+2)*3)
print(10/3)
print("\n")

num = 10
num+=100
print(num)
print("\n")

import math
print(pow(2,3))
print(math.sqrt(144))
print(round(2.3))
print("\n")


#User Input
# name = input("Enter your name:")
# print("Hello",name + "!")

# num1 = int(input("Enter First num:"))
# num2 = int(input("Enter second num:"))
# print(num1 + num2)

#Lists
lucky_numbers = [4,5,"fifteen",17,23,43.0]

lucky_numbers[0] = 90
print(lucky_numbers[0])
print(lucky_numbers[-1]) #last member of the list
print(lucky_numbers[2:])
print(lucky_numbers[2:4])
print(len(lucky_numbers))


# N dimentional list
numberGrid = [[1,2],[3,4]]
numberGrid [0][1] = 99
print(numberGrid[0][0])
print(numberGrid[0][1])
print("\n")


# List Functions
friends = []
friends.append("Oscar")
friends.append("Angela")
friends.insert(1,"Kevin")

friends.remove("Kevin")
print(friends.index("Oscar"))
print(friends.count("Angela"))
friends.sort()
print(friends)
friends.clear()
print(friends)
print("\n")


# Tuples (looks like "list" except parens; but cannot modify)
lucky_numbers = (4,8,"fifteen",16,17,18,43.0)

# lucky_numbers[0] = 90; can't modify
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])
print(len(lucky_numbers))