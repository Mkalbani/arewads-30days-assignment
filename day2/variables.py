"""
Day 2: 30 Days of python programming
"""
# Exercises: Level 1
first_name = "Musa"
last_name = "Khalid"
full_name = "Musa Khalid"
country = "Nigeria"
city = "Kaduna"
age = 18
year = 2000
is_married = False
is_true = True
is_light_on = False
# Declaring multiple variables in one line
first_name, last_name, full_name = "Musa", "Khalid", "Musa Khalid"

#Exercises: Level 2
# Using the len() built-in function, find the length of your first name
# Compare the length of your first name and your last name
compared_length = len(first_name) - len(last_name)
print(compared_length) #-2

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
total = num_one + num_two #addition
print(total)
# subtract
diff = num_one + num_two 
print(diff)
# product
product = num_one * num_two
print(product)
#division
division = num_one / num_two
print(division)
#remainder
remainder = num_one % num_
#exp
exp = num_one ** 2
print(exp)
#floor_division
floor_division = num_one // num_two

"""The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area."""

#Area of circle
from math import pi
area_of_circle = pi * 30 ** 2
print(area_of_circle)

# circumference of a circle 
circum_of_circle = 2 * pi * 30
print(circum_of_circle)

#Using user input, calculate the area
radius = float(input("enter radius: "))
area_of_circle_user = pi * radius ** 2
print(area_of_circle_user)
# Use the built-in input function to get first name, 
# last name, country and age from a user and store the value to their corresponding variable names
first_name = str(input("enter first name: "))
last_name = str(input("enter last name: "))
country = str(input("enter country: "))
age = int(input("enter age: "))