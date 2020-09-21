# # This is a human readable message

# '''
# This is also a 
# human readable message
# '''

# # print("This statement will not print")

# '''
# print("These statements")
# print("will not print")
# '''

# # Display two strings on separate lines
# print("Marc")
# print("Hauschildt")

# # Display two print statements on a single line, separated by a space
# print("Hauschildt")

# # Display two strings on a single line, separated by a space
# print("Marc", "Hauschildt")
# print("Marc " + "Hauschildt") # You have to manually add the space here

# # Display two strings on a single line, separated by a period

# # Display a string with a quotation mark
# print("My fantasy football team name is the \"Bootleggers\"")

# # Display a string with a back slash
# print("C:\\Users\\k0519415")

# # Display a string with a new line escape
# print("The quick brown fox\njumped over the lazy dog")

# # Display a string with a tab character
# name = "Jennifer"
# age = 19
# print("Name\t\tAge")
# print(name + "\t" + str(age))

# # Display decimals rounded to two decimal places
# print("Product\t\tPrice")
# print("Bananas\t\t" + "$" + format(0.789, ".2f"))
# print("Apples\t\t" + "$" + format(1.211, ".2f"))

# # Display commas separating large numbers with decimals aligned
# print("Product\t\tPrice")
# print("Bugatti\t\t" + "$" + format(1000000, "12,.2f"))
# print("F-150\t\t" + "$" + format(55000, "12,.2f"))

# # Display commas separating large numbers with decimals aligned
# print("How a baby spends its day:")
# print("Eating\t\t" + format(0.25, ".0%"))
# print("Sleeping\t" + format(0.75, ".0%"))

# print("I am " + str(19) + " years old")

# score = 0
# score = score + 20
# print(score) # 20
# score += 20
# print(score) # 40
# score = score - 15
# print(score) # 25
# score -= 15
# print(score) # 10

# import math

# print(math.pow(2, 3)) # 8.0 - similar to 2 ** 3, but the result is a float
# print(math.sqrt(25)) # 5.0 - square root
# print(math.pi) # 3.141592653589793
# print(math.ceil(2.5)) # 3 - round up to nearest integer
# print(math.floor(2.5)) # 2 - round down to nearest integer
# print(round(2.555, 2)) # 2.56 - round up or down
# print(round(2.554, 2)) # 2.55 - round up or down
# print(math.fabs(-10)) # 10.0 - absolute value, distance from 0

# side1Length = 3
# side2Length = 4
# hypotenuse = math.sqrt(side1Length ** 2 + side2Length ** 2) # Pythagorean theorem
# print(hypotenuse) # 5.0

# radius = 3
# areaOfCircle = math.pi * math.pow(radius, 2)
# print(areaOfCircle)

'''
Problem 1. Superfluous Buns
Format:
 - variable_name, data_type, data_source, example
Input(s): 
  - number_of_guests, int, from the user, 125
  - hotdogs_per_guest, float, from the user, 1.25
  - HOTDOGS_PER_PACK, int, constant, 8
  - BUNS_PER_PACK, int, constant, 12
Process(es): 
  - min_hotdogs_needed, int, math.ceil(number_of_guests * hotdogs_per_guest), 157
  - hotdog_packages, int, math.ceil(min_hotdogs_needed / HOTDOGS_PER_PACK), 20
  - hotdog_count, int hotdog_packages * HOTDOGS_PER_PACK, 160
  - bun_packages, int, math.ceil(hotdog_count / BUNS_PER_PACK), 14
  - bun_count, int, bun_packages * BUNS_PER_PACK, 168
  - extra_hotdogs, int, hotdog_count - min_hotdogs_needed, 3
  - extra_buns, int, bun_count - min_hotdogs_needed, 11
Output(s):
  - hotdog_packages
  - bun_packages
  - extra_hotdogs
  - extra_buns
'''
# # Type your code here
# import math

# number_of_guests = int(input("How many guests?")) #125
# dogs_per_guest = float(input("How many hotdogs per guest?")) #1.25
# DOGS_PER_PACK = 8
# BUNS_PER_PACK = 12
# min_dogs_needed = math.ceil(number_of_guests * dogs_per_guest) #157.0
# print(min_dogs_needed)
# hotdog_packages = math.ceil(min_dogs_needed / DOGS_PER_PACK) #20.0
# print(hotdog_packages)