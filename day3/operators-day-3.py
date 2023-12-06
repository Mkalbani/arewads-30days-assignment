"""
Day 3: 30 Days of python programming
"""
#declaration of age, height and complex number
age = 27
height = 1.83
complx = 2 + 3j
# Write a script that prompts the user to enter base 
# and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base:"))
height = float(input("Enter height:"))
area = 0.5 * base * height
print("The area of the triangle is: ", area)

#Write a script that prompts the user to 
# enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print("The perimeter of the triangle is: ", perimeter)

#Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
print("The area of the rectangle is ",area, " square meters")

# Get radius of a circle using prompt. 
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
import math
r = float(input("Input the radius of the circle: "))
area = math.pi * r ** 2
perimeter = 2 * math.pi * r 
print("The area of the circle is: ",area, " and ", "the perimeter is : ", perimeter)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = 0
y = 2*x - 2
y = 0
x = (2+y)//2
print(x) #ans = 2

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m = (y2-y1)/(x2-x1)
print("m: ", m)

#Compare the slopes in tasks 8 and 9.
print(m>x)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = int(input("enter x: "))
y = x**2 + 6*x + 9
print(y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_python = len('python')
length_dragon = len('dragon')
print(length_python != length_dragon)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('check if "on" in "python" and "on" in "jargon": ',"on" in "python" and "on" in "jargon")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('"jargon" is in "I hope this course is not full of jargon: "',"jargon" in "I hope this course is not full of jargon")

#There is no 'on' in both dragon and python
print("There is no 'on' in both dragon and python: ", 'on' not in ('dragon' and 'python'))

# Find the length of the text python and convert the value to float and convert it to string
print(str(float(len("python"))))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input())
if number % 2 == 0:
    print('number is even')
print('number is odd')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print("Check: ", 7 // 3 == 2.7) 

#Check if type of '10' is equal to type of 10
print("Check if!: ", type('10')== type(10)) 

#Check if int('9.8') is equal to 10
print("Check if!: ", type('9.8')== type(10)) 

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
a = float(input("Enter hours per week:"))
b = float(input("Enter rate per hour: "))
c = x * y
print("Your weekly earning is: ", c)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter the number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60 
print("You have lived for ",seconds, " seconds.")

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print('1\t1\t1\t1\t1\n2\t1\t2\t4\t8\n3\t1\t3\t9\t27\n4\t1\t4\t16\t64\n5\t1\t5\t25\t125')







