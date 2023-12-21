"""
Day 18: 30 Days of python programming
"""

# What is the most frequent word in the following paragraph?
#     paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
import re

from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Remove punctuation and convert to lowercase
cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph).lower()

# Split the paragraph into words and count the occurrences
words = re.findall(r'\w+', cleaned_paragraph)
word_count = Counter(words)

# Find the most common word
most_common_word = word_count.most_common(1)
print(f"The most frequent word is '{most_common_word[0][0]}' and it appears {most_common_word[0][1]} times.")

#The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 
# in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
# Extract these numbers from this whole text and find the distance between the two furthest particles.
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract numbers from the text
numbers = re.findall(r'-?\d+', text)

# Convert the extracted strings to integers
points = [int(num) for num in numbers]

# Sort the points
sorted_points = sorted(points)

# Find the distance between the two furthest particles
distance = sorted_points[-1] - sorted_points[0]

print(f"The furthest distance between particles is: {distance}")

# Write a pattern which identifies if a string is a valid python variable
import re

def is_valid_variable(variable):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable))

# Test cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True

""" 
Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

print(clean_text(sentence));
I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
"""

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()

def most_frequent_words(text):
    words = text.split()
    word_count = Counter(words)
    most_common = word_count.most_common(3)
    return most_common

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))  


