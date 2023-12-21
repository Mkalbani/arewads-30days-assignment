"""
Day 19: 30 Days of python programming
"""

""" 
Write a function which count number of lines and number of words in a text. 
All the files are in the data the folder: 
    a) Read obama_speech.txt file and count number of lines and words 
    b) Read michelle_obama_speech.txt file and count number of lines and words 
    c) Read donald_speech.txt file and count number of lines and words 
    d) Read melina_trump_speech.txt file and count number of lines and words
"""
def count_lines_words(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        words = ' '.join(lines).split()
        word_count = len(words)
    return line_count, word_count

# File paths to each speech
obama_speech_path = '/Users/mkalbani/ArewaDS/arewads-30days-assignment/day19/obama_speech.txt'
michelle_obama_speech_path = '/Users/mkalbani/ArewaDS/arewads-30days-assignment/day19/michelle_obama_speech.txt'
donald_speech_path = '/Users/mkalbani/ArewaDS/arewads-30days-assignment/day19/donald_speech.txt'
melina_trump_speech_path = '/Users/mkalbani/ArewaDS/arewads-30days-assignment/day19/melina_trump_speech.txt'

# Count lines and words in each speech
obama_lines, obama_words = count_lines_words(obama_speech_path)
print(f"Obama's speech - Lines: {obama_lines}, Words: {obama_words}")

michelle_lines, michelle_words = count_lines_words(michelle_obama_speech_path)
print(f"Michelle Obama's speech - Lines: {michelle_lines}, Words: {michelle_words}")

donald_lines, donald_words = count_lines_words(donald_speech_path)
print(f"Donald's speech - Lines: {donald_lines}, Words: {donald_words}")

melina_lines, melina_words = count_lines_words(melina_trump_speech_path)
print(f"Melina Trump's speech - Lines: {melina_lines}, Words: {melina_words}")


#Read the countries_data.json data file in data directory, 
# create a function that finds the ten most spoken languages

import json

def most_spoken_languages(filename, n):
    with open(filename, 'r') as file:
        data = json.load(file)
        languages = {}
        for country in data:
            for language in country['languages']:
                languages[language] = languages.get(language, 0) + 1

        sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
        return sorted_languages[:n]

print(most_spoken_languages(filename='./data/countries_data.json', n=10))
print(most_spoken_languages(filename='./data/countries_data.json', n=3))

# Read the countries_data.json data file in data directory,
# create a function that creates a list of the ten most populated countries
def most_populated_countries(filename, n):
    with open(filename, 'r') as file:
        data = json.load(file)
        countries_population = [{'country': country['name'], 'population': country['population']} for country in data]
        sorted_countries = sorted(countries_population, key=lambda x: x['population'], reverse=True)
        return sorted_countries[:n]

print(most_populated_countries(filename='./data/countries_data.json', n=10))
print(most_populated_countries(filename='./data/countries_data.json', n=3))


#Extract all incoming email addresses as a list from the email_exchange_big.txt file.

def extract_incoming_emails(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        incoming_emails = re.findall(r'(?<=From: )\w+@\w+\.\w+', content)
        return incoming_emails

file_name = 'path/to/email_exchange_big.txt'  # Replace with your file path
incoming_emails_list = extract_incoming_emails(file_name)
print(incoming_emails_list)

"""
Find the most common words in the English language. 
Call the name of your function find_most_common_words, it will take two parameters
 - a string or a file and a positive integer, indicating the number of words. 
 Your function will return an array of tuples in descending order. Check the output

"""

from collections import Counter
import re

def find_most_common_words(text_source, num_words):
    words = []
    
    if isinstance(text_source, str):
        with open(text_source, 'r') as file:
            content = file.read().lower() 
    else:
        content = text_source.lower()  
    words = re.findall(r'\b\w+\b', content)
    word_counter = Counter(words)
    most_common = word_counter.most_common(num_words)
    return most_common

print(find_most_common_words('sample.txt', 10))
print(find_most_common_words('sample.txt', 5))

# Use the function, find_most_frequent_words to find: 
    # a) The ten most frequent words used in Obama's speech 
    # b) The ten most frequent words used in Michelle's speech 
    # c) The ten most frequent words used in Trump's speech 
    # d) The ten most frequent words used in Melina's speech

def find_most_frequent_words(file_path):
    return find_most_common_words(file_path, 10)

# Paths to the speech files
obama_speech_path = '/Users/mkalbani/ArewaDS/arewads-30days-assignment/day19/obama_speech.txt'
michelle_obama_speech_path = '/Users/mkalbani/ArewaDS/arewads-30days-assignment/day19/michelle_obama_speech.txt'
donald_speech_path = '/Users/mkalbani/ArewaDS/arewads-30days-assignment/day19/donald_speech.txt'
melina_trump_speech_path = '/Users/mkalbani/ArewaDS/arewads-30days-assignment/day19/melina_trump_speech.txt'

# Find the ten most frequent words in each speech
obama_most_frequent = find_most_frequent_words(obama_speech_path)
michelle_obama_most_frequent = find_most_frequent_words(michelle_obama_speech_path)
donald_most_frequent = find_most_frequent_words(donald_speech_path)
melina_trump_most_frequent = find_most_frequent_words(melina_trump_speech_path)

# Print the results
print("Obama's speech - Most frequent words:", obama_most_frequent)
print("Michelle Obama's speech - Most frequent words:", michelle_obama_most_frequent)
print("Donald Trump's speech - Most frequent words:", donald_most_frequent)
print("Melina Trump's speech - Most frequent words:", melina_trump_most_frequent)
