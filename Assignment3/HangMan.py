#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

# i = random.randint(0, len(words)-1)
# word = words[i]

word = random.choice(words) # clock
joon = 10

while joon > 0:
    print('- ' * len(word)) # - - - - -

    user_character = input().lower() # s

    if user_character in word:
        print('yes')
        break
    else:
        joon = joon - 1
        print('no')

