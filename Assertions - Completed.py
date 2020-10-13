#!/usr/bin/env python
# coding: utf-8

# In[1]:


# purpose debugging 

# process of identifing and fixing the bug is called debugging

# Use of assertions over print() and env types - dev ,test ,prod env

# types of Assert statement

# assert conditional_expression


# In[2]:


x=10


assert x==10
#assert x>10


print(x)


# In[3]:


# augumented assert

# assert condition_expression message_to_show


# In[4]:


x=10


assert x==10
#assert x>10 ,"Here X value must be equal to 10 "


print(x)


# In[7]:


def squareOperation(num):
    return num**num              # num to the power num, 2 to the power 2 is 4, 3 to the power 3 is 27, 
                                 # 4 to the power 4 is 256
    #return num*num 

assert squareOperation(2)==4 , "square Operation must be 4 here or power Operation must be 4 here"

assert squareOperation(3)!=27 , "square Operation must be 9 here or power Operation must be 27 here"

print(squareOperation(2))

print(squareOperation(3))

print(squareOperation(4))

# py -o filename.py


# In[ ]:




