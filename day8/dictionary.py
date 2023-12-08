"""
Day 8: 30 Days of python programming
"""

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Doggie'
dog['color'] = 'White'
dog['breed'] = 'chuachua'
dog['legs'] = 4
dog['age'] = 2

# Create a student dictionary and add first_name, 
# last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
student = {}
student.update({'first_name':'Musa', 'last_name':'Khalis',
                'gender':'male', 'age':27, 'marital_status':'single',
                'skills':['Python','SQL', 'html'], 'country':'Nig',
                  'city':'Zaria'})

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))  

# Modify the skills values by adding one or two skills
student['skills'].append('Css')
print('Checking the modification:', student)

# Get the dictionary keys as a list
print('dictionary keys as a list: ',student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.pop('city')


# Delete one of the dictionaries
del student