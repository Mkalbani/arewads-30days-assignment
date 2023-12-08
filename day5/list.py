"""
Day 5: 30 Days of python programming
"""

#empty list
list = []

#Declare a list with more than 5 items
list_2 = ['me', 'you', 'them', 'him', 'she']

#Find the length of your list
list_length = len(list_2)
print(f'The length of the list is {list_length}') 

# Get the first item, the middle item and the last item of the list
first =  list_2[0] #me
middle =  list_2[int(len(list_2)/2)] 
last =  list_2[-1]  
print(f'The first, middle and last items in the list are {first},{middle} and {last} respectively ')

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Musa', 27, 1.83,'Single','Katsina']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)
print(mixed_data_types)

# Print the number of companies in the list
company_length = len(it_companies)
print(len(mixed_data_types))
print(f'The number of companies in the list is {company_length} ')

# Print the first, middle and last company
first_comp = it_companies[0] 
middle_comp = it_companies[len(it_companies)//2] 
last_comp = it_companies[-1]
print(f'The first middle and last companies are {first_comp},{middle_comp} and {last_comp} respectively.')

# Print the list after modifying one of the companies
it_companies[0] = 'Blackberry' 
print(it_companies)

# Add an IT company to it_companies
it_companies.insert(0,'Google')  
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2,'Zipline')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
'#;  '.join(it_companies)

# Check if a certain company exists in the it_companies list.
'Facebook' in it_companies

# Sort the list using sort() method
it_companies.sort() 
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse() 
print(it_companies)

# Slice out the first 3 companies from the list
it_companies[:3]

# Slice out the last 3 companies from the list
it_companies[-3:]

# Slice out the middle IT company or companies from the list
it_companies[len(it_companies)//2:len(it_companies)//2+1]

# Remove the first IT company from the list
it_companies.pop(0)
it_companies

# Remove the middle IT company or companies from the list
it_companies.pop(int(len(it_companies)/2))

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()
it_companies

# Destroy the IT companies list
del it_companies
it_companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy() 
full_stack.index('Redux') 
full_stack.insert(5,'Python') 
full_stack.insert(full_stack.index('Python')+1,'SQL')

"""
Exercises: Level 2
""" 

# The following is a list of 10 students ages:
ages = [11, 32, 13, 34, 26, 15, 19, 29, 25, 18]

# Sort the list and find the min and max age
ages.sort()
print(ages)  
min_age = min(ages)  
max_age = max(ages)  
print(f'The minimum age is {min_age} and the maximum age is {max_age} ')

# Add the min age and the max age again to the list
ages.extend([11,34])

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
ages_length = len(ages)
len(ages)
print(ages[int(len(ages)/2-1)],ages[int(len(ages)/2)]) 
if ages_length % 2 == 0:
  cond1 = ages[ages_length//2]
  cond2 = ages[ages_length//2-1]
  median_age = (cond1 + cond2)/2
else: 
  median_age = ages[ages_length//2]
print(f'The median age of the ages is {median_age}')

# Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages) 
print(f'The average age is {average}')

# Find the range of the ages (max minus min)
rng = max(ages) - min(ages) # 7
print(f'The range of the ages is {rng}')

# Compare the value of (min - average) and (max - average), use abs() method 
abs(min(ages) - average) == abs(max(ages)- average) 

#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
print(countries[len(countries)//2])

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half_countries = countries[:len(countries)//2+1]
second_half_countries = countries[len(countries)//2+1:]

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
CH,RU,US,*scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic
print(scandic)