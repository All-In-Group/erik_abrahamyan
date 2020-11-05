def get_middle(string):
    """
    :param string: arbitrary some word
    :return: Question 1: Given a string of odd length greater 7, return a string made of the middle three chars of a given String
    """
    if len(string) >= 7:
        middle_index = len(string) // 2
        middle_part_word = string[middle_index-1:middle_index+2]
        return middle_part_word

print(get_middle("JhonDipPeta"))
print(get_middle("JaSonAy"))
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

s1 = "Ault"
s2 = "Kelly"
middle_s1 = len(s2) // 2
new_s = s1[:middle_s1] + s2 + s1[2:]
print(new_s)
print(get_middle("JaSonAy"))
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 3: Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string

s1 = "America"
s2 = "Japan"
middle_letter = len(s1) // 2
new_s = s1[:1] + s2[:1] + s1[middle_letter: middle_letter+1] + s2[-3:]
print(new_s)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 4: Arrange string characters such that lowercase letters should come first

str1 = 'PyNaTive'
sort_str = sorted(str1, reverse=True)
news_s = ''.join(sort_str)
print(news_s)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 5: Count all lower case, upper case, digits, and special symbols from a given string


str1 = "P@#yn26at^&i5ve"
lower_case = []
upper_case = []
digit_case = []
symbol_case = []

for i in str1:
    if i.islower():
        lower_case.append(i)
    elif i.isupper():
        upper_case.append(i)
    elif i.isdigit():
        digit_case.append(i)
    else:
        symbol_case.append(i)

chars = len(lower_case) + len(upper_case)
digits = len(digit_case)
symbols = len(symbol_case)

print(f'Total counts of chars, digits,and symbols \n\n Chars = {chars} \n Digists = {digits} \n Symbols = {symbols}')
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 6: Given two strings, s1 and s2, create a mixed String

def mix_strings(s1, s2):
    """
    :param s1: arbitrary string_1
    :param s2: arbitrary string_2
    :return:Question 6: Given two strings, s1 and s2, create a mixed String(create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.)
    """
    res = []
    middle_part_1 = []
    middle_part_2 = []
    first_char_s1 = s1[0]
    first_char_s2 = s2[0]
    last_char_s2 = s2[-1]
    last_char_s1 = s1[-1]
    length_s1 = len(s1)
    length_s2 = len(s2)

    for i in range(1, length_s1-1):
        middle_part_1.append(s1[i])
    for j in range(1, length_s2-1):
        middle_part_2.append(s2[j])
    sorted_middle_part_2 = reversed(middle_part_2)
    middle_part_mix = zip(middle_part_1, sorted_middle_part_2)
    res_middle_part_mix = ''.join(''.join(x) for x in middle_part_mix)
    res = [first_char_s1 + last_char_s2 + res_middle_part_mix + last_char_s1 + first_char_s2]
    print(res)

mix_strings('Abc', 'Xyz')
mix_strings('hsdfsf', 'jsdasd')
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 7: String characters balance Test

s1 = "Ynf"
s2 = "PYnative"
if s1.find(s2):
    print(True)
else:
    print(False)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 8: Find all occurrences of “USA” in given string ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"
new_lower_string = str1.lower()
res = new_lower_string.count('usa')
print(f'The USA count is: {res}')
print()
print('******************************NEXT EXERCISE******************************')
print()



# Question 9: Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters

str1 = "English = 78 Science = 83 Math = 68 History = 65"
l = []
new_s = str1.split(' ')
for i in new_s:
    if i.isdigit():
        l.append(int(i))
sum_l = sum(l)
avg_l = sum(l) / len(l)
print(f'sum is {sum_l} \naverage is {avg_l} ')
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 10: Given an input string, count occurrences of all characters within a string

str1 = "Apple"
count = {}

for x in str1:
    amount = str1.count(x)
    count[x] = amount
print(count)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 11: Reverse a given string

str1 = "PYnative"
news_str_1 = str1[::-1]
print(news_str_1)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 12: Find the last position of a substring “Emma” in a given string

str1 = "Emma is a data scientist who knows Python. Emma works at google."
index = str1.rfind("Emma")
print(index)
print()
print('******************************NEXT EXERCISE******************************')
print()



# Question 13: Split a given string on hyphens into several substrings and display each substring

str1 = 'Emma-is-a-data-scientist'
divide_str = str1.split('-')
print('Displaying each substring \n')
for i in divide_str:
    print(i, end='\n')
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 14: Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_l = list(filter(None, str_list))
print(f"After removing empty strings \n{new_l}")
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 15: Remove special symbols/Punctuation from a given string

import re

str1 = "/*Jon is @developer & musician"
str2 = re.sub(r'[^\w\s]', '', str1)
print("New string is", str2)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 16: Removal all the characters other than integers from string

str_1 = 'I am 25 years and 10 months old'
str_2 = []
for x in str_1:
    if x.isdigit():
        str_2.append(x)
print(''.join(str_2))
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 17: Find words with both alphabets and numbers
import re

l = []
str1 = "Emma25 is Data scientist50 and AI Expert"
news_st1 = str1.split(' ')
reg = re.findall('\w+\d+', str1)
for x in reg:
    print(''.join(x))
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 18: From given string replace each punctuation with #

from string import punctuation

str1 = '/*Jon is @developer & musician!!'
replace_char = '#'
for char in punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)
print()
print('******************************LAST EXERCISE******************************')
print()