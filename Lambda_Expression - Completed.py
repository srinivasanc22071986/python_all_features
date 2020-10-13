#!/usr/bin/env python
# coding: utf-8

# In[1]:


# intro and stuff about the lambda expression

# Lambda argument list : expression_to_execute -> syntax of lambda expression(Lambda is keyword by python)

# It cannot contain any statements and returns a function object which can be assigned to any variable


# In[2]:


# normal function
def greeting():
    return "Hello"

print(greeting())


# In[3]:


# Lambda expression

greet_me = lambda:"Hello"

print(greet_me())

print(type(greet_me))


# In[6]:


# Normal Function

def add(x,y):
    return x+y

a=add(2,3)
print(a)


# In[7]:


# Normal Function

x=lambda x,y:x+y
print(x(20,10))


# In[8]:


def squareRoot(n):
    return n*n

print(squareRoot(10))


# In[9]:


x=lambda n:n*n

print(x(10))
print(x(20))


# In[10]:


# finding greatest no of two nos

x=lambda a,b:a if a>b else b

print(x(10,20))


# In[11]:


# Lambda function to check if a given value is from 10 to 20

check=lambda x:x>10 and x<20

print(check(12))

print(check(3))

print(check(24))


# In[12]:


# If the given value is less than 10 then multiple it by 2
# else if its between 10 to 20 the multipplies by 3
# else returns the unmodified same value

converter = lambda x:x*2 if x<10 else (x*3 if x<20 else x)

print("convert 5 to :",converter(5))

print("convert 13 to :",converter(13))

print("convert 23 to :",converter(23))) 


# In[13]:


'''

filter() - to filter values from the given sequence based on some condition


map() - in the given sequence, apply some functionality and generate new element with the required modification


reduce() - reduces sequence of elements into a single element by applying the specified function.

'''


# In[33]:


# filter syntax - > filter(function, sequence)

def num(n):
    if(n>7):
        return n
    
numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

#num1=[]

#for i in numbers_list:
    #num1.append(num(i))
    
#print(num1)#

#for i in numbers_list:
    #if(i>7):
        #num1.append(i)
    
#print(num1)


filtered_list = list(filter(num, numbers_list))

print(filtered_list)


# In[14]:


# filter syntax - > filter(function, sequence)

numbers_list = [2,6,8,10,11,4,12,7,13,17,0,3,21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)


# In[35]:


numbers_list = range(-5,5)

for i in numbers_list:
    print(i)

less_than_zero = list(filter(lambda x: x<0, numbers_list))

print(less_than_zero)


# In[17]:


Year_list = [1992,1994,1996,1998,2000,2003,2004,2008,2010,2012,2014]

Leap_Years = list(filter(lambda leap: (leap%4 == 0),Year_list))

print("The leap years in the list are: ",Leap_Years)


# In[18]:


list1=range(1,20)

final_list=list(filter(lambda x:x%3==1,list1))

print(final_list)


# In[19]:


a=[1,2,3,4,5,6]

list1=tuple(filter(lambda x: x%2 == 0, a))

print(list1)


# In[20]:


# map() function - syntax of map function without lambda expression

#without lambda

list1=[1,2,3,4,5]

def doubleNo(x):
    return 2*x

l1=list(map(doubleNo,list1))

print(l1)


# In[21]:


# making every element to double

list1=[1,2,3,4,5]

l1=list(map(lambda x:x*2,list1))

print(l1)


# In[22]:


# making every element to double

list1=[1,2,3,4,5]

l1=list(map(lambda x:x*x,list1))

print(l1)


# In[23]:


# making every element to double

list1=[1,2,3,4,10,123,22]

l1=list(map(lambda x:x*5,list1))

print(l1)


# In[39]:


from functools import *

list1=[1,2,3,4,5]

l1=reduce(lambda x,y:x+y,list1)

print(l1)


# In[40]:


from functools import *

list1=[1,2,3,4,5]

l1=reduce(lambda x,y:x*y,list1)

print(l1)


# In[46]:


f= lambda a,b:a if (a > b) else b

result=reduce(f,[10,20,30,40])

print(result)


# In[50]:


for i in range(1,20):
    print(i,end="")
    print(" ",end="")

print()

result=reduce(lambda x,y:x+y,range(1,20))
              
print(result)


# In[2]:


a = 10

print(a<<1)

print(a>>1)


# In[20]:


def x(a,b):
    return(a+b)

#x(10,20)


assert(x(10,20) == 30)

print("Test case passed")


# In[4]:


x = lambda a,b:(a+b)

x(10,20)


# In[ ]:




