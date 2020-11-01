# Question 1: Print First 10 natural numbers using while loop

for i in range(0, 11):
    print(i)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 2: Print the following pattern

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 3: Accept number from user and calculate the sum of all number between 1 and given number


number_of_user = int(input('Please type your number: '))
list_of_numbers = []

for i in range(1, number_of_user+1):
    list_of_numbers.append(i)
    result = sum(list_of_numbers)
print("Output will be: ", result)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 4: Print multiplication table of given number

num = 2
for x in range(1, 11):
    res = x * num
    print(res)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for item in list1:
    if item % 5 == 0 and item <= 150:
        print(item)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 6: Given a number count the total number of digits in a number

example = 75869
count = 0
str_integer = str(example)
for x in str_integer:
    count +=1
print(count)
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 7: Print the following pattern using for loop

x = 5
y = 5
for i in range(0,x+1):
    for j in range(y-i,0,-1):
        print(j,end=' ')
    print()
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 8: Reverse the following list using for loop

list1 = [10, 20, 30, 40, 50]
ordered_list = reversed(list1)
for item in ordered_list:
    print(item)
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 9: Display -10 to -1 using for loop

for x in range(-10, 0):
    print(x)
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 10: Display a message “Done” after successful execution of for loop

for i in range(5):
    print(i)
else:
    print('Done!')
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 11: Python program to display all the prime numbers within a range

start = 25
end = 50
print('Prime numbers between', start, 'and', end, 'are:')
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 12: Display Fibonacci series up to 10 terms

from fibonacci import fibonacci
fib = fibonacci(length=10)
for x in fib:
    print(x, end=' ')
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 13: Write a loop to find the factorial of any number

def factorial(number):
    result = 1
    for x in range(1, number + 1):
        result *= x
        print(str(x) + "!\t = " + str(result))
    return result


factorial(10)
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 14: Reverse a given integer number

example = 76542
str_example = str(example)
expected_output = str_example[::-1]
int_expected_output = int(expected_output)
print(int_expected_output)
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 15: Use a loop to display elements from a given list which are present at even positions


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in my_list:
    if my_list.index(x) % 2 != 0:
        print(x)
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 16: Display the cube of the number up to a given integer

input_number = 6
start_number = 1
while start_number <= input_number:
    print(f'Current number is: {start_number} and the cube is {pow(start_number, 3)}')
    start_number += 1
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 17: Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

number_of_terms = 5
start = 2
sum = 0
for i in range(0, number_of_terms):
    print(start, end=" ")
    sum += start
    start = (start * 10) + 2
print("\nSum of above series is:", sum)
print()
print('******************************NEXT EXERCISE******************************')
print()

# Question 18: Print the following pattern

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
print()
print('******************************LAST EXERCISE******************************')
print()