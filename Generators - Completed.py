#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Generator is a function which is responsible to generate a sequence of values.

# We can write generator functions just like ordinary functions, but it uses yield keyword to return values

# Memory utilization is the biggest advantage

# overall this seems to use yield instead of print


# In[3]:


def mygenerator():
    yield 'A'
    yield 'B'
    yield 'C'
    
g=mygenerator()

print(next(g))
print(next(g))
print(next(g))


# In[16]:


import time
def countdown(num):
    print("Start Countdown")
    while(num>0):
        yield(num)
        num=num-1
        
for x in countdown(5):
    time.sleep(3)
    print(x)


# In[ ]:


#l=[x*x for x in range(100000000000000000000000000000000000000)]
#print(l[0])


# In[5]:


# yeild function to generate the no

def generateNumber(num):
    n=1
    while n<=num:
        yield n
        n=n+1
        
for n in generateNumber(10):
    print(n)


# In[1]:


for i in range(0,10):
    print(i)


# In[4]:


x = xrange(0,10)

print(x)


# In[9]:


for i in range(0,10):

    print(i)


# In[ ]:




