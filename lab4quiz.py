# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 09:01:46 2024

@author: Lenovo
"""

''' 
Print out first N integers, one per line where N is read in from the the user.
When printing the number, apply the rules:
    
For multiple of 3, print Fizz
Multiple of 5, print Buzz
Multiple of both, FizzBuzz

if N less than 1 print  "N must be greater than 1"
if N greater than 100 "Too much work, not thanks"    
'''
#multipleof printing
multipleof3 = "Fizz"
multipleof5 = "Buzz"



n_input = int(input("N: "))
if n_input < 1:
    print("N must be greater than 1")
elif n_input > 100:
    print("Too much work, no thanks")
else:
    for i in range(1, n_input + 1, 1):
        if i % 3 == 0 and i % 5 == 0:
            print(multipleof3 + multipleof5)
        elif i % 3 == 0:
            print(multipleof3)
        elif i % 5 == 0:
            print(multipleof5)
        else:    
            print(i + 1)
