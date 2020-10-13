#!/usr/bin/env python
# coding: utf-8

# In[8]:


# AND with boolean
x = True
y = True
z = x and y 
                # z = True
print(z)


# In[2]:


x = True
y = False
z = x and y 
                # z = False
print(z)


# In[5]:


x = False
y = True
z = x and y 
                # z = False
print(z)


# In[6]:


x = False
y = False
z = x and y 
                # z = False
print(z)


# In[10]:


x = 1
y = 1
z = x and y 
                # z = y, so z = 1, see  and' and 'or' are not guranteed to be a boolean
print(z)


# In[11]:


x = 0
y = 1
z = x and y
print(z)


# In[12]:


x = 1
y = 0
z = x and y
print(z)


# In[13]:


x = 0
y = 0
z = x and y
print(z)


# In[15]:


# OR with boolean
x = True
y = True
z = x or y
                # z = True
print(z)


# In[16]:


x = True
y = False
z = x or y
                # z = True
print(z)


# In[17]:


x = False
y = True
z = x or y
                # z = True
print(z)


# In[18]:


x = False
y = False
z = x or y
                # z = False
print(z)


# In[19]:


x = 1
y = 1
z = x or y 
                # z = y, so z = 1, see  and' and 'or' are not guranteed to be a boolean
print(z)


# In[20]:


x = 0
y = 1
z = x or y
print(z)


# In[21]:


x = 1
y = 0
z = x or y
print(z)


# In[22]:


x = 0
y = 0
z = x or y
print(z)


# In[24]:


# Not with boolean

x = True
y = not x
            # y=False
print(y)


# In[25]:


# Not with boolean

x = False
y = not x
            # y=True
print(y)


# In[ ]:




