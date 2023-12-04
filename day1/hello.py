""""
 Exercise: Level 1 and 2
"""

# Check the python version you are using
!python --version #Python 3.10.13

#Open the python interactive shell and do the following operations. The operands are 3 and 4.
print(3 + 4)   #addition
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Check the data types of the following data:
print(type(10))                  # Int
print(type(9.8))                # Float
print(type(3.14))                # Float
print(type(4 - 4j))              # Complex
print(type(['Asabeneh', 'Python', 'Finland'])) #list
print(type('Musa'))          # String
print(type('Khalid'))          # String
print(type('Nigeria'))          # String

# Exercise: Level 3
# 1. Write an example for different Python data types such as 
# Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

#number
interger = 1
float_num = 1.0
complext = 1 + 2j

#String
string_exmpl = "This is a string"
Boolean = True
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Tuple = (2, 3, 4, 5, 6, 7, 8, 9, 10)
set_exmpl = {2, 3, 4, 5, 6, 7, 8, 9, 10}
Dictionary = {"name":" Musa", "surname":"Khalid"}

# 2. Find an Euclidian distance between (2, 3) and (10, 8)
import math 
point_1 = [2, 3]
point_2 = [10, 8]

Euclidian_distance = math.dist(point_1, point_2)
print(Euclidian_distance) #Ans = 9.433981132056603