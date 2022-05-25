#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get any number from User for print Snake
n = int(input("N : "))
# for i in range 0 to n - 1 
for i in range(n):
    # i start from 0 to n - 1 ---> if i % 2 == 0 means number is odd and print("*")
    if i % 2 == 0 :
        print("*", end = "")
    # elif i % 2 != 0 means number is even and print("#")
    elif i % 2 != 0 :
        print("#",end = "")

