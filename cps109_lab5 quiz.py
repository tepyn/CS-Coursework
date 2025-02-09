# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:05:26 2024

@author: Lenovo
"""
#lab5 quiz (a is a list, out is a boolean)

lst =["bob", "jack"]
status = False

def faro_shuffle(a, out):
    mid = len(a) // 2
    list1 = a[:mid]
    list2 = a[mid:]
    shuffled_list = []
    
    if out:
        for i in range(mid):
            shuffled_list.append(list1[i]) 
            shuffled_list.append(list2[i])
    else:
        for i in range(mid):
            shuffled_list.append(list2[i])
            shuffled_list.append(list1[i])
    
    return shuffled_list

newlist = faro_shuffle(lst, status)
print(newlist)