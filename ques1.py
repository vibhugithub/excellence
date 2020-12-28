# Question 1:-
# Python program to find sum of all the elements in a list.


# import random module as randint
from random import randint

# Initialize size of list
len_of_list = 5      


list_of_numbers = [randint(1,100) for _ in range(len_of_list)]   


# Create function with argument
def calculate_sum(list_of_numbers: list):
    sum_of_numbers = 0

    if len(list_of_numbers) > 0:        

        # If size of list is greater than 0
        # then elements is added
        for number in list_of_numbers:

            sum_of_numbers += number    

    return sum_of_numbers               

# Driver code
# Calling function with argument
sum_of_numbers = calculate_sum(list_of_numbers)     
print(sum_of_numbers)                  
