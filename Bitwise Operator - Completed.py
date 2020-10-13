#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ~ operator will flip all of the bits in the number - 1's Complement - 2's Complement - 1's complement+1

# And Operator  - &
# Or Operator - |
# Not Operator - ^
~0


# In[2]:


~123


# In[3]:


~1


# In[4]:


#9       8         7         6         5         4         3         2         1
#2power8 2power7   2power6   2power5   2power4   2power3   2power2   2power1   2power0
#256     128       64        32        16        8         4         2         1

#60 = Bitwise XOR

#

60 ^ 30


# In[5]:


#Bitwise AND
(60 & 30)


# In[6]:


#Bitwise OR
(60 | 30)


# In[7]:


# << operator will perform a bitwise "left shift"
2 << 2

# 2- 000000010
# << 2  -> shift the values(leave 2 digit from left) 
# by 2 so 000010 and then fill with zeros so 000010+00 -> 00001000 = 8


# In[8]:


# >> operator will perform a bitwise "right shift"
2 >> 2

# 2- 000000010
# << 2  -> shift the values(leave 2 digit from left) 
# by 2 so 000010 and then fill with zeros so 00+000010 -> 00000000 = 0


# In[10]:


2 ^ 1


# In[11]:


~-2


# In[12]:


~1


# In[ ]:




