#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Division operation,
a,b,c,d,e=3,2,2.0,-3,10
print(a/b)
print(a/c)
print(d/b)
print(b/a)
print(d/e)
print(e//a) #double division
print(e/a)


# In[2]:


# A module is a file containing Python definitions and statements.
pow(2,3)


# In[3]:


#we can also use the operator module
# the operator module provides 2-argument arithmetic functions
import operator

dir(operator)


# In[4]:


help(operator.truediv)


# In[5]:


# using function truediv
operator.truediv(a,b)


# In[6]:


# using function mod
operator.mod(a,b)


# In[4]:


import operator
help(operator.floordiv)
operator.floordiv(a,b) # = 1


# In[9]:


operator.floordiv(a,c) # = 1.0


# In[10]:


# Add using operator module
a,b = 1,2.0
print(a+b)
operator.add(a,b)


# In[11]:


a,b = 1, 2.0
a=operator.iadd(a,b)
print (a)


# In[12]:


help(operator.iadd)


# In[14]:


print (a)
print (b)
a += b

print(a)


# In[15]:


# Exponentiation

a,b = 2,3
print(a)
print(b)
print(a**b) # 2*2*2


# In[16]:


# math module pow() function
import math
a,b = 2,3
math.pow(a,b)


# In[17]:


# operator module pow() function
import operator
a,b = 2,3
math.pow(a,b)


# In[2]:


#using normal pow() can accept 3 arguments

a,b,c = 3,3,2
pow(2,3,2) # calculates (2**3) % 2


# In[20]:


import operator
a,b,c = 2,3,2
operator.pow(2,3,2) # calculates (2**3) % 2


# In[21]:


import math

c = 4
math.sqrt(c)


# In[22]:


import cmath
cmath.sqrt(5) # always gives complex format


# In[23]:


import math

#exp() computes e **x(e ** 0) (e ** 1)
#math.exp(2)
math.exp(0)


# In[24]:


math.exp(1)


# In[26]:


# Trignometric Functions
a,b = 1,2

import math
print(math.sin(a))

print(math.cosh(b))


# In[27]:


# arc tan is inverse of  the tangent function
math.atan(math.pi) # arch tan of pi


# In[28]:


#math.hypot(x,y) is also the length of the vector (or Eclidean distance) from the origin (0,0) to the point(x,y)
import math
math.hypot(a,b)


# In[29]:


#math.hypot(x2-x1,y2-y1)-> Eucidean distance between two points (x1,y1) and (x2,y2)
x1,y1=1,2
x2,y2=2,3
math.hypot(x2-x1,y2-y1)


# In[30]:


#radians -> degrees
math.degrees(a)


# In[32]:


#degrees -> radians
math.radians(57.29577951308232)


# In[33]:


# subtraction
a,b = 1,2
import operator
operator.sub(b,a)


# In[34]:


# multiplication
operator.mul(b,a)


# In[35]:


# Logarithms
import math
import cmath
math.log(5)


# In[36]:


# cmath so complex format
cmath.log(5)


# In[37]:


#optional base argument so log with base 10
math.log(1000,10)


# In[38]:


cmath.log(1000,10)


# In[39]:


# log base 2
math.log2(8)


# In[40]:


# log base 10
math.log10(100)


# In[41]:


# log base 10
cmath.log10(100)


# In[42]:


#Modulus
import operator
operator.mod(3,4)


# In[43]:


operator.mod(10,2)


# In[44]:


operator.mod(6,4)


# In[ ]:




