#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''

String literals in python are surrounded by either 
single quotation marks, or 
double quotation marks or 
tripple quotation marks 

'hello' is the name as "hello"

'''

a="Welcome to Python"
print(a)


# In[2]:


print(type(a))


# In[3]:


'''

python doesn't support the character data type instead a single character written as 'p' is 
treated as the string of length 1

'''

print (type('p'))
print (type('10'))
print (type(10))


# In[4]:


# string as variable
myString="Hello World"
print(myString)


# In[5]:


print(''' String as triple quotes''')


# In[11]:


print("Hello, world!")

print('Hello, world!')

print("Let's go!")

print('"Hello, world" she said')

print('Let\'s go!')

print("\"Hello, world!\" she said")

print('''"Sri"n"i"vasan"''')


# In[7]:


# Indexing starts with 0

a="Hello World!"
print(a[1])


# In[8]:


sample_str="Welcome Post"
print(sample_str[1.25])


# In[9]:


print(sample_str[1024])


# In[10]:


print("This is a string with  \"double quotes\"")

print('This is a string with  "double quotes"')

print("This is a string with  'single quotes'")

print("""This is a string with  "double quotes" and 'single quotes'. You can even do multiple lines""") # even triple double quites can be used

print('''This is a string with  'single qoutes' and "double quotes"''') # even triple single quites can be used

print('''This is a string with  "double" qoutes' and 'single' quotes''') # even triple single quites can be used


# In[1]:


# with Triple quotes Strings can extend to multiple lines

String_var = '''    This document will help you to 
explore all the concepts
                            of Python Strings'''
print(String_var[46])


# In[12]:


b = "Hello, World!"
print(b[2:8])


# In[13]:


sample_str = 'Python String'

#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# P<------>y<------>t<------>h<------>o<----->n<-----> <----->S<----->t<----->r<----->i<----->n<----->g
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

print("********One Parameter****************************************")

print("sample_str[000] : ",sample_str[0]) #return 0th character

print("sample_str[001] : ",sample_str[1]) #return 1st character

print("sample_str[002] : ",sample_str[2]) #return 2nd character

print("sample_str[003] : ",sample_str[3]) #return 3rd character

print("sample_str[004] : ",sample_str[4]) #return 4th character

print("sample_str[005] : ",sample_str[5]) #return 5th character

print("sample_str[006] : ",sample_str[6]) #return 6th character

print("sample_str[007] : ",sample_str[7]) #return 7th character

print("sample_str[008] : ",sample_str[8]) #return 8th character

print("sample_str[009] : ",sample_str[9]) #return 9th character

print("sample_str[010] : ",sample_str[10]) #return 10th character

print("sample_str[011] : ",sample_str[11]) #return 11th character

print("sample_str[012] : ",sample_str[12]) #return 12th character

print("********Reverse****************************************")

print("sample_str[-01] : ",sample_str[-1]) #return last character

print("sample_str[-02] : ",sample_str[-2]) #return last but first character

print("sample_str[-03] : ",sample_str[-3]) #return last but second character

print("sample_str[-04] : ",sample_str[-4]) #return last but third character

print("sample_str[-05] : ",sample_str[-5]) #return last but forth character

print("sample_str[-06] : ",sample_str[-6]) #return last but fifth character

print("sample_str[-07] : ",sample_str[-7]) #return last but sixth character

print("sample_str[-08] : ",sample_str[-8]) #return last but seventh character

print("sample_str[-09] : ",sample_str[-9]) #return last but eigth character

print("sample_str[-10] : ",sample_str[-10]) #return last but ninth character

print("sample_str[-11] : ",sample_str[-11]) #return last but tenth character

print("sample_str[-12] : ",sample_str[-12]) #return last but eleventh character

print("sample_str[-13] : ",sample_str[-13]) #return last but twelth character


# In[14]:


#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# P<------>y<------>t<------>h<------>o<----->n<-----> <----->S<----->t<----->r<----->i<----->n<----->g
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

print("********Two Parameter****************************************")

print("********Left to Right****************************************")

print("sample_str[0:00] : ",sample_str[0:0]) 
print("sample_str[0:01] : ",sample_str[0:1]) 
print("sample_str[0:02] : ",sample_str[0:2]) 
print("sample_str[0:03] : ",sample_str[0:3]) 
print("sample_str[0:04] : ",sample_str[0:4]) 
print("sample_str[0:05] : ",sample_str[0:5]) 
print("sample_str[0:06] : ",sample_str[0:6]) 
print("sample_str[0:07] : ",sample_str[0:7]) 
print("sample_str[0:08] : ",sample_str[0:8]) 
print("sample_str[0:09] : ",sample_str[0:9]) 
print("sample_str[0:10] : ",sample_str[0:10]) 
print("sample_str[0:11] : ",sample_str[0:11]) 
print("sample_str[0:12] : ",sample_str[0:12]) 

print("*************************************************************")

print("sample_str[1:00] : ",sample_str[1:0]) 
print("sample_str[1:01] : ",sample_str[1:1]) 
print("sample_str[1:02] : ",sample_str[1:2]) 
print("sample_str[1:03] : ",sample_str[1:3]) 
print("sample_str[1:04] : ",sample_str[1:4]) 
print("sample_str[1:05] : ",sample_str[1:5]) 
print("sample_str[1:06] : ",sample_str[1:6]) 
print("sample_str[1:07] : ",sample_str[1:7]) 
print("sample_str[1:08] : ",sample_str[1:8]) 
print("sample_str[1:09] : ",sample_str[1:9]) 
print("sample_str[1:10] : ",sample_str[1:10]) 
print("sample_str[1:11] : ",sample_str[1:11]) 
print("sample_str[1:12] : ",sample_str[1:12])

print("*************************************************************")

print("sample_str[2:00] : ",sample_str[2:0]) 
print("sample_str[2:01] : ",sample_str[2:1]) 
print("sample_str[2:02] : ",sample_str[2:2]) 
print("sample_str[2:03] : ",sample_str[2:3]) 
print("sample_str[2:04] : ",sample_str[2:4]) 
print("sample_str[2:05] : ",sample_str[2:5]) 
print("sample_str[2:06] : ",sample_str[2:6]) 
print("sample_str[2:07] : ",sample_str[2:7]) 
print("sample_str[2:08] : ",sample_str[2:8]) 
print("sample_str[2:09] : ",sample_str[2:9]) 
print("sample_str[2:10] : ",sample_str[2:10]) 
print("sample_str[2:11] : ",sample_str[2:11]) 
print("sample_str[2:12] : ",sample_str[2:12]) 

print("*************************************************************")

print("sample_str[3:00] : ",sample_str[3:0]) 
print("sample_str[3:01] : ",sample_str[3:1]) 
print("sample_str[3:02] : ",sample_str[3:2]) 
print("sample_str[3:03] : ",sample_str[3:3]) 
print("sample_str[3:04] : ",sample_str[3:4]) 
print("sample_str[3:05] : ",sample_str[3:5]) 
print("sample_str[3:06] : ",sample_str[3:6]) 
print("sample_str[3:07] : ",sample_str[3:7]) 
print("sample_str[3:08] : ",sample_str[3:8]) 
print("sample_str[3:09] : ",sample_str[3:9]) 
print("sample_str[3:10] : ",sample_str[3:10]) 
print("sample_str[3:11] : ",sample_str[3:11]) 
print("sample_str[3:12] : ",sample_str[3:12]) 

print("*************************************************************")

print("sample_str[4:00] : ",sample_str[4:0]) 
print("sample_str[4:01] : ",sample_str[4:1]) 
print("sample_str[4:02] : ",sample_str[4:2]) 
print("sample_str[4:03] : ",sample_str[4:3]) 
print("sample_str[4:04] : ",sample_str[4:4]) 
print("sample_str[4:05] : ",sample_str[4:5]) 
print("sample_str[4:06] : ",sample_str[4:6]) 
print("sample_str[4:07] : ",sample_str[4:7]) 
print("sample_str[4:08] : ",sample_str[4:8]) 
print("sample_str[4:09] : ",sample_str[4:9]) 
print("sample_str[4:10] : ",sample_str[4:10]) 
print("sample_str[4:11] : ",sample_str[4:11]) 
print("sample_str[4:12] : ",sample_str[4:12]) 

print("*************************************************************")

print("sample_str[5:00] : ",sample_str[5:0]) 
print("sample_str[5:01] : ",sample_str[5:1]) 
print("sample_str[5:02] : ",sample_str[5:2]) 
print("sample_str[5:03] : ",sample_str[5:3]) 
print("sample_str[5:04] : ",sample_str[5:4]) 
print("sample_str[5:05] : ",sample_str[5:5]) 
print("sample_str[5:06] : ",sample_str[5:6]) 
print("sample_str[5:07] : ",sample_str[5:7]) 
print("sample_str[5:08] : ",sample_str[5:8]) 
print("sample_str[5:09] : ",sample_str[5:9]) 
print("sample_str[5:10] : ",sample_str[5:10]) 
print("sample_str[5:11] : ",sample_str[5:11]) 
print("sample_str[5:12] : ",sample_str[5:12])

print("*************************************************************")

print("sample_str[6:00] : ",sample_str[6:0]) 
print("sample_str[6:01] : ",sample_str[6:1]) 
print("sample_str[6:02] : ",sample_str[6:2]) 
print("sample_str[6:03] : ",sample_str[6:3]) 
print("sample_str[6:04] : ",sample_str[6:4]) 
print("sample_str[6:05] : ",sample_str[6:5]) 
print("sample_str[6:06] : ",sample_str[6:6]) 
print("sample_str[6:07] : ",sample_str[6:7]) 
print("sample_str[6:08] : ",sample_str[6:8]) 
print("sample_str[6:09] : ",sample_str[6:9]) 
print("sample_str[6:10] : ",sample_str[6:10]) 
print("sample_str[6:11] : ",sample_str[6:11]) 
print("sample_str[6:12] : ",sample_str[6:12])

print("*************************************************************")

print("sample_str[7:00] : ",sample_str[7:0]) 
print("sample_str[7:01] : ",sample_str[7:1]) 
print("sample_str[7:02] : ",sample_str[7:2]) 
print("sample_str[7:03] : ",sample_str[7:3]) 
print("sample_str[7:04] : ",sample_str[7:4]) 
print("sample_str[7:05] : ",sample_str[7:5]) 
print("sample_str[7:06] : ",sample_str[7:6]) 
print("sample_str[7:07] : ",sample_str[7:7]) 
print("sample_str[7:08] : ",sample_str[7:8]) 
print("sample_str[7:09] : ",sample_str[7:9]) 
print("sample_str[7:10] : ",sample_str[7:10]) 
print("sample_str[7:11] : ",sample_str[7:11]) 
print("sample_str[7:12] : ",sample_str[7:12])

print("*************************************************************")

print("sample_str[8:00] : ",sample_str[8:0]) 
print("sample_str[8:01] : ",sample_str[8:1]) 
print("sample_str[8:02] : ",sample_str[8:2]) 
print("sample_str[8:03] : ",sample_str[8:3]) 
print("sample_str[8:04] : ",sample_str[8:4]) 
print("sample_str[8:05] : ",sample_str[8:5]) 
print("sample_str[8:06] : ",sample_str[8:6]) 
print("sample_str[8:07] : ",sample_str[8:7]) 
print("sample_str[8:08] : ",sample_str[8:8]) 
print("sample_str[8:09] : ",sample_str[8:9]) 
print("sample_str[8:10] : ",sample_str[8:10]) 
print("sample_str[8:11] : ",sample_str[8:11]) 
print("sample_str[8:12] : ",sample_str[8:12])

print("*************************************************************")

print("sample_str[9:00] : ",sample_str[9:0]) 
print("sample_str[9:01] : ",sample_str[9:1]) 
print("sample_str[9:02] : ",sample_str[9:2]) 
print("sample_str[9:03] : ",sample_str[9:3]) 
print("sample_str[9:04] : ",sample_str[9:4]) 
print("sample_str[9:05] : ",sample_str[9:5]) 
print("sample_str[9:06] : ",sample_str[9:6]) 
print("sample_str[9:07] : ",sample_str[9:7]) 
print("sample_str[9:08] : ",sample_str[9:8]) 
print("sample_str[9:09] : ",sample_str[9:9]) 
print("sample_str[9:10] : ",sample_str[9:10]) 
print("sample_str[9:11] : ",sample_str[9:11]) 
print("sample_str[9:12] : ",sample_str[9:12])

print("*************************************************************")

print("sample_str[10:00] : ",sample_str[10:0]) 
print("sample_str[10:01] : ",sample_str[10:1]) 
print("sample_str[10:02] : ",sample_str[10:2]) 
print("sample_str[10:03] : ",sample_str[10:3]) 
print("sample_str[10:04] : ",sample_str[10:4]) 
print("sample_str[10:05] : ",sample_str[10:5]) 
print("sample_str[10:06] : ",sample_str[10:6]) 
print("sample_str[10:07] : ",sample_str[10:7]) 
print("sample_str[10:08] : ",sample_str[10:8]) 
print("sample_str[10:09] : ",sample_str[10:9]) 
print("sample_str[10:10] : ",sample_str[10:10]) 
print("sample_str[10:11] : ",sample_str[10:11]) 
print("sample_str[10:12] : ",sample_str[10:12])

print("*************************************************************")

print("sample_str[11:00] : ",sample_str[11:0]) 
print("sample_str[11:01] : ",sample_str[11:1]) 
print("sample_str[11:02] : ",sample_str[11:2]) 
print("sample_str[11:03] : ",sample_str[11:3]) 
print("sample_str[11:04] : ",sample_str[11:4]) 
print("sample_str[11:05] : ",sample_str[11:5]) 
print("sample_str[11:06] : ",sample_str[11:6]) 
print("sample_str[11:07] : ",sample_str[11:7]) 
print("sample_str[11:08] : ",sample_str[11:8]) 
print("sample_str[11:09] : ",sample_str[11:9]) 
print("sample_str[11:10] : ",sample_str[11:10]) 
print("sample_str[11:11] : ",sample_str[11:11]) 
print("sample_str[11:12] : ",sample_str[11:12])

print("*************************************************************")

print("sample_str[12:00] : ",sample_str[12:0]) 
print("sample_str[12:01] : ",sample_str[12:1]) 
print("sample_str[12:02] : ",sample_str[12:2]) 
print("sample_str[12:03] : ",sample_str[12:3]) 
print("sample_str[12:04] : ",sample_str[12:4]) 
print("sample_str[12:05] : ",sample_str[12:5]) 
print("sample_str[12:06] : ",sample_str[12:6]) 
print("sample_str[12:07] : ",sample_str[12:7]) 
print("sample_str[12:08] : ",sample_str[12:8]) 
print("sample_str[12:09] : ",sample_str[12:9]) 
print("sample_str[12:10] : ",sample_str[12:10]) 
print("sample_str[12:11] : ",sample_str[12:11]) 
print("sample_str[12:12] : ",sample_str[12:12])


# In[15]:


#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# P<------>y<------>t<------>h<------>o<----->n<-----> <----->S<----->t<----->r<----->i<----->n<----->g
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

print("********Three Parameter****************************************")

print("********Right to Left****************************************")

print("sample_str[0:00:-1] : ",sample_str[0:0:-1]) 
print("sample_str[0:01:-1] : ",sample_str[0:1:-1]) 
print("sample_str[0:02:-1] : ",sample_str[0:2:-1]) 
print("sample_str[0:03:-1] : ",sample_str[0:3:-1]) 
print("sample_str[0:04:-1] : ",sample_str[0:4:-1]) 
print("sample_str[0:05:-1] : ",sample_str[0:5:-1]) 
print("sample_str[0:06:-1] : ",sample_str[0:6:-1]) 
print("sample_str[0:07:-1] : ",sample_str[0:7:-1]) 
print("sample_str[0:08:-1] : ",sample_str[0:8:-1]) 
print("sample_str[0:09:-1] : ",sample_str[0:9:-1]) 
print("sample_str[0:10:-1] : ",sample_str[0:10:-1]) 
print("sample_str[0:11:-1] : ",sample_str[0:11:-1]) 
print("sample_str[0:12:-1] : ",sample_str[0:12:-1]) 

print("*************************************************************")

print("sample_str[1:00:-1] : ",sample_str[1:0:-1]) 
print("sample_str[1:01:-1] : ",sample_str[1:1:-1]) 
print("sample_str[1:02:-1] : ",sample_str[1:2:-1]) 
print("sample_str[1:03:-1] : ",sample_str[1:3:-1]) 
print("sample_str[1:04:-1] : ",sample_str[1:4:-1]) 
print("sample_str[1:05:-1] : ",sample_str[1:5:-1]) 
print("sample_str[1:06:-1] : ",sample_str[1:6:-1]) 
print("sample_str[1:07:-1] : ",sample_str[1:7:-1]) 
print("sample_str[1:08:-1] : ",sample_str[1:8:-1]) 
print("sample_str[1:09:-1] : ",sample_str[1:9:-1]) 
print("sample_str[1:10:-1] : ",sample_str[1:10:-1]) 
print("sample_str[1:11:-1] : ",sample_str[1:11:-1]) 
print("sample_str[1:12:-1] : ",sample_str[1:12:-1])

print("*************************************************************")

print("sample_str[2:00:-1] : ",sample_str[2:0:-1]) 
print("sample_str[2:01:-1] : ",sample_str[2:1:-1]) 
print("sample_str[2:02:-1] : ",sample_str[2:2:-1]) 
print("sample_str[2:03:-1] : ",sample_str[2:3:-1]) 
print("sample_str[2:04:-1] : ",sample_str[2:4:-1]) 
print("sample_str[2:05:-1] : ",sample_str[2:5:-1]) 
print("sample_str[2:06:-1] : ",sample_str[2:6:-1]) 
print("sample_str[2:07:-1] : ",sample_str[2:7:-1]) 
print("sample_str[2:08:-1] : ",sample_str[2:8:-1]) 
print("sample_str[2:09:-1] : ",sample_str[2:9:-1]) 
print("sample_str[2:10:-1] : ",sample_str[2:10:-1]) 
print("sample_str[2:11:-1] : ",sample_str[2:11:-1]) 
print("sample_str[2:12:-1] : ",sample_str[2:12:-1]) 

print("*************************************************************")

print("sample_str[3:00:-1] : ",sample_str[3:0:-1]) 
print("sample_str[3:01:-1] : ",sample_str[3:1:-1]) 
print("sample_str[3:02:-1] : ",sample_str[3:2:-1]) 
print("sample_str[3:03:-1] : ",sample_str[3:3:-1]) 
print("sample_str[3:04:-1] : ",sample_str[3:4:-1]) 
print("sample_str[3:05:-1] : ",sample_str[3:5:-1]) 
print("sample_str[3:06:-1] : ",sample_str[3:6:-1]) 
print("sample_str[3:07:-1] : ",sample_str[3:7:-1]) 
print("sample_str[3:08:-1] : ",sample_str[3:8:-1]) 
print("sample_str[3:09:-1] : ",sample_str[3:9:-1]) 
print("sample_str[3:10:-1] : ",sample_str[3:10:-1]) 
print("sample_str[3:11:-1] : ",sample_str[3:11:-1]) 
print("sample_str[3:12:-1] : ",sample_str[3:12:-1]) 

print("*************************************************************")

print("sample_str[4:00:-1] : ",sample_str[4:0:-1]) 
print("sample_str[4:01:-1] : ",sample_str[4:1:-1]) 
print("sample_str[4:02:-1] : ",sample_str[4:2:-1]) 
print("sample_str[4:03:-1] : ",sample_str[4:3:-1]) 
print("sample_str[4:04:-1] : ",sample_str[4:4:-1]) 
print("sample_str[4:05:-1] : ",sample_str[4:5:-1]) 
print("sample_str[4:06:-1] : ",sample_str[4:6:-1]) 
print("sample_str[4:07:-1] : ",sample_str[4:7:-1]) 
print("sample_str[4:08:-1] : ",sample_str[4:8:-1]) 
print("sample_str[4:09:-1] : ",sample_str[4:9:-1]) 
print("sample_str[4:10:-1] : ",sample_str[4:10:-1]) 
print("sample_str[4:11:-1] : ",sample_str[4:11:-1]) 
print("sample_str[4:12:-1] : ",sample_str[4:12:-1]) 

print("*************************************************************")

print("sample_str[5:00:-1] : ",sample_str[5:0:-1]) 
print("sample_str[5:01:-1] : ",sample_str[5:1:-1]) 
print("sample_str[5:02:-1] : ",sample_str[5:2:-1]) 
print("sample_str[5:03:-1] : ",sample_str[5:3:-1]) 
print("sample_str[5:04:-1] : ",sample_str[5:4:-1]) 
print("sample_str[5:05:-1] : ",sample_str[5:5:-1]) 
print("sample_str[5:06:-1] : ",sample_str[5:6:-1]) 
print("sample_str[5:07:-1] : ",sample_str[5:7:-1]) 
print("sample_str[5:08:-1] : ",sample_str[5:8:-1]) 
print("sample_str[5:09:-1] : ",sample_str[5:9:-1]) 
print("sample_str[5:10:-1] : ",sample_str[5:10:-1]) 
print("sample_str[5:11:-1] : ",sample_str[5:11:-1]) 
print("sample_str[5:12:-1] : ",sample_str[5:12:-1])

print("*************************************************************")

print("sample_str[6:00:-1] : ",sample_str[6:0:-1]) 
print("sample_str[6:01:-1] : ",sample_str[6:1:-1]) 
print("sample_str[6:02:-1] : ",sample_str[6:2:-1]) 
print("sample_str[6:03:-1] : ",sample_str[6:3:-1]) 
print("sample_str[6:04:-1] : ",sample_str[6:4:-1]) 
print("sample_str[6:05:-1] : ",sample_str[6:5:-1]) 
print("sample_str[6:06:-1] : ",sample_str[6:6:-1]) 
print("sample_str[6:07:-1] : ",sample_str[6:7:-1]) 
print("sample_str[6:08:-1] : ",sample_str[6:8:-1]) 
print("sample_str[6:09:-1] : ",sample_str[6:9:-1]) 
print("sample_str[6:10:-1] : ",sample_str[6:10:-1]) 
print("sample_str[6:11:-1] : ",sample_str[6:11:-1]) 
print("sample_str[6:12:-1] : ",sample_str[6:12:-1])

print("*************************************************************")

print("sample_str[7:00:-1] : ",sample_str[7:0:-1]) 
print("sample_str[7:01:-1] : ",sample_str[7:1:-1]) 
print("sample_str[7:02:-1] : ",sample_str[7:2:-1]) 
print("sample_str[7:03:-1] : ",sample_str[7:3:-1]) 
print("sample_str[7:04:-1] : ",sample_str[7:4:-1]) 
print("sample_str[7:05:-1] : ",sample_str[7:5:-1]) 
print("sample_str[7:06:-1] : ",sample_str[7:6:-1]) 
print("sample_str[7:07:-1] : ",sample_str[7:7:-1]) 
print("sample_str[7:08:-1] : ",sample_str[7:8:-1]) 
print("sample_str[7:09:-1] : ",sample_str[7:9:-1]) 
print("sample_str[7:10:-1] : ",sample_str[7:10:-1]) 
print("sample_str[7:11:-1] : ",sample_str[7:11:-1]) 
print("sample_str[7:12:-1] : ",sample_str[7:12:-1])

print("*************************************************************")

print("sample_str[8:00:-1] : ",sample_str[8:0:-1]) 
print("sample_str[8:01:-1] : ",sample_str[8:1:-1]) 
print("sample_str[8:02:-1] : ",sample_str[8:2:-1]) 
print("sample_str[8:03:-1] : ",sample_str[8:3:-1]) 
print("sample_str[8:04:-1] : ",sample_str[8:4:-1]) 
print("sample_str[8:05:-1] : ",sample_str[8:5:-1]) 
print("sample_str[8:06:-1] : ",sample_str[8:6:-1]) 
print("sample_str[8:07:-1] : ",sample_str[8:7:-1]) 
print("sample_str[8:08:-1] : ",sample_str[8:8:-1]) 
print("sample_str[8:09:-1] : ",sample_str[8:9:-1]) 
print("sample_str[8:10:-1] : ",sample_str[8:10:-1]) 
print("sample_str[8:11:-1] : ",sample_str[8:11:-1]) 
print("sample_str[8:12:-1] : ",sample_str[8:12:-1])

print("*************************************************************")

print("sample_str[9:00:-1] : ",sample_str[9:0:-1]) 
print("sample_str[9:01:-1] : ",sample_str[9:1:-1]) 
print("sample_str[9:02:-1] : ",sample_str[9:2:-1]) 
print("sample_str[9:03:-1] : ",sample_str[9:3:-1]) 
print("sample_str[9:04:-1] : ",sample_str[9:4:-1]) 
print("sample_str[9:05:-1] : ",sample_str[9:5:-1]) 
print("sample_str[9:06:-1] : ",sample_str[9:6:-1]) 
print("sample_str[9:07:-1] : ",sample_str[9:7:-1]) 
print("sample_str[9:08:-1] : ",sample_str[9:8:-1]) 
print("sample_str[9:09:-1] : ",sample_str[9:9:-1]) 
print("sample_str[9:10:-1] : ",sample_str[9:10:-1]) 
print("sample_str[9:11:-1] : ",sample_str[9:11:-1]) 
print("sample_str[9:12:-1] : ",sample_str[9:12:-1])

print("*************************************************************")

print("sample_str[10:00:-1] : ",sample_str[10:0:-1]) 
print("sample_str[10:01:-1] : ",sample_str[10:1:-1]) 
print("sample_str[10:02:-1] : ",sample_str[10:2:-1]) 
print("sample_str[10:03:-1] : ",sample_str[10:3:-1]) 
print("sample_str[10:04:-1] : ",sample_str[10:4:-1]) 
print("sample_str[10:05:-1] : ",sample_str[10:5:-1]) 
print("sample_str[10:06:-1] : ",sample_str[10:6:-1]) 
print("sample_str[10:07:-1] : ",sample_str[10:7:-1]) 
print("sample_str[10:08:-1] : ",sample_str[10:8:-1]) 
print("sample_str[10:09:-1] : ",sample_str[10:9:-1]) 
print("sample_str[10:10:-1] : ",sample_str[10:10:-1]) 
print("sample_str[10:11:-1] : ",sample_str[10:11:-1]) 
print("sample_str[10:12:-1] : ",sample_str[10:12:-1])

print("*************************************************************")

print("sample_str[11:00:-1] : ",sample_str[11:0:-1]) 
print("sample_str[11:01:-1] : ",sample_str[11:1:-1]) 
print("sample_str[11:02:-1] : ",sample_str[11:2:-1]) 
print("sample_str[11:03:-1] : ",sample_str[11:3:-1]) 
print("sample_str[11:04:-1] : ",sample_str[11:4:-1]) 
print("sample_str[11:05:-1] : ",sample_str[11:5:-1]) 
print("sample_str[11:06:-1] : ",sample_str[11:6:-1]) 
print("sample_str[11:07:-1] : ",sample_str[11:7:-1]) 
print("sample_str[11:08:-1] : ",sample_str[11:8:-1]) 
print("sample_str[11:09:-1] : ",sample_str[11:9:-1]) 
print("sample_str[11:10:-1] : ",sample_str[11:10:-1]) 
print("sample_str[11:11:-1] : ",sample_str[11:11:-1]) 
print("sample_str[11:12:-1] : ",sample_str[11:12:-1])

print("*************************************************************")

print("sample_str[12:00:-1] : ",sample_str[12:0:-1]) 
print("sample_str[12:01:-1] : ",sample_str[12:1:-1]) 
print("sample_str[12:02:-1] : ",sample_str[12:2:-1]) 
print("sample_str[12:03:-1] : ",sample_str[12:3:-1]) 
print("sample_str[12:04:-1] : ",sample_str[12:4:-1]) 
print("sample_str[12:05:-1] : ",sample_str[12:5:-1]) 
print("sample_str[12:06:-1] : ",sample_str[12:6:-1]) 
print("sample_str[12:07:-1] : ",sample_str[12:7:-1]) 
print("sample_str[12:08:-1] : ",sample_str[12:8:-1]) 
print("sample_str[12:09:-1] : ",sample_str[12:9:-1]) 
print("sample_str[12:10:-1] : ",sample_str[12:10:-1]) 
print("sample_str[12:11:-1] : ",sample_str[12:11:-1]) 
print("sample_str[12:12:-1] : ",sample_str[12:12:-1])


# In[16]:


#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# P<------>y<------>t<------>h<------>o<----->n<-----> <----->S<----->t<----->r<----->i<----->n<----->g
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

print("********Three Parameter****************************************")

print("********Right to Left - Negative Start and Negative End *****")

print("sample_str[-0:-00:-1] : ",sample_str[-0:-0:-1]) 
print("sample_str[-0:-01:-1] : ",sample_str[-0:-1:-1]) 
print("sample_str[-0:-02:-1] : ",sample_str[-0:-2:-1]) 
print("sample_str[-0:-03:-1] : ",sample_str[-0:-3:-1]) 
print("sample_str[-0:-04:-1] : ",sample_str[-0:-4:-1]) 
print("sample_str[-0:-05:-1] : ",sample_str[-0:-5:-1]) 
print("sample_str[-0:-06:-1] : ",sample_str[-0:-6:-1]) 
print("sample_str[-0:-07:-1] : ",sample_str[-0:-7:-1]) 
print("sample_str[-0:-08:-1] : ",sample_str[-0:-8:-1]) 
print("sample_str[-0:-09:-1] : ",sample_str[-0:-9:-1]) 
print("sample_str[-0:-10:-1] : ",sample_str[-0:-10:-1]) 
print("sample_str[-0:-11:-1] : ",sample_str[-0:-11:-1]) 
print("sample_str[-0:-12:-1] : ",sample_str[-0:-12:-1]) 

print("*************************************************************")

print("sample_str[-1:-00:-1] : ",sample_str[-1:-0:-1]) 
print("sample_str[-1:-01:-1] : ",sample_str[-1:-1:-1]) 
print("sample_str[-1:-02:-1] : ",sample_str[-1:-2:-1]) 
print("sample_str[-1:-03:-1] : ",sample_str[-1:-3:-1]) 
print("sample_str[-1:-04:-1] : ",sample_str[-1:-4:-1]) 
print("sample_str[-1:-05:-1] : ",sample_str[-1:-5:-1]) 
print("sample_str[-1:-06:-1] : ",sample_str[-1:-6:-1]) 
print("sample_str[-1:-07:-1] : ",sample_str[-1:-7:-1]) 
print("sample_str[-1:-08:-1] : ",sample_str[-1:-8:-1]) 
print("sample_str[-1:-09:-1] : ",sample_str[-1:-9:-1]) 
print("sample_str[-1:-10:-1] : ",sample_str[-1:-10:-1]) 
print("sample_str[-1:-11:-1] : ",sample_str[-1:-11:-1]) 
print("sample_str[-1:-12:-1] : ",sample_str[-1:-12:-1])

print("*************************************************************")

print("sample_str[-2:-00:-1] : ",sample_str[-2:-0:-1]) 
print("sample_str[-2:-01:-1] : ",sample_str[-2:-1:-1]) 
print("sample_str[-2:-02:-1] : ",sample_str[-2:-2:-1]) 
print("sample_str[-2:-03:-1] : ",sample_str[-2:-3:-1]) 
print("sample_str[-2:-04:-1] : ",sample_str[-2:-4:-1]) 
print("sample_str[-2:-05:-1] : ",sample_str[-2:-5:-1]) 
print("sample_str[-2:-06:-1] : ",sample_str[-2:-6:-1]) 
print("sample_str[-2:-07:-1] : ",sample_str[-2:-7:-1]) 
print("sample_str[-2:-08:-1] : ",sample_str[-2:-8:-1]) 
print("sample_str[-2:-09:-1] : ",sample_str[-2:-9:-1]) 
print("sample_str[-2:-10:-1] : ",sample_str[-2:-10:-1]) 
print("sample_str[-2:-11:-1] : ",sample_str[-2:-11:-1]) 
print("sample_str[-2:-12:-1] : ",sample_str[-2:-12:-1]) 

print("*************************************************************")

print("sample_str[-3:-00:-1] : ",sample_str[-3:-0:-1]) 
print("sample_str[-3:-01:-1] : ",sample_str[-3:-1:-1]) 
print("sample_str[-3:-02:-1] : ",sample_str[-3:-2:-1]) 
print("sample_str[-3:-03:-1] : ",sample_str[-3:-3:-1]) 
print("sample_str[-3:-04:-1] : ",sample_str[-3:-4:-1]) 
print("sample_str[-3:-05:-1] : ",sample_str[-3:-5:-1]) 
print("sample_str[-3:-06:-1] : ",sample_str[-3:-6:-1]) 
print("sample_str[-3:-07:-1] : ",sample_str[-3:-7:-1]) 
print("sample_str[-3:-08:-1] : ",sample_str[-3:-8:-1]) 
print("sample_str[-3:-09:-1] : ",sample_str[-3:-9:-1]) 
print("sample_str[-3:-10:-1] : ",sample_str[-3:-10:-1]) 
print("sample_str[-3:-11:-1] : ",sample_str[-3:-11:-1]) 
print("sample_str[-3:-12:-1] : ",sample_str[-3:-12:-1]) 

print("*************************************************************")

print("sample_str[-4:-00:-1] : ",sample_str[-4:-0:-1]) 
print("sample_str[-4:-01:-1] : ",sample_str[-4:-1:-1]) 
print("sample_str[-4:-02:-1] : ",sample_str[-4:-2:-1]) 
print("sample_str[-4:-03:-1] : ",sample_str[-4:-3:-1]) 
print("sample_str[-4:-04:-1] : ",sample_str[-4:-4:-1]) 
print("sample_str[-4:-05:-1] : ",sample_str[-4:-5:-1]) 
print("sample_str[-4:-06:-1] : ",sample_str[-4:-6:-1]) 
print("sample_str[-4:-07:-1] : ",sample_str[-4:-7:-1]) 
print("sample_str[-4:-08:-1] : ",sample_str[-4:-8:-1]) 
print("sample_str[-4:-09:-1] : ",sample_str[-4:-9:-1]) 
print("sample_str[-4:-10:-1] : ",sample_str[-4:-10:-1]) 
print("sample_str[-4:-11:-1] : ",sample_str[-4:-11:-1]) 
print("sample_str[-4:-12:-1] : ",sample_str[-4:-12:-1]) 

print("*************************************************************")

print("sample_str[-5:-00:-1] : ",sample_str[-5:-0:-1]) 
print("sample_str[-5:-01:-1] : ",sample_str[-5:-1:-1]) 
print("sample_str[-5:-02:-1] : ",sample_str[-5:-2:-1]) 
print("sample_str[-5:-03:-1] : ",sample_str[-5:-3:-1]) 
print("sample_str[-5:-04:-1] : ",sample_str[-5:-4:-1]) 
print("sample_str[-5:-05:-1] : ",sample_str[-5:-5:-1]) 
print("sample_str[-5:-06:-1] : ",sample_str[-5:-6:-1]) 
print("sample_str[-5:-07:-1] : ",sample_str[-5:-7:-1]) 
print("sample_str[-5:-08:-1] : ",sample_str[-5:-8:-1]) 
print("sample_str[-5:-09:-1] : ",sample_str[-5:-9:-1]) 
print("sample_str[-5:-10:-1] : ",sample_str[-5:-10:-1]) 
print("sample_str[-5:-11:-1] : ",sample_str[-5:-11:-1]) 
print("sample_str[-5:-12:-1] : ",sample_str[-5:-12:-1])

print("*************************************************************")

print("sample_str[-6:-00:-1] : ",sample_str[-6:-0:-1]) 
print("sample_str[-6:-01:-1] : ",sample_str[-6:-1:-1]) 
print("sample_str[-6:-02:-1] : ",sample_str[-6:-2:-1]) 
print("sample_str[-6:-03:-1] : ",sample_str[-6:-3:-1]) 
print("sample_str[-6:-04:-1] : ",sample_str[-6:-4:-1]) 
print("sample_str[-6:-05:-1] : ",sample_str[-6:-5:-1]) 
print("sample_str[-6:-06:-1] : ",sample_str[-6:-6:-1]) 
print("sample_str[-6:-07:-1] : ",sample_str[-6:-7:-1]) 
print("sample_str[-6:-08:-1] : ",sample_str[-6:-8:-1]) 
print("sample_str[-6:-09:-1] : ",sample_str[-6:-9:-1]) 
print("sample_str[-6:-10:-1] : ",sample_str[-6:-10:-1]) 
print("sample_str[-6:-11:-1] : ",sample_str[-6:-11:-1]) 
print("sample_str[-6:-12:-1] : ",sample_str[-6:-12:-1])

print("*************************************************************")

print("sample_str[-7:-00:-1] : ",sample_str[-7:-0:-1]) 
print("sample_str[-7:-01:-1] : ",sample_str[-7:-1:-1]) 
print("sample_str[-7:-02:-1] : ",sample_str[-7:-2:-1]) 
print("sample_str[-7:-03:-1] : ",sample_str[-7:-3:-1]) 
print("sample_str[-7:-04:-1] : ",sample_str[-7:-4:-1]) 
print("sample_str[-7:-05:-1] : ",sample_str[-7:-5:-1]) 
print("sample_str[-7:-06:-1] : ",sample_str[-7:-6:-1]) 
print("sample_str[-7:-07:-1] : ",sample_str[-7:-7:-1]) 
print("sample_str[-7:-08:-1] : ",sample_str[-7:-8:-1]) 
print("sample_str[-7:-09:-1] : ",sample_str[-7:-9:-1]) 
print("sample_str[-7:-10:-1] : ",sample_str[-7:-10:-1]) 
print("sample_str[-7:-11:-1] : ",sample_str[-7:-11:-1]) 
print("sample_str[-7:-12:-1] : ",sample_str[-7:-12:-1])

print("*************************************************************")

print("sample_str[-8:-00:-1] : ",sample_str[-8:-0:-1]) 
print("sample_str[-8:-01:-1] : ",sample_str[-8:-1:-1]) 
print("sample_str[-8:-02:-1] : ",sample_str[-8:-2:-1]) 
print("sample_str[-8:-03:-1] : ",sample_str[-8:-3:-1]) 
print("sample_str[-8:-04:-1] : ",sample_str[-8:-4:-1]) 
print("sample_str[-8:-05:-1] : ",sample_str[-8:-5:-1]) 
print("sample_str[-8:-06:-1] : ",sample_str[-8:-6:-1]) 
print("sample_str[-8:-07:-1] : ",sample_str[-8:-7:-1]) 
print("sample_str[-8:-08:-1] : ",sample_str[-8:-8:-1]) 
print("sample_str[-8:-09:-1] : ",sample_str[-8:-9:-1]) 
print("sample_str[-8:-10:-1] : ",sample_str[-8:-10:-1]) 
print("sample_str[-8:-11:-1] : ",sample_str[-8:-11:-1]) 
print("sample_str[-8:-12:-1] : ",sample_str[-8:-12:-1])

print("*************************************************************")

print("sample_str[-9:-00:-1] : ",sample_str[-9:-0:-1]) 
print("sample_str[-9:-01:-1] : ",sample_str[-9:-1:-1]) 
print("sample_str[-9:-02:-1] : ",sample_str[-9:-2:-1]) 
print("sample_str[-9:-03:-1] : ",sample_str[-9:-3:-1]) 
print("sample_str[-9:-04:-1] : ",sample_str[-9:-4:-1]) 
print("sample_str[-9:-05:-1] : ",sample_str[-9:-5:-1]) 
print("sample_str[-9:-06:-1] : ",sample_str[-9:-6:-1]) 
print("sample_str[-9:-07:-1] : ",sample_str[-9:-7:-1]) 
print("sample_str[-9:-08:-1] : ",sample_str[-9:-8:-1]) 
print("sample_str[-9:-09:-1] : ",sample_str[-9:-9:-1]) 
print("sample_str[-9:-10:-1] : ",sample_str[-9:-10:-1]) 
print("sample_str[-9:-11:-1] : ",sample_str[-9:-11:-1]) 
print("sample_str[-9:-12:-1] : ",sample_str[-9:-12:-1])

print("*************************************************************")

print("sample_str[-10:-00:-1] : ",sample_str[-10:-0:-1]) 
print("sample_str[-10:-01:-1] : ",sample_str[-10:-1:-1]) 
print("sample_str[-10:-02:-1] : ",sample_str[-10:-2:-1]) 
print("sample_str[-10:-03:-1] : ",sample_str[-10:-3:-1]) 
print("sample_str[-10:-04:-1] : ",sample_str[-10:-4:-1]) 
print("sample_str[-10:-05:-1] : ",sample_str[-10:-5:-1]) 
print("sample_str[-10:-06:-1] : ",sample_str[-10:-6:-1]) 
print("sample_str[-10:-07:-1] : ",sample_str[-10:-7:-1]) 
print("sample_str[-10:-08:-1] : ",sample_str[-10:-8:-1]) 
print("sample_str[-10:-09:-1] : ",sample_str[-10:-9:-1]) 
print("sample_str[-10:-10:-1] : ",sample_str[-10:-10:-1]) 
print("sample_str[-10:-11:-1] : ",sample_str[-10:-11:-1]) 
print("sample_str[-10:-12:-1] : ",sample_str[-10:-12:-1])

print("*************************************************************")

print("sample_str[-11:-00:-1] : ",sample_str[-11:-0:-1]) 
print("sample_str[-11:-01:-1] : ",sample_str[-11:-1:-1]) 
print("sample_str[-11:-02:-1] : ",sample_str[-11:-2:-1]) 
print("sample_str[-11:-03:-1] : ",sample_str[-11:-3:-1]) 
print("sample_str[-11:-04:-1] : ",sample_str[-11:-4:-1]) 
print("sample_str[-11:-05:-1] : ",sample_str[-11:-5:-1]) 
print("sample_str[-11:-06:-1] : ",sample_str[-11:-6:-1]) 
print("sample_str[-11:-07:-1] : ",sample_str[-11:-7:-1]) 
print("sample_str[-11:-08:-1] : ",sample_str[-11:-8:-1]) 
print("sample_str[-11:-09:-1] : ",sample_str[-11:-9:-1]) 
print("sample_str[-11:-10:-1] : ",sample_str[-11:-10:-1]) 
print("sample_str[-11:-11:-1] : ",sample_str[-11:-11:-1]) 
print("sample_str[-11:-12:-1] : ",sample_str[-11:-12:-1])

print("*************************************************************")

print("sample_str[-12:-00:-1] : ",sample_str[-12:-0:-1]) 
print("sample_str[-12:-01:-1] : ",sample_str[-12:-1:-1]) 
print("sample_str[-12:-02:-1] : ",sample_str[-12:-2:-1]) 
print("sample_str[-12:-03:-1] : ",sample_str[-12:-3:-1]) 
print("sample_str[-12:-04:-1] : ",sample_str[-12:-4:-1]) 
print("sample_str[-12:-05:-1] : ",sample_str[-12:-5:-1]) 
print("sample_str[-12:-06:-1] : ",sample_str[-12:-6:-1]) 
print("sample_str[-12:-07:-1] : ",sample_str[-12:-7:-1]) 
print("sample_str[-12:-08:-1] : ",sample_str[-12:-8:-1]) 
print("sample_str[-12:-09:-1] : ",sample_str[-12:-9:-1]) 
print("sample_str[-12:-10:-1] : ",sample_str[-12:-10:-1]) 
print("sample_str[-12:-11:-1] : ",sample_str[-12:-11:-1]) 
print("sample_str[-12:-12:-1] : ",sample_str[-12:-12:-1])


# In[17]:


# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12
# P<------>y<------>t<------>h<------>o<----->n<-----> <----->S<----->t<----->r<----->i<----->n<----->g
#(-13)--->(-12)--->(-11)--->(-10)--->(-9)--->(-8)--->(-7)--->(-6)--->(-5)--->(-4)--->(-3)--->(-2)--->(-1)

print("********Three Parameter****************************************")

print("********Right to Left - Negative Start and Positive End*****")

print("sample_str[-0:00:-1] : ",sample_str[-0:0:-1]) 
print("sample_str[-0:01:-1] : ",sample_str[-0:1:-1]) 
print("sample_str[-0:02:-1] : ",sample_str[-0:2:-1]) 
print("sample_str[-0:03:-1] : ",sample_str[-0:3:-1]) 
print("sample_str[-0:04:-1] : ",sample_str[-0:4:-1]) 
print("sample_str[-0:05:-1] : ",sample_str[-0:5:-1]) 
print("sample_str[-0:06:-1] : ",sample_str[-0:6:-1]) 
print("sample_str[-0:07:-1] : ",sample_str[-0:7:-1]) 
print("sample_str[-0:08:-1] : ",sample_str[-0:8:-1]) 
print("sample_str[-0:09:-1] : ",sample_str[-0:9:-1]) 
print("sample_str[-0:10:-1] : ",sample_str[-0:10:-1]) 
print("sample_str[-0:11:-1] : ",sample_str[-0:11:-1]) 
print("sample_str[-0:12:-1] : ",sample_str[-0:12:-1]) 

print("*************************************************************")

print("sample_str[-1:00:-1] : ",sample_str[-1:0:-1]) 
print("sample_str[-1:01:-1] : ",sample_str[-1:1:-1]) 
print("sample_str[-1:02:-1] : ",sample_str[-1:2:-1]) 
print("sample_str[-1:03:-1] : ",sample_str[-1:3:-1]) 
print("sample_str[-1:04:-1] : ",sample_str[-1:4:-1]) 
print("sample_str[-1:05:-1] : ",sample_str[-1:5:-1]) 
print("sample_str[-1:06:-1] : ",sample_str[-1:6:-1]) 
print("sample_str[-1:07:-1] : ",sample_str[-1:7:-1]) 
print("sample_str[-1:08:-1] : ",sample_str[-1:8:-1]) 
print("sample_str[-1:09:-1] : ",sample_str[-1:9:-1]) 
print("sample_str[-1:10:-1] : ",sample_str[-1:10:-1]) 
print("sample_str[-1:11:-1] : ",sample_str[-1:11:-1]) 
print("sample_str[-1:12:-1] : ",sample_str[-1:12:-1])

print("*************************************************************")

print("sample_str[-2:00:-1] : ",sample_str[-2:0:-1]) 
print("sample_str[-2:01:-1] : ",sample_str[-2:1:-1]) 
print("sample_str[-2:02:-1] : ",sample_str[-2:2:-1]) 
print("sample_str[-2:03:-1] : ",sample_str[-2:3:-1]) 
print("sample_str[-2:04:-1] : ",sample_str[-2:4:-1]) 
print("sample_str[-2:05:-1] : ",sample_str[-2:5:-1]) 
print("sample_str[-2:06:-1] : ",sample_str[-2:6:-1]) 
print("sample_str[-2:07:-1] : ",sample_str[-2:7:-1]) 
print("sample_str[-2:08:-1] : ",sample_str[-2:8:-1]) 
print("sample_str[-2:09:-1] : ",sample_str[-2:9:-1]) 
print("sample_str[-2:10:-1] : ",sample_str[-2:10:-1]) 
print("sample_str[-2:11:-1] : ",sample_str[-2:11:-1]) 
print("sample_str[-2:12:-1] : ",sample_str[-2:12:-1]) 

print("*************************************************************")

print("sample_str[-3:00:-1] : ",sample_str[-3:0:-1]) 
print("sample_str[-3:01:-1] : ",sample_str[-3:1:-1]) 
print("sample_str[-3:02:-1] : ",sample_str[-3:2:-1]) 
print("sample_str[-3:03:-1] : ",sample_str[-3:3:-1]) 
print("sample_str[-3:04:-1] : ",sample_str[-3:4:-1]) 
print("sample_str[-3:05:-1] : ",sample_str[-3:5:-1]) 
print("sample_str[-3:06:-1] : ",sample_str[-3:6:-1]) 
print("sample_str[-3:07:-1] : ",sample_str[-3:7:-1]) 
print("sample_str[-3:08:-1] : ",sample_str[-3:8:-1]) 
print("sample_str[-3:09:-1] : ",sample_str[-3:9:-1]) 
print("sample_str[-3:10:-1] : ",sample_str[-3:10:-1]) 
print("sample_str[-3:11:-1] : ",sample_str[-3:11:-1]) 
print("sample_str[-3:12:-1] : ",sample_str[-3:12:-1]) 

print("*************************************************************")

print("sample_str[-4:00:-1] : ",sample_str[-4:0:-1]) 
print("sample_str[-4:01:-1] : ",sample_str[-4:1:-1]) 
print("sample_str[-4:02:-1] : ",sample_str[-4:2:-1]) 
print("sample_str[-4:03:-1] : ",sample_str[-4:3:-1]) 
print("sample_str[-4:04:-1] : ",sample_str[-4:4:-1]) 
print("sample_str[-4:05:-1] : ",sample_str[-4:5:-1]) 
print("sample_str[-4:06:-1] : ",sample_str[-4:6:-1]) 
print("sample_str[-4:07:-1] : ",sample_str[-4:7:-1]) 
print("sample_str[-4:08:-1] : ",sample_str[-4:8:-1]) 
print("sample_str[-4:09:-1] : ",sample_str[-4:9:-1]) 
print("sample_str[-4:10:-1] : ",sample_str[-4:10:-1]) 
print("sample_str[-4:11:-1] : ",sample_str[-4:11:-1]) 
print("sample_str[-4:12:-1] : ",sample_str[-4:12:-1]) 

print("*************************************************************")

print("sample_str[-5:00:-1] : ",sample_str[-5:0:-1]) 
print("sample_str[-5:01:-1] : ",sample_str[-5:1:-1]) 
print("sample_str[-5:02:-1] : ",sample_str[-5:2:-1]) 
print("sample_str[-5:03:-1] : ",sample_str[-5:3:-1]) 
print("sample_str[-5:04:-1] : ",sample_str[-5:4:-1]) 
print("sample_str[-5:05:-1] : ",sample_str[-5:5:-1]) 
print("sample_str[-5:06:-1] : ",sample_str[-5:6:-1]) 
print("sample_str[-5:07:-1] : ",sample_str[-5:7:-1]) 
print("sample_str[-5:08:-1] : ",sample_str[-5:8:-1]) 
print("sample_str[-5:09:-1] : ",sample_str[-5:9:-1]) 
print("sample_str[-5:10:-1] : ",sample_str[-5:10:-1]) 
print("sample_str[-5:11:-1] : ",sample_str[-5:11:-1]) 
print("sample_str[-5:12:-1] : ",sample_str[-5:12:-1])

print("*************************************************************")

print("sample_str[-6:00:-1] : ",sample_str[-6:0:-1]) 
print("sample_str[-6:01:-1] : ",sample_str[-6:1:-1]) 
print("sample_str[-6:02:-1] : ",sample_str[-6:2:-1]) 
print("sample_str[-6:03:-1] : ",sample_str[-6:3:-1]) 
print("sample_str[-6:04:-1] : ",sample_str[-6:4:-1]) 
print("sample_str[-6:05:-1] : ",sample_str[-6:5:-1]) 
print("sample_str[-6:06:-1] : ",sample_str[-6:6:-1]) 
print("sample_str[-6:07:-1] : ",sample_str[-6:7:-1]) 
print("sample_str[-6:08:-1] : ",sample_str[-6:8:-1]) 
print("sample_str[-6:09:-1] : ",sample_str[-6:9:-1]) 
print("sample_str[-6:10:-1] : ",sample_str[-6:10:-1]) 
print("sample_str[-6:11:-1] : ",sample_str[-6:11:-1]) 
print("sample_str[-6:12:-1] : ",sample_str[-6:12:-1])

print("*************************************************************")

print("sample_str[-7:00:-1] : ",sample_str[-7:0:-1]) 
print("sample_str[-7:01:-1] : ",sample_str[-7:1:-1]) 
print("sample_str[-7:02:-1] : ",sample_str[-7:2:-1]) 
print("sample_str[-7:03:-1] : ",sample_str[-7:3:-1]) 
print("sample_str[-7:04:-1] : ",sample_str[-7:4:-1]) 
print("sample_str[-7:05:-1] : ",sample_str[-7:5:-1]) 
print("sample_str[-7:06:-1] : ",sample_str[-7:6:-1]) 
print("sample_str[-7:07:-1] : ",sample_str[-7:7:-1]) 
print("sample_str[-7:08:-1] : ",sample_str[-7:8:-1]) 
print("sample_str[-7:09:-1] : ",sample_str[-7:9:-1]) 
print("sample_str[-7:10:-1] : ",sample_str[-7:10:-1]) 
print("sample_str[-7:11:-1] : ",sample_str[-7:11:-1]) 
print("sample_str[-7:12:-1] : ",sample_str[-7:12:-1])

print("*************************************************************")

print("sample_str[-8:00:-1] : ",sample_str[-8:0:-1]) 
print("sample_str[-8:01:-1] : ",sample_str[-8:1:-1]) 
print("sample_str[-8:02:-1] : ",sample_str[-8:2:-1]) 
print("sample_str[-8:03:-1] : ",sample_str[-8:3:-1]) 
print("sample_str[-8:04:-1] : ",sample_str[-8:4:-1]) 
print("sample_str[-8:05:-1] : ",sample_str[-8:5:-1]) 
print("sample_str[-8:06:-1] : ",sample_str[-8:6:-1]) 
print("sample_str[-8:07:-1] : ",sample_str[-8:7:-1]) 
print("sample_str[-8:08:-1] : ",sample_str[-8:8:-1]) 
print("sample_str[-8:09:-1] : ",sample_str[-8:9:-1]) 
print("sample_str[-8:10:-1] : ",sample_str[-8:10:-1]) 
print("sample_str[-8:11:-1] : ",sample_str[-8:11:-1]) 
print("sample_str[-8:12:-1] : ",sample_str[-8:12:-1])

print("*************************************************************")

print("sample_str[-9:00:-1] : ",sample_str[-9:0:-1]) 
print("sample_str[-9:01:-1] : ",sample_str[-9:1:-1]) 
print("sample_str[-9:02:-1] : ",sample_str[-9:2:-1]) 
print("sample_str[-9:03:-1] : ",sample_str[-9:3:-1]) 
print("sample_str[-9:04:-1] : ",sample_str[-9:4:-1]) 
print("sample_str[-9:05:-1] : ",sample_str[-9:5:-1]) 
print("sample_str[-9:06:-1] : ",sample_str[-9:6:-1]) 
print("sample_str[-9:07:-1] : ",sample_str[-9:7:-1]) 
print("sample_str[-9:08:-1] : ",sample_str[-9:8:-1]) 
print("sample_str[-9:09:-1] : ",sample_str[-9:9:-1]) 
print("sample_str[-9:10:-1] : ",sample_str[-9:10:-1]) 
print("sample_str[-9:11:-1] : ",sample_str[-9:11:-1]) 
print("sample_str[-9:12:-1] : ",sample_str[-9:12:-1])

print("*************************************************************")

print("sample_str[-10:00:-1] : ",sample_str[-10:0:-1]) 
print("sample_str[-10:01:-1] : ",sample_str[-10:1:-1]) 
print("sample_str[-10:02:-1] : ",sample_str[-10:2:-1]) 
print("sample_str[-10:03:-1] : ",sample_str[-10:3:-1]) 
print("sample_str[-10:04:-1] : ",sample_str[-10:4:-1]) 
print("sample_str[-10:05:-1] : ",sample_str[-10:5:-1]) 
print("sample_str[-10:06:-1] : ",sample_str[-10:6:-1]) 
print("sample_str[-10:07:-1] : ",sample_str[-10:7:-1]) 
print("sample_str[-10:08:-1] : ",sample_str[-10:8:-1]) 
print("sample_str[-10:09:-1] : ",sample_str[-10:9:-1]) 
print("sample_str[-10:10:-1] : ",sample_str[-10:10:-1]) 
print("sample_str[-10:11:-1] : ",sample_str[-10:11:-1]) 
print("sample_str[-10:12:-1] : ",sample_str[-10:12:-1])

print("*************************************************************")

print("sample_str[-11:00:-1] : ",sample_str[-11:0:-1]) 
print("sample_str[-11:01:-1] : ",sample_str[-11:1:-1]) 
print("sample_str[-11:02:-1] : ",sample_str[-11:2:-1]) 
print("sample_str[-11:03:-1] : ",sample_str[-11:3:-1]) 
print("sample_str[-11:04:-1] : ",sample_str[-11:4:-1]) 
print("sample_str[-11:05:-1] : ",sample_str[-11:5:-1]) 
print("sample_str[-11:06:-1] : ",sample_str[-11:6:-1]) 
print("sample_str[-11:07:-1] : ",sample_str[-11:7:-1]) 
print("sample_str[-11:08:-1] : ",sample_str[-11:8:-1]) 
print("sample_str[-11:09:-1] : ",sample_str[-11:9:-1]) 
print("sample_str[-11:10:-1] : ",sample_str[-11:10:-1]) 
print("sample_str[-11:11:-1] : ",sample_str[-11:11:-1]) 
print("sample_str[-11:12:-1] : ",sample_str[-11:12:-1])

print("*************************************************************")

print("sample_str[-12:00:-1] : ",sample_str[-12:0:-1]) 
print("sample_str[-12:01:-1] : ",sample_str[-12:1:-1]) 
print("sample_str[-12:02:-1] : ",sample_str[-12:2:-1]) 
print("sample_str[-12:03:-1] : ",sample_str[-12:3:-1]) 
print("sample_str[-12:04:-1] : ",sample_str[-12:4:-1]) 
print("sample_str[-12:05:-1] : ",sample_str[-12:5:-1]) 
print("sample_str[-12:06:-1] : ",sample_str[-12:6:-1]) 
print("sample_str[-12:07:-1] : ",sample_str[-12:7:-1]) 
print("sample_str[-12:08:-1] : ",sample_str[-12:8:-1]) 
print("sample_str[-12:09:-1] : ",sample_str[-12:9:-1]) 
print("sample_str[-12:10:-1] : ",sample_str[-12:10:-1]) 
print("sample_str[-12:11:-1] : ",sample_str[-12:11:-1]) 
print("sample_str[-12:12:-1] : ",sample_str[-12:12:-1])


# In[18]:


#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# P<------>y<------>t<------>h<------>o<----->n<-----> <----->S<----->t<----->r<----->i<----->n<----->g
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

print("********Three Parameter****************************************")

print("********Right to Left - Positive Start and Negative End******")

print("sample_str[0:-00:-1] : ",sample_str[0:-0:-1]) 
print("sample_str[0:-01:-1] : ",sample_str[0:-1:-1]) 
print("sample_str[0:-02:-1] : ",sample_str[0:-2:-1]) 
print("sample_str[0:-03:-1] : ",sample_str[0:-3:-1]) 
print("sample_str[0:-04:-1] : ",sample_str[0:-4:-1]) 
print("sample_str[0:-05:-1] : ",sample_str[0:-5:-1]) 
print("sample_str[0:-06:-1] : ",sample_str[0:-6:-1]) 
print("sample_str[0:-07:-1] : ",sample_str[0:-7:-1]) 
print("sample_str[0:-08:-1] : ",sample_str[0:-8:-1]) 
print("sample_str[0:-09:-1] : ",sample_str[0:-9:-1]) 
print("sample_str[0:-10:-1] : ",sample_str[0:-10:-1]) 
print("sample_str[0:-11:-1] : ",sample_str[0:-11:-1]) 
print("sample_str[0:-12:-1] : ",sample_str[0:-12:-1]) 

print("*************************************************************")

print("sample_str[1:-00:-1] : ",sample_str[1:-0:-1]) 
print("sample_str[1:-01:-1] : ",sample_str[1:-1:-1]) 
print("sample_str[1:-02:-1] : ",sample_str[1:-2:-1]) 
print("sample_str[1:-03:-1] : ",sample_str[1:-3:-1]) 
print("sample_str[1:-04:-1] : ",sample_str[1:-4:-1]) 
print("sample_str[1:-05:-1] : ",sample_str[1:-5:-1]) 
print("sample_str[1:-06:-1] : ",sample_str[1:-6:-1]) 
print("sample_str[1:-07:-1] : ",sample_str[1:-7:-1]) 
print("sample_str[1:-08:-1] : ",sample_str[1:-8:-1]) 
print("sample_str[1:-09:-1] : ",sample_str[1:-9:-1]) 
print("sample_str[1:-10:-1] : ",sample_str[1:-10:-1]) 
print("sample_str[1:-11:-1] : ",sample_str[1:-11:-1]) 
print("sample_str[1:-12:-1] : ",sample_str[1:-12:-1])

print("*************************************************************")

print("sample_str[2:-00:-1] : ",sample_str[2:-0:-1]) 
print("sample_str[2:-01:-1] : ",sample_str[2:-1:-1]) 
print("sample_str[2:-02:-1] : ",sample_str[2:-2:-1]) 
print("sample_str[2:-03:-1] : ",sample_str[2:-3:-1]) 
print("sample_str[2:-04:-1] : ",sample_str[2:-4:-1]) 
print("sample_str[2:-05:-1] : ",sample_str[2:-5:-1]) 
print("sample_str[2:-06:-1] : ",sample_str[2:-6:-1]) 
print("sample_str[2:-07:-1] : ",sample_str[2:-7:-1]) 
print("sample_str[2:-08:-1] : ",sample_str[2:-8:-1]) 
print("sample_str[2:-09:-1] : ",sample_str[2:-9:-1]) 
print("sample_str[2:-10:-1] : ",sample_str[2:-10:-1]) 
print("sample_str[2:-11:-1] : ",sample_str[2:-11:-1]) 
print("sample_str[2:-12:-1] : ",sample_str[2:-12:-1]) 

print("*************************************************************")

print("sample_str[3:-00:-1] : ",sample_str[3:-0:-1]) 
print("sample_str[3:-01:-1] : ",sample_str[3:-1:-1]) 
print("sample_str[3:-02:-1] : ",sample_str[3:-2:-1]) 
print("sample_str[3:-03:-1] : ",sample_str[3:-3:-1]) 
print("sample_str[3:-04:-1] : ",sample_str[3:-4:-1]) 
print("sample_str[3:-05:-1] : ",sample_str[3:-5:-1]) 
print("sample_str[3:-06:-1] : ",sample_str[3:-6:-1]) 
print("sample_str[3:-07:-1] : ",sample_str[3:-7:-1]) 
print("sample_str[3:-08:-1] : ",sample_str[3:-8:-1]) 
print("sample_str[3:-09:-1] : ",sample_str[3:-9:-1]) 
print("sample_str[3:-10:-1] : ",sample_str[3:-10:-1]) 
print("sample_str[3:-11:-1] : ",sample_str[3:-11:-1]) 
print("sample_str[3:-12:-1] : ",sample_str[3:-12:-1]) 

print("*************************************************************")

print("sample_str[4:-00:-1] : ",sample_str[4:-0:-1]) 
print("sample_str[4:-01:-1] : ",sample_str[4:-1:-1]) 
print("sample_str[4:-02:-1] : ",sample_str[4:-2:-1]) 
print("sample_str[4:-03:-1] : ",sample_str[4:-3:-1]) 
print("sample_str[4:-04:-1] : ",sample_str[4:-4:-1]) 
print("sample_str[4:-05:-1] : ",sample_str[4:-5:-1]) 
print("sample_str[4:-06:-1] : ",sample_str[4:-6:-1]) 
print("sample_str[4:-07:-1] : ",sample_str[4:-7:-1]) 
print("sample_str[4:-08:-1] : ",sample_str[4:-8:-1]) 
print("sample_str[4:-09:-1] : ",sample_str[4:-9:-1]) 
print("sample_str[4:-10:-1] : ",sample_str[4:-10:-1]) 
print("sample_str[4:-11:-1] : ",sample_str[4:-11:-1]) 
print("sample_str[4:-12:-1] : ",sample_str[4:-12:-1]) 

print("*************************************************************")

print("sample_str[5:-00:-1] : ",sample_str[5:-0:-1]) 
print("sample_str[5:-01:-1] : ",sample_str[5:-1:-1]) 
print("sample_str[5:-02:-1] : ",sample_str[5:-2:-1]) 
print("sample_str[5:-03:-1] : ",sample_str[5:-3:-1]) 
print("sample_str[5:-04:-1] : ",sample_str[5:-4:-1]) 
print("sample_str[5:-05:-1] : ",sample_str[5:-5:-1]) 
print("sample_str[5:-06:-1] : ",sample_str[5:-6:-1]) 
print("sample_str[5:-07:-1] : ",sample_str[5:-7:-1]) 
print("sample_str[5:-08:-1] : ",sample_str[5:-8:-1]) 
print("sample_str[5:-09:-1] : ",sample_str[5:-9:-1]) 
print("sample_str[5:-10:-1] : ",sample_str[5:-10:-1]) 
print("sample_str[5:-11:-1] : ",sample_str[5:-11:-1]) 
print("sample_str[5:-12:-1] : ",sample_str[5:-12:-1])

print("*************************************************************")

print("sample_str[6:-00:-1] : ",sample_str[6:-0:-1]) 
print("sample_str[6:-01:-1] : ",sample_str[6:-1:-1]) 
print("sample_str[6:-02:-1] : ",sample_str[6:-2:-1]) 
print("sample_str[6:-03:-1] : ",sample_str[6:-3:-1]) 
print("sample_str[6:-04:-1] : ",sample_str[6:-4:-1]) 
print("sample_str[6:-05:-1] : ",sample_str[6:-5:-1]) 
print("sample_str[6:-06:-1] : ",sample_str[6:-6:-1]) 
print("sample_str[6:-07:-1] : ",sample_str[6:-7:-1]) 
print("sample_str[6:-08:-1] : ",sample_str[6:-8:-1]) 
print("sample_str[6:-09:-1] : ",sample_str[6:-9:-1]) 
print("sample_str[6:-10:-1] : ",sample_str[6:-10:-1]) 
print("sample_str[6:-11:-1] : ",sample_str[6:-11:-1]) 
print("sample_str[6:-12:-1] : ",sample_str[6:-12:-1])

print("*************************************************************")

print("sample_str[7:-00:-1] : ",sample_str[7:-0:-1]) 
print("sample_str[7:-01:-1] : ",sample_str[7:-1:-1]) 
print("sample_str[7:-02:-1] : ",sample_str[7:-2:-1]) 
print("sample_str[7:-03:-1] : ",sample_str[7:-3:-1]) 
print("sample_str[7:-04:-1] : ",sample_str[7:-4:-1]) 
print("sample_str[7:-05:-1] : ",sample_str[7:-5:-1]) 
print("sample_str[7:-06:-1] : ",sample_str[7:-6:-1]) 
print("sample_str[7:-07:-1] : ",sample_str[7:-7:-1]) 
print("sample_str[7:-08:-1] : ",sample_str[7:-8:-1]) 
print("sample_str[7:-09:-1] : ",sample_str[7:-9:-1]) 
print("sample_str[7:-10:-1] : ",sample_str[7:-10:-1]) 
print("sample_str[7:-11:-1] : ",sample_str[7:-11:-1]) 
print("sample_str[7:-12:-1] : ",sample_str[7:-12:-1])

print("*************************************************************")

print("sample_str[8:-00:-1] : ",sample_str[8:-0:-1]) 
print("sample_str[8:-01:-1] : ",sample_str[8:-1:-1]) 
print("sample_str[8:-02:-1] : ",sample_str[8:-2:-1]) 
print("sample_str[8:-03:-1] : ",sample_str[8:-3:-1]) 
print("sample_str[8:-04:-1] : ",sample_str[8:-4:-1]) 
print("sample_str[8:-05:-1] : ",sample_str[8:-5:-1]) 
print("sample_str[8:-06:-1] : ",sample_str[8:-6:-1]) 
print("sample_str[8:-07:-1] : ",sample_str[8:-7:-1]) 
print("sample_str[8:-08:-1] : ",sample_str[8:-8:-1]) 
print("sample_str[8:-09:-1] : ",sample_str[8:-9:-1]) 
print("sample_str[8:-10:-1] : ",sample_str[8:-10:-1]) 
print("sample_str[8:-11:-1] : ",sample_str[8:-11:-1]) 
print("sample_str[8:-12:-1] : ",sample_str[8:-12:-1])

print("*************************************************************")

print("sample_str[9:-00:-1] : ",sample_str[9:-0:-1]) 
print("sample_str[9:-01:-1] : ",sample_str[9:-1:-1]) 
print("sample_str[9:-02:-1] : ",sample_str[9:-2:-1]) 
print("sample_str[9:-03:-1] : ",sample_str[9:-3:-1]) 
print("sample_str[9:-04:-1] : ",sample_str[9:-4:-1]) 
print("sample_str[9:-05:-1] : ",sample_str[9:-5:-1]) 
print("sample_str[9:-06:-1] : ",sample_str[9:-6:-1]) 
print("sample_str[9:-07:-1] : ",sample_str[9:-7:-1]) 
print("sample_str[9:-08:-1] : ",sample_str[9:-8:-1]) 
print("sample_str[9:-09:-1] : ",sample_str[9:-9:-1]) 
print("sample_str[9:-10:-1] : ",sample_str[9:-10:-1]) 
print("sample_str[9:-11:-1] : ",sample_str[9:-11:-1]) 
print("sample_str[9:-12:-1] : ",sample_str[9:-12:-1])

print("*************************************************************")

print("sample_str[10:-00:-1] : ",sample_str[10:-0:-1]) 
print("sample_str[10:-01:-1] : ",sample_str[10:-1:-1]) 
print("sample_str[10:-02:-1] : ",sample_str[10:-2:-1]) 
print("sample_str[10:-03:-1] : ",sample_str[10:-3:-1]) 
print("sample_str[10:-04:-1] : ",sample_str[10:-4:-1]) 
print("sample_str[10:-05:-1] : ",sample_str[10:-5:-1]) 
print("sample_str[10:-06:-1] : ",sample_str[10:-6:-1]) 
print("sample_str[10:-07:-1] : ",sample_str[10:-7:-1]) 
print("sample_str[10:-08:-1] : ",sample_str[10:-8:-1]) 
print("sample_str[10:-09:-1] : ",sample_str[10:-9:-1]) 
print("sample_str[10:-10:-1] : ",sample_str[10:-10:-1]) 
print("sample_str[10:-11:-1] : ",sample_str[10:-11:-1]) 
print("sample_str[10:-12:-1] : ",sample_str[10:-12:-1])

print("*************************************************************")

print("sample_str[11:-00:-1] : ",sample_str[11:-0:-1]) 
print("sample_str[11:-01:-1] : ",sample_str[11:-1:-1]) 
print("sample_str[11:-02:-1] : ",sample_str[11:-2:-1]) 
print("sample_str[11:-03:-1] : ",sample_str[11:-3:-1]) 
print("sample_str[11:-04:-1] : ",sample_str[11:-4:-1]) 
print("sample_str[11:-05:-1] : ",sample_str[11:-5:-1]) 
print("sample_str[11:-06:-1] : ",sample_str[11:-6:-1]) 
print("sample_str[11:-07:-1] : ",sample_str[11:-7:-1]) 
print("sample_str[11:-08:-1] : ",sample_str[11:-8:-1]) 
print("sample_str[11:-09:-1] : ",sample_str[11:-9:-1]) 
print("sample_str[11:-10:-1] : ",sample_str[11:-10:-1]) 
print("sample_str[11:-11:-1] : ",sample_str[11:-11:-1]) 
print("sample_str[11:-12:-1] : ",sample_str[11:-12:-1])

print("*************************************************************")

print("sample_str[12:-00:-1] : ",sample_str[12:-0:-1]) 
print("sample_str[12:-01:-1] : ",sample_str[12:-1:-1]) 
print("sample_str[12:-02:-1] : ",sample_str[12:-2:-1]) 
print("sample_str[12:-03:-1] : ",sample_str[12:-3:-1]) 
print("sample_str[12:-04:-1] : ",sample_str[12:-4:-1]) 
print("sample_str[12:-05:-1] : ",sample_str[12:-5:-1]) 
print("sample_str[12:-06:-1] : ",sample_str[12:-6:-1]) 
print("sample_str[12:-07:-1] : ",sample_str[12:-7:-1]) 
print("sample_str[12:-08:-1] : ",sample_str[12:-8:-1]) 
print("sample_str[12:-09:-1] : ",sample_str[12:-9:-1]) 
print("sample_str[12:-10:-1] : ",sample_str[12:-10:-1]) 
print("sample_str[12:-11:-1] : ",sample_str[12:-11:-1]) 
print("sample_str[12:-12:-1] : ",sample_str[12:-12:-1])


# In[19]:


print(len(sample_str))


# In[20]:


#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# H<------>e<------>l<------>l<------>o<----->,<-----> <----->W<----->o<----->r<----->l<----->d<----->!
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

astring="Hello, World!"
print(astring[3:7])


# In[21]:


#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# P<------>y<------>t<------>h<------>o<----->n<-----> <----->S<----->t<----->r<----->i<----->n<----->g
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

sample_str='Python String'
print(sample_str[3:5])    #return a range of character

print(sample_str[7:])    #return all characters from index 7

print(sample_str[:6])    #return all characters before index 6

print(sample_str[6:-5])    #returns from 7 to -4 range

print(len(sample_str[6:-6]))    


# In[23]:


#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# P<------>y<------>t<------>h<------>o<----->n<-----> <----->S<----->t<----->r<----->i<----->n<----->g
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

sample_str='Python String'

print(sample_str[::-1])   #prints the opposite string


# In[22]:


string1 = "Now I am here."

print(string1.center(100))
print(string1.rjust(50))
print(string1.ljust(50))


# In[24]:


a="Hello, World!"

#(-13)<---(-12)<---(-11)<---(-10)<---(-9)<---(-8)<---(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# H<------>e<------>l<------>l<------>o<----->,<-----> <----->W<----->o<----->r<----->l<----->d<----->!
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9------>10----->11----->12

print(a[:7:-2]) # if start is not given and if it is in positive direction then start is assumed as 0, 
                # if in negative direction then the same is assumed as 12


print(a[:7:-3])

print(a[:])

print(a[::])   # the first position tells the begining of the string(0th position) and the second position is 
               # upto the length of the string

print(a[::-1]) # the first position tells the end of the string(len-1 th position) and the second position is 
               # upto the 0th position of the string

#print(a[:5:-1])

#print(a[0:])

#print(a[:])


#print(a[:11:-1])


#print(a[:11:2])


# In[25]:


astring="Hello world!"
print(astring.count("l"))


# In[26]:


print(astring.index("o")) #prints the index of given char


# In[27]:


print(astring.upper())
print(astring.lower())


# In[28]:


print(astring.startswith("Hello"))

print(astring.endswith("asdfasdfasdf"))

print(astring.endswith("ld!"))


# In[29]:


sample="                   Hello, World"

print(sample)
print(sample.strip()) # removes white space from start and end


# In[30]:


test=('This is a test')
print(test)
print(test.replace('is','eez'))


# In[31]:


question="What is the air speed velocity of an unlaiden swallow?"
print(question)

question2=question.replace("swallow","European swallow")
print(question2)

question3=question.replace("swallow","African swallow")
print(question3)


# In[32]:


#(-10)<---(-9)<----(-8)<----(-7)<---(-6)<---(-5)<---(-4)<---(-3)<---(-2)<---(-1)
# p<------>y<------>t<------>h<------>o<----->n<----->a<----->b<----->c<----->d
# 0------->1------->2------->3------->4------>5------>6------>7------>8------>9

a="pythonabcd"

print(a[0:9])
print(a[0:10])
print(a[2:8])
print(a[0:20])
print(a[:0:-1])
print(a[:2:-2])
print(a[:2:-3])


# In[33]:


string1="one, one, one, one, one, one"

print("Original:", string1)
print('Replaced "one" with "two":',string1.replace("one","two"))
print("Replaced 3 maximum:", string1.replace("one","two",3))
print("After Change:", string1)


# In[34]:


str="hello people"

str2=str.capitalize()

print("Old Value:",str)

print("New Value:",str2)


# In[35]:


# What of the first character is already a capital letter
str="Hello people"

str2=str.capitalize()

print("Old Value:",str)

print("New Value:",str2)


# In[36]:


str1="#hello to all"

str2="1-hello to all"

print(str1.capitalize())
print(str2.capitalize())


# In[37]:


print("alpha" < "beta")


# In[38]:


str1='abc'
str2='lmn'
str3='xyz'
print(str1 < str2)
print(str2 != str3)
print(str1 < str3 and str2 == 'xyz')


# In[39]:


ch = 'b'

print(ord(ch)) # returns ASCII Code

print(chr(97)) # returns character represent by ASCII Code

print(ord('A')) 


# In[40]:


print(len("hello")) 

print(max("abc")) # returns character having highest ASCII value

print(min("abc")) # returns character having lowest ASCII value


# In[41]:


# Python compares string using ASCII value of the characters.
print("tim" == "tie")
print("free" != "freedom")
print("arrow" > "aron")
print("right" >= "left")
print("teeth" < "tee")
print("yellow" <= "fellow")
print("abc" > "")


# In[36]:


str1="welcome to python"

print("Whether str1 is alphanumeric :",str1.isalnum())
print("Whether the word \"Welcome\" is alphabetic :","Welcome".isalpha())
print("Whether the word \"2012\" is alphabetic :","2012".isdigit())

# Checks whether it is a valid identifier, Not valid if it contains space,special symbol or if it starts with number

print("Whether the word \" p\" is an identifier :"," p".isidentifier())
print("Whether the word \"pyt hon\" is an identifier :","pyt hon".isidentifier())
print("Whether the word \"python \" is an identifier :","python ".isidentifier())
print("Whether the word \"srinivasan \" is an identifier :","srinivasan ".isidentifier())

print("Whether the word \"s$\" is an identifier :","s$".isidentifier()) 
print("Whether the word \"$s\" is an identifier :","$s".isidentifier()) 
print("Whether the word \"srini$\" is an identifier :","srini$".isidentifier())
print("Whether the word \"s$rini\" is an identifier :","s$rini".isidentifier()) 

print("Whether the word \"1a\" is an identifier :","1a".isidentifier())
print("Whether the word \"a1\" is an identifier :","a1".isidentifier())
print("Whether the word \"a2134\" is an identifier :","a2134".isidentifier())
print("Whether the word \"1234a\" is an identifier :","1234a".isidentifier())

print("Whether the word \"Python\" is an identifier :","Python".isidentifier())

# Checks only the first character
print("Whether the first character in the string \"welcome to python\" is an lowercase :",str1.islower())  

# Checks all the characters
print("Whether all the characters in the word \"WELCOME\" is in uppercase :","WELCOME".isupper())
print("Whether there is space in the word ' \t' :","  \t".isspace())
print("Whether there is space in the word '' :","".isspace())
print("Whether there is space in the word ' ':"," ".isspace())


# In[19]:



# Python code to illustrate the working of isidentifier() 
  
# String with spaces 
string = "Geeks for Geeks"
print(string.isidentifier()) 
  
# A Perfect identifier 
string = "GeeksforGeeks"
print(string.isidentifier()) 
  
# Empty string 
string = "" 
print(string.isidentifier()) 
  
# Alphanumerical string 
string = "Geeks0for0Geeks"
print(string.isidentifier()) 
  
# Beginning with an integer 
string = "54Geeks0for0Geeks"
print(string.isidentifier()) 


# In[43]:


str1="welcome to python"

print(str1.endswith("thon"))
print(str1.startswith("good"))
print(str1.find("come"))
print(str1.find("become"))
print(str1.count("o"))


# In[44]:


txt="Hello, welcome to my world"

x=txt.find("e",5,10)

print(x)


# In[45]:


s="string in python"

s1 = s.capitalize()
print(s1)

s2 = s.title()
print(s2)


s="This Is Test"

print(s)

s3=s.lower()
print(s3)

s4=s.upper()
print(s4)

s5=s.swapcase()  #Lowercase convereted  to uppercase and upper case to lower case
print(s5)

s6=s.replace("Is", "Was")
print(s6)


# In[46]:


#concating the python string

print("Hello, " + "world!")
x="Hello, "
y="world!"
print(x+y)


# In[47]:


word1= "A"
word2= "few"
word3= "good"
word4= "words"
wordList= ["A", "few", "more", "good", "words"]

print("Words:" + word1 + word2 + word3 + word4)
print("List: " + ' '.join(wordList))


# In[49]:


print("List: " + (wordList))


# In[22]:


myTuple = (" John "," Peter ", " Vicky ") # The join happens inbetween, not on the end and not on the start
mySeperator = "TEST"

x=mySeperator.join(myTuple)

print(x)
print(type(x))


# In[50]:


seq = ('ab','bc','cd')
str = '='
print(str.join(seq))


# In[21]:


txt="Welcome to the Jungle"  # By default it splits by space
x=txt.split()
print(x)
print(type(x))


# In[52]:


txt= "hello, my name is Peter, I am 26 years old"

x=txt.split(",")

print(x)


# In[53]:


print('1+2+3+4+5'.split('+'))
print('/usr/bin/env'.split('/'))
print('Using the default'.split())


# In[54]:


sentence = "A Simple Sentence"

print(sentence.split())


# In[55]:


entry = "Name:James:Occupation:Software Engineer"
print(entry.split(':'))


# In[56]:


txt = "50"

x = txt.zfill(10) #Fill the string with zeros until it is 10 characters long

print(x)


# In[57]:


a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))

print(b.zfill(10))

print(c.zfill(20))


# In[58]:


var1 = 'Python'
print(var1*3) #repeatition


# In[59]:


var1='Python'
print('n' in var1) #in -> to check the membership


# In[60]:


var1= 'Python'
print('N' not in var1)


# In[61]:


var1= 'Python'
print('n' not in var1)


# In[62]:


var= '   This is a good example    '
print(var)
print(var.lstrip())


# In[63]:


var= '   This is a good example    '
print(var)
print(var.rstrip())


# In[64]:


var= '   This is a good example    '
print(var)
print(var.strip())


# In[65]:


s1= "Welcome"
print("come" in s1)
print("come" not in s1)


# In[38]:


str="     Sr i n i vasan"
print(str)
len(str)
str.strip()


# In[39]:


str="SRINIVASAN"
str.lower()


# In[40]:


str.upper()


# In[41]:


str="Srinivasan, is a good person"
str.split(",")


# In[42]:


str="Srinivasan, is a good person"
str.index(",")


# In[43]:


str="Srinivasan, is a good person"
str.count(",")


# In[44]:


str="Srinivasan, is a good person"
str.replace("n","a")


# In[45]:


str="Srinivasan, is a good person"
str.startswith("Sri")


# In[46]:


str="Srinivasan, is a good person"
str.endswith("rson")


# In[52]:


str="Srinivasan, is a good person"
str.center(100)


# In[53]:


str="Srinivasan, is a good person"
str.rjust(100)


# In[54]:


str="Srinivasan, is a good person"
str.ljust(100)


# In[55]:


str="srinivasan, is a good person"
str.capitalize()


# In[57]:


print(ord("S"))


# In[59]:


print(chr(83))


# In[61]:


str="Srinivasan"

max(str)


# In[65]:


str="Srinivasan"

min(str)


# In[66]:


"a"=="A"


# In[68]:


str="Srinivasan"

str.isalpha()


# In[71]:


str="Srini123vasan"

str.isalnum()


# In[73]:


str="123"

str.isdigit()


# In[74]:


str="Srinivasan"
str.isidentifier()


# In[75]:


str="srinivasan"
str.islower()


# In[76]:


str="SRINI"
str.isupper()


# In[77]:


str=" "
str.isspace()


# In[78]:


str="srinivasan"
str.find("i")


# In[80]:


str="srinivasan"
str.find("i",4,10)


# In[81]:


str="srini is a good person"
str.title()


# In[82]:


str="SrInIvAsAn"
str.swapcase()


# In[84]:


str1="srini"
str2="vasan"

str3=str1+str2

print(str3)


# In[85]:


str="srini"
str.zfill(10)


# In[87]:


str="srinivasan"

"s" in str


# In[89]:


str="srinivasan"

"x" not in str


# In[96]:


str="     Srinivasan"
print(len(str))
str1=str.lstrip()
print(len(str1))


# In[95]:


str="Srinivasan     "
#print(len(str))
print(str.rstrip())
#print(len(str))


# In[98]:


str="Python"
print(str*3)


# In[11]:


print(ord('a'))


# In[ ]:




