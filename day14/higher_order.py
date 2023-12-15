"""
Day 14: 30 Days of python programming
"""
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

########
# Exercises: Level 1

# Explain the difference between map, filter, and reduce.
# Map: map() 
# This applies a given function to each item of an iterable (like a list)
# and returns a new iterable containing the results. 
# It takes two parameters: the function to apply and the iterable to apply it to.

# Filter: filter() 
# This applies a function to each element of an iterable and returns only the elements 
# for which the function returns True. It also takes two parameters: the function for 
# filtering and the iterable to filter.

# Reduce: reduce() 
# This applies a rolling computation to sequential pairs of values in an 
# iterable and returns a single result. It's in the functools module in Python 3 and needs to be imported.
#  It requires a function that accepts two arguments and the iterable to be reduced.

# Explain the difference between higher order function, closure and decorator
# Higher-Order Function: 
# A higher-order function is a function that either takes
#  one or more functions as arguments or returns a function as its result. Examples in Python include map(), 
# filter(), and reduce().

# Closure: 
# A closure is a function that remembers the values from its enclosing lexical scope even when 
# the program flow is no longer in that scope. It encapsulates the state of its surrounding environment. 
# Closures are created when a nested function accesses variables from its enclosing scope.

# Decorator: 
# A decorator is a design pattern in Python that allows modifying or extending the behavior of a 
# callable (functions, methods, or classes) without permanently modifying the callable itself. 
# It starts with the @ symbol and is placed just before the function or method to be decorated.


# Define a call function before map, filter or reduce, see examples.
# The callable function in Python returns True if the specified object is 
# callable (can be called as a function) and False otherwise. It checks if the 
# given object appears to be callable by verifying whether 
# it's an instance of a class implementing the __call__() method or if it's a
# built-in function or a user-defined function.
# Example demonstrating the `callable` function
callable_map = map(lambda x: x.upper(), countries)
print(callable(callable_map))  # Output: False

callable_filter = filter(lambda x: len(x) > 6, names)
print(callable(callable_filter))  # Output: False

from functools import reduce
callable_reduce = reduce(lambda x, y: x + y, numbers)
print(callable(callable_reduce))  # Output: True

# Use for loop to print each country in the countries list.
for country in countries:
    print(country)
# Use for to print each name in the names list.
for name in names:
    print(name)
# Use for to print each number in the numbers list.
for number in numbers:
    print(number)

#######
#Excercise2

# Use map to create a new list by changing each country to uppercase in the countries list
countries_upper = list(map(lambda country: country.upper(), countries))
print(countries_upper)

# Use map to create a new list by changing each number to its square in the numbers list
numbers_square = list(map(lambda number: number ** 2, numbers))
print(numbers_square)

# Use map to change each name to uppercase in the names list
names_upper = list(map(lambda name: name.upper(), names))
print(names_upper)

# Use filter to filter out countries containing 'land'.
countries_filtered_land = list(filter(lambda country: 'land' not in country.lower(), countries))
print(countries_filtered_land)

# Use filter to filter out countries having exactly six characters.
countries_filtered_six_chars = list(filter(lambda country: len(country) != 6, countries))
print(countries_filtered_six_chars)

# Use filter to filter out countries containing six letters and more in the country list.
countries_filtered_six_letters = list(filter(lambda country: len(country) < 6, countries))
print(countries_filtered_six_letters)

# Use filter to filter out countries starting with an 'E'
countries_filtered_e = list(filter(lambda country: not country.startswith('E'), countries))
print(countries_filtered_e)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))
# Declare a function called get_string_lists which takes a 
# list as a parameter and then returns a list containing only string items.
numbers = [1, 'two', 3, 'four', 5, 'six']
result = reduce(lambda x, func: func(x), [map(str, numbers), get_string_lists, lambda x: list(filter(lambda s: s.isdigit(), x))])
print(result)
# Use reduce to sum all the numbers in the numbers list.

# sum_numbers = reduce(lambda x, y: x + y, numbers)
# print(sum_numbers)
# Use reduce to concatenate all the countries and to produce this sentence: 
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countrie
sentence = reduce(lambda x, y: x + ', ' + y, countries) + ' are north European countries.'
print(sentence)

# Declare a function called categorize_countries that returns a list of countries with some
# common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries import countries

def categorize_countries(listed_countries):
    comm_patterns = ['ia', 'island', 'land', 'stan']
    categorized = {pattern: [] for pattern in comm_patterns} 
    
    for country in listed_countries:
        for pattern in comm_patterns:
            if pattern in country.lower(): 
                categorized[pattern].append(country)
                
    return categorized
result = categorize_countries(countries)
for pattern, countries_list in result.items():
    print(f"Countries with pattern '{pattern}': {countries_list}")

# Create a function returning a dictionary, where keys stand for starting
#  letters of countries and values are the number of country names starting with that letter.
def count_countries_starting_with_letters(country_list):
    letter_count = {}
    for country in country_list:
        first_letter = country[0].upper()  
        if first_letter.isalpha():  
            if first_letter in letter_count:
                letter_count[first_letter] += 1
            else:
                letter_count[first_letter] = 1
    return letter_count
country_counts = count_countries_starting_with_letters(countries)
print(country_counts)
# Declare a get_first_ten_countries function - it returns a list of first ten countries from
#  the countries.js list in the data folder.
def get_first_ten_countries(country_list):
    return country_list[:10]
first_ten = get_first_ten_countries(countries)
print(first_ten)
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(country_list):
    return country_list[-10:]
last_ten = get_last_ten_countries(countries)
print(last_ten)

#####
# Exercise 3
# Use the countries_data.py
#  (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
    # Sort countries by name, by capital, by population
    # Sort out the ten most spoken languages by location.
    # Sort out the ten most populated countries.

from countries_data import countries

# Sort countries by name, capital, and population
sorted_by_name = sorted(countries, key=lambda x: x['name'])
sorted_by_capital = sorted(countries, key=lambda x: x['capital'])
sorted_by_population = sorted(countries, key=lambda x: x['population'], reverse=True)  # Sort by population in descending order

# Sort the ten most spoken languages by location
all_languages = []
for country in countries:
    all_languages.extend(country['languages'])
language_count = {}
for language in all_languages:
    language_count[language] = language_count.get(language, 0) + 1
sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]

# Sort the ten most populated countries
sorted_by_population_top_10 = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]

# Outputs
print('Countries sorted by name:')
for country in sorted_by_name:
    print(country['name'])

print('\nCountries sorted by capital:')
for country in sorted_by_capital:
    print(country['capital'])

print('\nCountries sorted by population:')
for country in sorted_by_population:
    print(country['name'], country['population'])

print('\nTen most spoken languages:')
for language, count in sorted_languages:
    print(f'{language}: {count}')

print('\nTen most populated countries:')
for country in sorted_by_population_top_10:
    print(country['name'], country['population'])
