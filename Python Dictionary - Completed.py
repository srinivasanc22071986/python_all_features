#!/usr/bin/env python
# coding: utf-8

# In[1]:


Employee = {"Name" : "John", "Age" : 29, "salary" : 25000, "Company" : "GOOGLE"}

print(type(Employee))

print("printing Employee data ....")

print(Employee)


# In[2]:


friends = {
'tom' : '111-222-333',
'jerry' : '666-33-111'    
}

print(type(friends))
print(friends)


# In[3]:


x=friends["tom"]  #Acessing the value by key

print(x)


# In[4]:


x=friends[0]    # Dictionary is unordered and unindexed
print(x)


# In[5]:


x=friends.get('tom')  #get the value by key using get() function
print(x)


# In[6]:


d = {'x' : 1, 'y' : 2, 'z' : 3}

for key in d:
    print(key)


# In[7]:


for x in d:
    print(x, "value is :",d[x])


# In[8]:


# List in Dictionary

letterDict = {'vowel' : ['a','e','i','o','u'], 'consonant' : ['b','c','d','f']}
print(letterDict)


# In[2]:


friends = {
'tom' : '111-222-333',
'jerry' : '666-33-111'
}

print(friends)

friends["Mark"] = '777-55-333'  # Dictionary is changeable

print(friends)


# In[10]:


# prints only keys
for x in friends:
    print(x)
    


# In[11]:


# prints values
for x in friends:
    print(friends[x])


# In[12]:


# prints value using values()function

for x in friends.values():
    print(x)
print(friends.values())


# In[17]:


# prints both key and values using items() function

for x,y in friends.items():
    print(x,y)
print(friends.items())
print(type(friends))
print(friends["tom"])
#print(friends[0])
print(type(friends["tom"]))


# In[14]:


# prints both key and values using items() function

for x in friends.keys():
    print(x)


# In[15]:


# prints both key and values using items() function

for x in friends.values():
    print(x)


# In[14]:


print(len(friends))


# In[9]:


dict1 = {'A':'earth', 'B' : 80}
print(dict1)

dict1['A'] = 'venus'
dict1['B'] = "6969"
dict1['C'] = 'sunoss'

print(dict1)


# In[16]:


params = {"A":"a","B":"b","C":"c","D":"d"}
print(params.keys())
print(params.values())
print(params.items())
          


# In[17]:


d = {'host' : 'earth', 'port' : 80}

print(d)
returned_value = d.clear()
print(d)
print(returned_value)


# In[18]:


#mixing data types in dict.
d = {"A":"a","B":"b"}
print(d)
d["retrycount"] = 3
print(d)
d[42] = "douglas"
print (d)


# In[19]:


items = [('name','Gumby'),('age',42)]   # tuple in list  #important
print(items)

d = dict(items)  #dict() -> constructor to make a new dictionary
print(d)

print(d['name'])


# In[12]:


d = dict(name='Gumby', age=42) # tuple
print (d)


# In[15]:


d = dict[['name','Gumby'], ['age',42]] # nested list
print (d)


# In[21]:


x = {'username':'admin','machines':['foo','bar','baz']}
y=x.copy()

print(y)
print(x)


# In[22]:


x = {'username' : 'admin','machines': ['foo','bar','baz']}
print(x)

y = x.copy()

print(y)

y['username'] = 'm1h'

print("-------------------------")
print(y)
print(x)

y['machines'].remove('bar')

print("-------------------------")
print(y)
print(x)


# In[2]:


emptyDictionary = {}
print(emptyDictionary)

grades = {"A":87, "B":76, "C":92, "D":89}
print ("\nAll grades:",grades)

print(grades["A"])
grades["A"] = 90
print ("A's new grade:", grades["A"])

#add to an existing dictionary
grades["B"] = 93
print ("\nDictionary grades after modification:")
print(grades)

#delete entry from dictionary
del grades["C"]
print ("\nDictionary grades after deletion:")
print(grades)


# In[4]:


dict2 = {'name':'earth', 'port': 80}

print('name' in dict2)

print('earth in dict2.values()')
print("---------------------")
print(dict2.values())

print('port' not in dict2)

print('phone' in dict2)
print('phone' not in dict2)


# In[18]:


d1 = {"mike":41, "bob":3}
d2 = {"bob":3, "mike":41}
d3 = {"bob":3, "mike":42, "Joy":45}

print(d1 == d2) #checking for equality of dict

print(d1 < d2)


# In[6]:


d = {'x':1, 'y':2}
d.pop('x')
print(d)


# In[7]:


d ={'x':1, 'y':2}
d.pop() #no indexing here so can take the last element by itself as it takes in list
print(d)


# In[8]:


d = {'url' : 'http://python.org','spam':0, 'title': 'Python Web Site'}
d.popitem() #removes random item
print(d)


# In[17]:


dict2 = {'name':'earth','port':80}
print(dict2)

del dict2['name']
print(dict2)

dict2.clear()
print(dict2)


# In[18]:


dict2 = {'name':'earth','port':80}

del dict2
print(dict2)


# In[19]:


print ({}.fromkeys(['name','age',10])) #by default None will be set as default value


# In[21]:


print (dict.fromkeys(['name','age'])) 
print (dict.fromkeys(['name','age'],'(unknown)')) #supplying our own default value

print (dict.fromkeys(['name','age'],'(its unknown)')) #supplying our own default value


# In[22]:


d = dict.fromkeys(['name','age'],'(unknown)')
print(d.get('name'))


# In[23]:


dict2 = {'host':'earth','port':80}
dict3 = {'host':'venus','server':'http'}

dict2.update(dict3)
print(dict2)

print(dict3)
dict3.clear()
print (dict3)


# In[ ]:




