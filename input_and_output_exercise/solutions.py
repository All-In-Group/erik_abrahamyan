# Question 1: Accept two numbers from the user and calculate multiplication

num_1 = int(input("Please type first number: "))
num_2 = int(input("Please type second number: "))
result = num_1 + num_2
print('The result is',result)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 2: Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function

print('My', 'Name', 'Is', 'James', sep='**')
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 3: Convert decimal number to octal using print() output formatting

print('%.2f' %458.541315)


# Question 5: Accept list of 5 float numbers as a input from user

new_list = []
size_of_list = int(input('Please type size of list: '))
for i in range(0, size_of_list):
    item = float(input('Please type item of list: '))
    new_list.append(item)
print('Your list of numbers are:', new_list)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 6: write all file content into new file by skiping line 5 from following file

with open('example.txt', 'r') as f:
    data = f.readlines()
    for item in data:
        if item != 'line5\n':
            with open('new_example.txt', 'a') as new_f:
                new_f.write(item)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 7: Accept any three string from one input() call

str_1, str_2, str_3 = input('Please type 3 string: ').split(' ')
print(str_1, str_2, str_3)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 8: You have the following data.

totalMoney = 1000
quantity = 3
price = 450
print(f'I have {totalMoney} dollars so I can buy {quantity} football for {price:.2f} dollars.')
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 9: How to check file is empty or not

import os
print(os.stat('new_example.txt').st_size==0)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 10: Read line number 4 from the following file

with open('example.txt', 'r') as f:
    for i in f:
        if i == 'line4\n':
            print(i)
print()
print('******************************LAST EXERCISE******************************')
print()
