"""
Day 17: 30 Days of python programming
"""

#names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
# Unpack the first five countries and store them in a variable nordic_countries,
# store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries, last, lastlast = names
print(nordic_countries, last, lastlast)


