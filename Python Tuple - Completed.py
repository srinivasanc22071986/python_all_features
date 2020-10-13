#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# tuples - ordered, indexed, unchnageable - Allow Duplicate members


# In[1]:


# tuple -> ordered, indexed and unchangeable

x = 1,2,3
print(x)

# Tuples may also be enclosed in parenthesis

x = (1,2,3)
print(x)

# The empty tuple is written as two parenthesis containing nothing:

x = ()
print(x)
print(type(x))  #type of tuple


# In[3]:


x = 42, # single value tuple (if dont write a, then becomes a variable)
print(x)
print(type(x))


# In[4]:


x = 42
y = 42,

print (type(x))
print (type(y))


# In[5]:


print (3*(40+2))

print (3*(40+2,))  # this creates a tuple with three repetitions


# In[6]:


domaintuple = ("ASDC","MIG","Finance")     # tuple is ordered, indexed and unchangeable
print(domaintuple[1])


# In[7]:


domaintuple = ("ASDC","MIG","Finance")     # tuple is ordered, indexed and unchangeable
for i in domaintuple:
    print(i)


# In[10]:


# converting into tuple using tuple() constructor

print(tuple([1,2,3]))  # List in tuple

print(tuple('abc'))  # String in tuple

print(tuple((1,2,3)))  # Tuple in tuple


# In[4]:


aList = ['tao',93,99, 'time',99] #converting a list into a tuple
aTuple = tuple(aList)
print(aList)
print(aTuple)


# In[17]:


print(aList == aTuple) # cannot compare List and Tuple


# In[3]:


anotherList = list(aTuple)
print(aList == anotherList)  # can compare List and List


# In[16]:


print(aList is anotherList)


# In[18]:


domaintuple = ("ASDC","MIG","Finance")   # Tuple is unchangeable
domaintuple[1] = "blackcurrant"
# The values will remain the same:
print(thisTuple)


# In[23]:


aTuple = (123, 'abc', 4.56, ['inner','tuple'],7-9j)
print(aTuple)

aTuple2 = aTuple[0], aTuple[1], aTuple[-1]
print(aTuple2)

tup1 = (12,34.56)

tup2 = ('abc','xyz')

tup3 = tup1+tup2

print(tup3)


# In[24]:


t = (['xyz',123], 23, -103.4)
print(t)

print(t * 2)

t = t + ('free','easy')
print(t)


# In[1]:


s = 'first'
s = s + 'second'
print(s)

t = ('third','fourth')
print(t)

t = t + ('fifth','sixth')
print(t)

t = t + (['fifth','sixth'])
print(t)


# In[26]:


domaintuple = ("ASDC","MIG","Finance")

if "MIG" in domaintuple:
    print("Yes, 'MIG' is in the domaintuple")


# In[27]:


print(len(domaintuple))


# In[28]:


domaintuple = ("ASDC","MIG","Finance")
domaintuple[3] = "Global Wealth" # This will raise an error as Tuple are unchangeable
print(domaintuple)


# In[29]:


# we cannot delete the element from the tuple but we can delete the tuple completely

domaintuple = {"ASDC","MIG","Finance"}
del domaintuple[1]
print (domaintuple)


# In[1]:


# here domaintuple delelted completly
domaintuple = {"ASDC","MIG","Finance"}
del domaintuple


# In[3]:


my_tuple = ('A','S','D','C','C','G')   #Tuple allows duplicate values

print(my_tuple[0])

print(my_tuple[5])

print(my_tuple[6])


# In[4]:


my_tuple[2.0]


# In[6]:


# nested tuple
n_tuple = ("Tower",[13,6,8],[4,9,9])
print(n_tuple[0][3])


# In[8]:


print(n_tuple[1][1])

print(n_tuple[-1])


# In[9]:


my_tuple = ('m','a','n','a','g','m','e','n','t')

print(my_tuple[1:4])


# In[10]:


print(my_tuple[:-7])


# In[12]:


print(my_tuple[7:])


# In[13]:


print(my_tuple[:])


# In[14]:


my_tuple = (7,9,4, [12,5])  # values in tuple are not changeable#

my_tuple[1] = 9


# In[15]:


#items of list element in a tuple can be changed

my_tuple[3][0] = 9
print(my_tuple)


# In[16]:


my_tuple[3][2] = 10
print(my_tuple)


# In[21]:


# we can reassign the tuple
my_tuple = ('m','a','n','a','g','e','m','e','n','t')

print(my_tuple)


# In[18]:


my_tuple = ('m','a','n','a','g','e','m','e','n','t')

print(my_tuple.count('a'))

print(my_tuple.index('n'))


# In[20]:


my_tuple = ('m','a','n','a','g','e','m','e','n','t')

print('a' in my_tuple)

print('b' in my_tuple)

print('g' not in my_tuple)


# In[ ]:




