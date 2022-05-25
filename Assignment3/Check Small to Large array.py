#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Define array and variable for using in program
aray = []
count = 0

# How many Numbers USER Want To input Program ,Get From USER
n = int(input("N : "))

# range (0,n) # n = User Input in variable n # for example n = 5 --> i = 0 to 4 
for i in range(n):
    # item save numbers USER input 
    item = int(input(f"enter number {i+1} :"))
    # aray append item and convert to list
    aray.append(item)
# 1. i in start is 0 : aray [i - 1] + 1 ---> aray [0 - 1] + 1 = aray [0]
# 2. aray [i] + 1 ---> aray[0] + 1 = aray [1]
# i start from 0 to 4 and continue sentense 1 and 2  
    if aray[i - 1] + 1 < aray[i] + 1 :
            # if condition is TRUE count = count + 1 and count = n - 1 because n start from 0 and end to 4 (means < 5)
            count = count + 1

# if condition is TRUE means numbers sorted from small to large or A to Z or Asscending sort ---> print ("Moratab")
if count == n - 1  :
    print("Moratab")
# if condition is False print ("Na Maratab")
elif count != n -1 :
    print("Na Moratab")
# print aray for show list numbers
print(aray)


