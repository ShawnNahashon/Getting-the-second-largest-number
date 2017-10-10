'''
Script that takes an indefinate amount of numbers as input and outputs the next largest
number to the screen after the user has finished entering numbers and would like to exit.
'''
# Written by Shawn

import itertools # itertools module imported so that the for loop can run infinitely
def second_largest_number(): # function to find the second largest number
    numbers_list = [] # empty list created to store the numbers that'll be entered by the user
    for i in itertools.count(): # loop that runs infinitely
        number = int(input("Please enter a positive number(type -1 to exit):")) # prompts the user to enter a positive number or (-1) to exit the prompt
        if number ==-1: # condition statement to exit the program if -1 is entered
            break
        numbers_list.append(number) # the positive numbers entered are put into the list defined earlier
    numbers_list.remove(max(numbers_list)) # the maximum number from the list is removed
    # the next maximum number is now the second largest number
    print("\n The second largest number is:                 ",(max(numbers_list)))# function to print the second largest number

second_largest_number() # second_largest_number function call
