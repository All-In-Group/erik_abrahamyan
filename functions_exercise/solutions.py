def name_age(name, age):
    """
    :param name: the name of man
    :param age: age of the man
    :return: Question 1: Create a function that can accept two arguments name and age and print its value
    """
    return f'My name is {name} and I am {age}'


print(name_age('Erik', 31))
print()
print('******************************NEXT EXERCISE******************************')
print()


def func1(*args):
    """
    :param args: accept a variable length of  argument
    :return: Question 2: Write a function func1() such that it can accept a variable length of  argument and print all arguments value
    """
    for i in args:
        print(i)


func1(20, 40, 60)
func1(80, 100)
print()
print('******************************NEXT EXERCISE******************************')
print()


def calculation(a, b):
    """
    :param a: arbitrary number_1
    :param b: arbitrary number_2
    :return: Question 3: Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call
    """
    return a + b, a - b


res = calculation(40, 10)
print(res)
print()
print('******************************NEXT EXERCISE******************************')
print()


def showEmployee(name, salary=9000):
    """
    :param name: arbitrary name of worker
    :param salary: default we set salary in size 9000
    :return: Question 4: Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000
    """
    return f'Employee {name} salary is: {salary}'

print(showEmployee('Ben', 9_000))
print(showEmployee('Ben'))
print()
print('******************************NEXT EXERCISE******************************')
print()


def outer(a,b):
    """
    :param a: arbitrary number_1
    :param b: arbitrary number_2
    :return: Create an inner function to calculate the addition in the following way
    """
    def inner(a,b):
        """
        :param a: arbitrary number_1
        :param b: arbitrary number_2
        :return: sum the result of both number
        """
        return a + b
    bonus_point = inner(a,b)
    return bonus_point + 5


print(outer(20,30))
print()
print('******************************NEXT EXERCISE******************************')
print()


def displayStudent(name, age):
    """
    :param name: arbitrary name
    :param age: arbitrary age
    :return: Question 7: Assign a different name to function and call it through the new name
    """
    print(name, age)


showStudent = displayStudent
showStudent('Emma', 26)
print()
print('******************************NEXT EXERCISE******************************')
print()


def even_number(even_numbers_list=[]):
    """
    :param even_numbers_list: empty list where will be append our result
    :return: Generate a Python list of all the even numbers between 4 to 30
    """
    for i in range(4, 31):
        if i % 2 == 0:
            even_numbers_list.append(i)
    print(even_numbers_list)


even_number()
print()
print('******************************NEXT EXERCISE******************************')
print()


# Question 9: Return the largest item from the given list
aList = [4, 6, 8, 24, 12, 2]
biggegst_item = max(aList)
print(biggegst_item)
print()
print('******************************LAST EXERCISE******************************')
print()




