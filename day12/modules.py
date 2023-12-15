"""
Day 12: 30 Days of python programming
"""


# Writ a function which generates a six digit/character random_user_id.
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

print(random_user_id());
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    length, count = map(int, input("Enter the length and number of IDs (separated by space): ").split())
    for _ in range(count):
        user_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        print(user_id)

print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form

###
# Exercises: Level 2

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num):
    hexa_colors = []
    for _ in range(num):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hexa_colors.append(color)
    return hexa_colors

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    rgb_colors = []
    for _ in range(num):
        color = f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"
        rgb_colors.append(color)
    return rgb_colors

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, num):
    if color_type == 'hexa':
        return list_of_hexa_colors(num)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))  # ['#b334ef']
print(generate_colors('rgb', 3))   # ['rgb(5,55,175)', 'rgb(50,105,100)', 'rgb(15,26,80)']
print(generate_colors('rgb', 1))   # ['rgb(33,79,176)']

#Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(input_list):
    shuffled = input_list[:]
    random.shuffle(shuffled)
    return shuffled
my_list = [1, 2, 3, 4, 5]
print("Shuffled list:", shuffle_list(my_list))
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def generate_seven_unique_numbers():
    return random.sample(range(10), 7)
print("Seven unique random numbers:", generate_seven_unique_numbers())

