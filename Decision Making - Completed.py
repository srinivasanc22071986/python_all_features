#!/usr/bin/env python
# coding: utf-8

# In[1]:


# if decision making

num = int(input("Enter the number?"))

if num%2 ==0:
    print("Number is even")


# In[3]:


if 2+2 == 4:
    print("I know math")


# In[4]:


if True:
    print("This is True")


# In[1]:


a = int(input("Enter the value of a?"))
b = int(input("Enter the value of b?"))
c = int(input("Enter the value of c?"))

if a>b and a>c:
    print("A is the greatest")
    
if b>a and b>c:
    print("B is the greatest")
    
if c>b and c>a:
    print("C is the greatest")


# In[6]:


age = int(input("Enter your age?"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You have to wait")


# In[7]:


a = int(input("Enter the value of a?"))
b = int(input("Enter the value of b?"))
if a>b :
    print("A is the greatest")
else:
    print("B is the greatest")


# In[3]:


#checking for nested conditions
a = int(input("Enter the value of a?"))
b = int(input("Enter the value of b?"))
if a>b :
    print("A is the greatest")
elif b>a:
    print("B is the greatest")
else:
    print("Both A and B are same")


# In[10]:


a = int(input("Enter the value of a?"))
b = int(input("Enter the value of b?"))
c = int(input("Enter the value of c?"))

if a>b and a>c:
    print("A is the greatest")
    
elif b>a and b>c:
    print("B is the greatest")
    
elif c>b and c>a:
    print("C is the greatest")

else:
    print("Error in input")


# In[16]:


marks = int(input("Enter the marks:"))

if marks>85 and marks<=100:
    print("You have scored A grade")
    
elif marks>60 and marks<=85:
    print("You have scored B grade")
    
elif marks>40 and marks<=60:
    print("You have scored C grade")
    
elif marks>30 and marks<=40:
    print("You have scored D grade")

else:
    print("Sorry you have failed")


# In[ ]:




