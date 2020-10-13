#!/usr/bin/env python
# coding: utf-8

# In[2]:


#A set is an unordered collection data type with no duplicate elements

domainset = {"ASDC","MIG","Finance","Insurance"}    # Looks like a Dictionary, 
                                                    # But not if you notice no key-value pair
print(domainset)
print(type(domainset))


# In[3]:


for x in domainset:
    print(x)


# In[7]:


set1 = set("Management")   # set is unordered
print(set1)


# In[8]:


set1 = set(["C","java","python"])   # set is unordered
print(set1)


# In[9]:


set1 = set([1,2,3,4,5,6,7,7,7])   # set doesnt allow duplicates
print(set1)


# In[12]:


samplestring = 'management'
set1 = set(samplestring)
print(set1)


# In[13]:


set1.add("m") # set is changeable
print(set1)


# In[15]:


set1.discard("m") # set is changeable
print(set1)


# In[16]:


set1.add("m") # set is changeable
print(set1)


# In[17]:


set1.remove("m") # set is changeable
print(set1)


# In[9]:


set1 = {} #empty set is a dictionary
print(type(set1))


# In[18]:


tuplee = ()
print(type(tuplee))


# In[19]:


listt = []
print(type(listt))


# In[10]:


#creating empty set
set1 = set()
print(type(set1))


# In[ ]:


listt = []
print(type(listt))


# In[11]:


# mixed set
set1 = {10.0,"Query",(10,20,30)}
print(set1)


# In[15]:


Days = set(["Sun","Mon","Tue","Wed","Thu","Fri","Sat"])  # set is unordered
for d in Days:
    print(d)


# In[14]:


print ("Tue" in Days)
print ("Thursday" in Days)


# In[18]:


Days = set(["Sun","Mon","Tue","Wed","Thu","Fri"])  # set is changeable
print(Days)

Days.add("Sat")
print(Days)


# In[19]:


Days.discard("Wed")
print(Days)


# In[20]:


Days.remove("Mon")
print(Days)


# In[21]:


Days.discard("Wed")
print(Days)


# In[22]:


Days.remove("Mon")
print(Days)


# In[31]:


# some random element will get removed
print(Days.pop())

print(Days)


# In[33]:


Days.clear()

print(Days)


# In[34]:


Days = set(["Sun","Mon","Tue","Wed","Thu","Fri"])  # set is changeable
print(Days)

Months = set(['Oct','Jan','Nov','May','Aug','Feb','Sep','March','Apr','Dec','June','July'])
print(Months)


# In[35]:


days_and_months = Days.union(Months)
print(days_and_months)


# In[36]:


# using | symbol for union of set
print(Days | Months)


# In[38]:


# union on more than 1 set
x = {1,2,3}
y = {4,5,6}
z = {7,8,9,7}

output = x.union(y, z)

print(output)


# In[20]:


# intersection on set   #common element is picked out  
x = {1,2,3}
y = {4,3,6}

print(x & y)


# In[40]:


# by intersection method  #common element is picked out
x = {1,2,3}
y = {4,3,6}

print(x.intersection(y))


# In[24]:


set1 = {1,2,3,4,5}                     # set1! - only the uncommon elements of set1 will be picked out 
set2 = {4,5,6,7,8}
diff_set = set1.difference(set2)
print(diff_set)
diff_sett = set2.difference(set1)
print(diff_sett)
diff_settt = set2.symmetric_difference(set1)
print(diff_settt)


# In[45]:


set1 = {1,2,3,4,5}                    # set1! - only the uncommon elements of set1 will be picked out 
set2 = {4,5,6,7,8}
diff_set = set1-set2
print(diff_set)


# In[25]:


# not included common elements        # A! U B!
set1 = {1,2,3,4,5}                     
set2 = {4,5,6,7,8}
diff_set = set1.symmetric_difference(set2)
print(diff_set)


# In[47]:


# not included common elements        # A! U B!
print(set1^set2)


# In[54]:


months1 = set(['Jan','Feb','March','Apr','May','June'])
months2 = set(['Jan','Feb','March','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'])


subset_check = months1.issubset(months2)

superset_check = months2.issuperset(months1)

superset_check2 = months1.issuperset(months2)

print(subset_check)
print(superset_check)
print(superset_check2)


# In[55]:


A = {1,2,3}
B = {3,2,3,1}

print(A ==B)


# In[26]:


setA = set([21,22,23,24,25,26,27,27,27,27])
print(setA)


# In[57]:


setA.add(80)
print(setA)


# In[59]:


setA.add((90,100))   # Adding tuple to set
print(setA)


# In[63]:


setA.add([90,100])
print(setA)


# In[27]:


setA.update([110,120])  # Updating list to set, which becomes tuple in the output
print(setA)


# In[28]:


setA.update([120,140],{150:160})   # Updating list and dict to set, which becomes set in the output
print(setA)


# In[65]:


X = frozenset([1,2,3,4,5,6])   #frozenset converts the changeable property of set to unchangeble
Y = frozenset([4,5,6,7,8,9])
print(X)
print(Y)


# In[66]:


print(type(X))


# In[67]:


#frozenset makes the set to immutable
X.add(10)
print(Days)


# In[68]:


#frozenset makes the set to immutable
X.remove(5)
print(Days)


# In[69]:


#frozenset makes the set to immutable
X.update(50)
print(Days)


# In[ ]:




