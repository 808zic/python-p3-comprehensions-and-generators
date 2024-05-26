#!/usr/bin/env python3

def return_evens(num_list):

    return [n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):

    return [sentence + "!" for sentence in sentence_list]
    



# List Comprehension
#A list comprehension uses square brackets
'''
eg
squared_minus_one = [(n **2) - 1 for n in range(1, 11)]

print(squared_minus_one)
# [0, 3, 8, 15, 24, 35, 48, 63, 80, 99]

'''
#Generator Expressions  
#A generator expression uses parentheses
'''
eg 
one_to_three = range(1,4)
squared_ge = (n ** 2 for n in one_to_three)
 print(n)

NOTE : Generator expressions produce generator objects instead of lists
'''
#NOTE:The key difference between list comprehensions and generator expressions is that
# list comprehensions create new, complete lists while generator expressions save the code to create new, complete lists.