"""
Day 6: 30 Days of python programming
"""

# Create an empty tuple
tpl = ()  

# Create two tuples each containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Abba','Ahmad')
sisters = ('Aisha','Ummi')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# How many siblings do you have?
print(len(siblings)) 

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
parents = ['Baba','Mama']
family_members = siblings
print("Family_members: ",family_members)

#Unpack siblings and parents from family_members
(*siblings,father,mother) = family_members
print("siblings",siblings)
print(father)
print(mother)

# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple','Banana')
vegetables = ('Lettuce','Tomato')
animal_products = ('Meat','Milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_tp)%2 == 0:
    print(food_stuff_tp[len(food_stuff_tp)//2:len(food_stuff_tp)//2+2])
else:
    print(food_stuff_tp[len(food_stuff_tp)//2])
    
# Slice out the first three items and the last three items from food_staff_lt list
print("first three items: ",food_stuff_lt[:3])
print("last three items: ",food_stuff_lt[-3:])

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in  tuple:
print(f"tomato is in food_stuff_tp: {'tomato' in food_stuff_tp}.")

# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
'Estonia' in nordic_countries 
'Iceland' in nordic_countries  
