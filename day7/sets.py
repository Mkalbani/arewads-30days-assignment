"""
Day 7: 30 Days of python programming
"""

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print('Length of it_companies set: ', len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)  

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Cisco','Dell','Salesforce','Nokia'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Cisco')
# What is the difference between remove and discard ?
#The discard() method removes the specified item from the set. 
# This method is different from the remove() method, because the remove() method will raise an error 
# if the specified item does not exist, and the discard() method will not.

# Join A and B
print('Result of join: ', A.union(B)) 

# Find A intersection B
print('A intersection B: ', A.intersection(B))

# Is A subset of B
print('A is a subset of B : ', A.issubset(B)) # True

# Are A and B disjoint sets
print('A and B are disjoint: ', A.isdisjoint(B)) #False

# Join A with B and B with A: same thing
print('A with B: ', A.union(B))
print('B with A: ', B.union(A))

# What is the symmetric difference between A and B
print('Symmetric difference of A and B: ',A.symmetric_difference(B)) 

# Delete the sets completely
del A
del B

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print('age_set is smaller than age(the list): ', len(age_st) < len(age))

#Explain the difference between the following data types: string, list, tuple and set
"""
List: Mutable (modifiable).
Tuple: Immutable (non-modifiable).
Set: Mutable, but elements inside must be immutable.
Dictionary: Key-value pairs -- Mutable; keys are immutable, but values can change.
"""

# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.

sentence = 'I am a teacher and I love to inspire and teach people'
convert_to_set = set(sentence.split())
print(len(convert_to_set)) #ten unique
