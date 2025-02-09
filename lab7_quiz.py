# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:16:27 2024

@author: Lenovo
"""
#find len without using len function
def rlen(items): #items could be list/string 
    
    #base case, check if it is empty
    if not items:
        return 0
    else:
        #recursive function
        return 1 + rlen(items[:-1])
    
lst = [1, 2, ["hello", "bye"], 4, "hi", 7.9]
print(rlen(lst))
        