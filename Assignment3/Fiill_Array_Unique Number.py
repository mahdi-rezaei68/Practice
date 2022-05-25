#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import 
import random
# n = User say how many random numbers need to show
n = int(input("N : "))
# item variable save random nembers from 0 to 99 , n means how much numbers
# sample means numbers should be unique
item = random.sample(range(0,100),n)
print(item)

