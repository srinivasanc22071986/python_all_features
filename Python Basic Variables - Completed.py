#!/usr/bin/env python
# coding: utf-8

# In[1]:


#basic print statements in python
print("Hello World")
print("Welcome to python")
print('a')
print(10)
print(10.23456)
print(10+20)
print(30-10) 


# In[2]:


#<variable_name> = value (python take the type of variable by itself)
a=10
print(a)

x="concentrate here please"
print(x)

b=10+20
print(b)

pi=3.14
print(pi)
c='A'
print(c)

name='Vijay Mallaya'
print(name)

q=True
print (q)

t=None
print (t)

r=0
print(r)


# In[12]:


#showing the list of keywords which are used by python
import keyword
print(keyword.kwlist)


# In[19]:


#rules with variables
#1.Variables names must start with a letter or an underscore
x=True #valid

_y=True #valid

#9x=False #starts with numeral => SyntaxError: invalid syntax

#$y=True #starts with symbol => SyntaxError: invalid syntax


# In[20]:


#2.The remaining portion of your variable name may consist of letters, numbers and underscores
has_0_in_it = "Still Valid"


# In[22]:


#3.Names are case sensitive
x=9
y=X*5


# In[3]:


#4.Even though there's no need to specify a data type when declaring a variable in Python, while allocating the 
#necessary area in memory for the variable, the Python interpreter automatically picks the most 
#suitable built-in type for it:
a=2
print(type(a))
#Output: <type 'int'>

b=None
print(type(b))

c=0
print(type(c))

print(type(True))

d=True
print(type(d))


# In[27]:


#5.You can assign mutiple values to multiple variables in one line.
# Note that there must be the same number of arguments on the right and left sides of the operator

a, b, c =1, 2, 3
print(a,b,c)
#Output: 1 2 3


# In[4]:


a,b,_=1,2,3

print(a,b,_)

#a.b,_=1,2,3,4


# In[29]:


a=b=c=1
print(a,b,c)


# In[30]:


a=b=c=1
print(a,b,c)
b=2
print(a,b,c)


# In[31]:


x=y=[7,8,9] #here x and y is a list
x=[13,8,9]  #here x is a list
print(y)
print(x)


# In[32]:


a=[1,2,3] #here a is a list
b=[1,2,3] #here b is a list

print(a)
print(b)

a[0]=10;
print(a)
print(b)


# In[33]:


a=2
print(a)
a="new value"
print(a)


# In[37]:


x=y=[7,8,9]
print(y)
print(x)
x[0]=13
print(y)
print(x)


# In[ ]:




