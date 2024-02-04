#!/usr/bin/env python
# coding: utf-8

# ======== __Week 2 Assignment__ =========
# 
#         - set comperhension - 
#         - zip() function -

# In[12]:


# find who's making over $100,000 per year

# {name, $income}

agents = [("James", 97000),
            ("Jade", 250000),
            ("Trish", 50000),
            ("David", 150000)]


rank = {a for a, i in agents if i>100000}

print(rank)


# In[18]:


# finding if x and y has similiar values

x = [4, 7, 14, 12, 21]
y = [6, 7, 11, 13, 21]

for a, b in zip(x,y):
    if a == b:
        print("Same value")
    else:
        print("Not the same value")


# In[ ]:




