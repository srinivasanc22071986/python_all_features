#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Loops can execute a block of code number of times until a certain condition is met

# For loop  iterates the elements of a sequence and the no of iteration is known n of times 
# iteration should happen

'''
python syntax - for variable_to_iterate in sequence:
                    statements(s)
'''


# In[1]:


i=1
n=int(input("Enter the number up to which you want to print the numbers :"))
for i in range(0,n):
    print(i, end = ' ')
    
'''

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),  
and ends at a specified number

'''

    
    


# In[3]:


x = range(6)

for n in x:
    print(n)


# In[4]:


x = range(3,6)

for n in x:
    print(n)


# In[5]:


x = range(3,20,3)

for n in x:
    print(n)


# In[6]:


programming_language = ["Java","Python","C++"]
for x in programming_language:
    print(x)


# In[7]:


'''

In python, while loop is used to execute a block of statements repeatedly until a given condition is satisfied.

while condition_to_check:
    statements to execute
'''

i=0;
while i<=10:
    print(i);
    i=i+1;


# In[8]:


# here the for loop cannot be used as we dont know what will be value of of the variable numrange
# so here while loop only can be used, as we have an uncertainity 

i=1
number = int(input("Enter the number to make mutiplication table ?"))
numrange = int(input("Enter the number upto which the mutiplication table"))
while i<=numrange:
    print("%d * %d = %d \n"  %(number,i,number*i))
    i=i+1;


# In[9]:


# Break Statement - With the break statement we can stop the loop even if the while condition is true:


i=1;
while 1<=10: # here we checks the condition
    print(i);
    if i ==3:
        break
    i=i+1;


# In[10]:


# Continue Statement - continue statement we can stop the current iteration, and continue with the next

i=1
while i<=10:
    i=i+1
    if i == 3:
        continue
    print(i);


# In[30]:


for i in range(0,10):    
    
    if i == 6 or i==7:
        continue
#    if i == 7:
#        continue
    print(i)


# In[ ]:


x=1
while x < 10:
    if x== 5:
        continue
    print(x)
    x+=1


# In[ ]:




