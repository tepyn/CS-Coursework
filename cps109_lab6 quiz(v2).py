# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:20:15 2024

@author: Lenovo
"""

#see if int recieved is a prime
def is_prime(n):
    prime_num = True
    
    if n >= 1:
        if n % 2 == 0: #skips the even nums
            return False
        else:
            for i in range(3, n, 2): 
                if n % i == 0:
                    prime_num = False
                    break
                
    return prime_num
input_n = int(input("n: "))
print(is_prime(input_n))