def greater_or_not(num_1, num_2):
    """
    :param num_1: input data form client
    :param num_2: input data form client
    :return: Question 1: Given a two integer numbers return their product and if the product is greater than 1000, then return their sum
    """
    if num_1 * num_2 < 1000:
        result_multyply = num_1 * num_2
        return (f'The result is {result_multyply}')
    else:
        result_sum = num_1 + num_2
        return f'The result is {result_sum}'


print(greater_or_not(40, 30))
print()
print('******************************NEXT EXERCISE******************************')
print()


def current_and_previous_numbers_sum(nums=range(10)):
    """
    :param nums: It's numbers from 0 to 10, generated with method range()
    :return: Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print  the sum of the current number and previous number
    """
    for num in nums:
        if num == 0:
            print(f'Current Number {num} Previous Number {num} Sum: {num}')
        else:
            print(f'Current Number {num} Previous Number {num-1} Sum: {num + (num-1)}')


current_and_previous_numbers_sum()
print()
print('******************************NEXT EXERCISE******************************')
print()


def letter_with_even_index(word):
    """
    :param word: Input data is string
    :return: Question 3: Given a string, display only those characters which are present at an even index number.
    """
    for item in word:
        if word.index(item) % 2 == 0:
            print(item)


letter_with_even_index('pynative')
print()
print('******************************NEXT EXERCISE******************************')
print()


def remove_chars(string, number):
    """
    :param string: arbitrary word
    :param number: number to define which part have to slice
    :return: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
    """
    new_str = string[number:]
    return new_str


print(remove_chars('pynative', 4))
print()
print('******************************NEXT EXERCISE******************************')
print()


def match_first_and_last_numbers(list_of_numbers):
    """
    :param list_of_numbers: arbitrary list of numbers
    :return: Question 5: Given a list of numbers, return True if first and last number of a list is same
    """
    first_number = list_of_numbers[0]
    last_number = list_of_numbers[-1]
    if first_number == last_number:
        print(f'Given list is {list_of_numbers}')
        print('result is True')
    else:
        print(f'Given list is {list_of_numbers}')
        print('result is False')


match_first_and_last_numbers([10, 20, 30, 40, 10])
match_first_and_last_numbers([10, 20, 30, 40, 50])
print(remove_chars('pynative', 4))
print()
print('******************************NEXT EXERCISE******************************')
print()


def count_word(string):
    """
    :param string: arbitrary sentences
    :return: Question 7: Return the total count of sub-string “Emma” appears in the given string
    """
    new_str = string.split(' ')
    count_match = new_str.count('Emma')
    return f'Emma appeared {count_match} times'


print(count_word('Emma is good developer. Emma is a writer'))
print()
print('******************************NEXT EXERCISE******************************')
print()


def create_pyramid(nums=range(6)):
    """
    :param nums: Generate numbers
    :return: Question 8: Print the following pattern
    """
    for num in nums:
        for item in range(num):
            print(num, end=' ')
        print('\n')


create_pyramid()
print()
print('******************************NEXT EXERCISE******************************')
print()


def palindrom(num):
    """
    :param num: arbitrary number
    :return: Question 9: Reverse a given number and return true if it is the same as the original number
    """
    num_str = str(num)
    if num_str == num_str[::-1]:
        print(f'original number {num}\n The original and reverse number is the same \n')
    else:
        print(f'original number {num}\n The original and reverse number is not same')


palindrom(121)
palindrom(125)
print()
print('******************************NEXT EXERCISE******************************')
print()


def odd_and_egg_numbers(list_1, list_2):
    """
    :param list_of_numbers: arbitrary list of numbers
    :return: Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list
    """
    result_list_1 = [item_1 for item_1 in list_1 if item_1 % 2 != 0]
    result_list_2 = [item_2 for item_2 in list_2 if item_2 % 2 == 0]
    result_list = result_list_1 + result_list_2
    return f'result list is {result_list}'

first_list = [10, 20, 23, 11, 17]
second_list = [13, 43, 24, 36, 12]
print(odd_and_egg_numbers(first_list, second_list))
print()
print('******************************NEXT EXERCISE******************************')
print()


def reverse_numbers(nums):
    """
    :param nums: arbitrary numbers
    :return: Question 11: Write a code to extract each digit from an integer, in the reverse order
    """
    while nums > 0:
        ex = nums % 10
        print(ex, end=' ', )
        nums = nums // 10


reverse_numbers(7536)
print()
print('******************************NEXT EXERCISE******************************')
print()


def income_tax(income):
    """
    :param income: size of income
    :return: Calculate income tax
    """
    tax_for_pay = 0
    if income <= 10_000:
        tax_for_pay = 0
        print(f"Your income is {income}\nTax is {tax_for_pay}")
    elif income <= 20_000:
        tax_for_pay += (income - 10_000) * 10 / 100
        print(f"Your income is {income}\nTax is {tax_for_pay}")
    else:
        tax_for_pay += 10_000 *10 / 100
        tax_for_pay += (income - 20_000) * 20 / 100
        print(f"Your income is {income}\nTax is {tax_for_pay}")


income_tax(14_002)
income_tax(45_000)
income_tax(33_000)
income_tax(114_050)
print()
print('******************************NEXT EXERCISE******************************')
print()


def multiplications_table():
    """
    :return: Question 13: Print multiplication table form 1 to 10
    """
    for vertical in range(1, 11):
        for horizontal in range(1, 11):
            print(vertical * horizontal, end=' ')
        print('\t\t')


multiplications_table()
print()
print('******************************NEXT EXERCISE******************************')
print()


def pyramid_asterisk(num):
    """
    :param num: arbitrary number which show us deep of pyramid
    :return: Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)
    """
    while num != 0:
        print('*' * num, end='\n')
        num -= 1


pyramid_asterisk(5)
print()
print('******************************NEXT EXERCISE******************************')
print()


def exponent(base, exp):
    """
    :param base: just integer
    :param exp: non-negative integer
    :return: Question 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
    """
    result = base ** exp
    return f'{base} raises to the power of {exp} is: {result}'


print(exponent(5, 4))
print()
print('******************************NEXT EXERCISE******************************')
print()