#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''

int()
float()
bool()
complex()
str()

'''


# In[1]:


a=10.7263487637
print(a)
b=int(a)
print(b)


# In[2]:


a=True
b=int(a)
print(a)
print(b)


# In[3]:


a=10
b=str(a)
print(a)
print(type(a))
print(b)
print(type(b))      


# In[4]:


a="10"
b=int(a)
print(a)
print(type(a))
print(b)
print(type(b))  


# In[5]:


a="abc"
b=int(a)
print(a)
print(type(a))
print(b)
print(type(b))  


# In[6]:


a=10+10j
b=int(a)
print(a)
print(type(a))
print(b)
print(type(b))  


# In[7]:


a=10+10j
b=float(a)
print(a)
print(type(a))
print(b)
print(type(b))  


# In[3]:


a=10+10j
b=bool(a)
print(a)
print(type(a))
print(b)
print(type(b))  


# In[9]:


a=True
b=str(a)
print(a)
print(type(a))
print(b)
print(type(b))  


# In[10]:


a=10.2634723
b=str(a)
print(a)
print(type(a))
print(b)
print(type(b))  


# In[11]:


a=10+10j
b=str(a)
print(a)
print(type(a))
print(b)
print(type(b))


# In[16]:


a=10
b=10
c=10
print(id(a))
print(id(b))
print(id(c))

print("*********")

b=20
print(id(a))
print(id(b))
print(id(c))


# In[17]:


print(a is c)   # compares the address


# In[19]:


print(a is b)   # compares the address


# In[18]:


print(a == c)   # compares the values


# In[20]:


print(a == b)   # compares the values


# In[21]:


# in case of float and complex always new object created
# same object for same value is assigned only for int, bool and string type only

a=10.64732647
b=10.64732647
print(id(a))
print(id(b))


# In[4]:


a=10+10j
b=10+10j
print(id(a))
print(id(b))


# In[ ]:


'''

#9       8         7         6         5         4         3         2         1
#2power8 2power7   2power6   2power5   2power4   2power3   2power2   2power1   2power0
#256     128       64        32        16        8         4         2         1


only till 8 bits(0 to 256) no only same object (Why this range ???) (at start only python creates object 
in range of 0 to 256)

this is most common range so created while starting of python interpreter only

int - 0 to 255 same object assigned for same contect(interpreter creates the int objects 
while starting of interpreter)

string - always same object is assigned for same content(interpreter checks if string contect is available 
or not, if available then assign to that object but no string object is created while start of python)

bool - always same object is assigned for same content

complex - every time new object created for same content also(so many floating values cant 
predict the common values)

float - every time new object created for same content also(so many floating values cant 
predict the common values)
'''


# In[5]:


a=256
b=256
print(id(a))
print(id(b))


# In[21]:


c=257
d=257
print(id(c))
print(id(d))


# In[16]:


a="abc"
b="abc"
print(id(a))
print(id(b))


# In[17]:


'''

Garbage Collection

responsibility of creating objects and destroy objects in old language (C, C++ -> out of memory problem)

responsibility of creating objects and destroy objects in new language (Java, Python -> is handled by itself)

when an object is eligible for garbage collection?? -> if no reference variable

enable and disable the GC ?

'''


# In[26]:


import gc


# In[34]:


dir(gc)


# In[29]:


print(gc.isenabled())


# In[32]:


gc.disable()


# In[33]:


print(gc.isenabled())


# In[35]:


gc.enable()


# In[36]:


print(gc.isenabled())


# In[23]:


# date, time and datetime calculator

import time

    # prints the numer of seconds since 12 AM, 1st Janusry 1970 (epoch format)
    
print(time.time())


# In[24]:


print(time.localtime(time.time()))


# In[7]:


# date, time and datetime calculator

import time

    # prints the numer of seconds since 12 AM, 1st Janusry 1970 (epoch format)
    
print(now())


# In[25]:


print(time.asctime(time.localtime(time.time())))


# In[2]:


import time
print(time.asctime(time.localtime()))


# In[3]:


import time
print(time.asctime(time.time()))


# In[42]:


help(time.asctime)


# In[29]:


import time
for i in range(0,20):
    print(i)
    time.sleep(10)


# In[35]:


dir(datetime)


# In[30]:


import datetime
print(datetime.datetime.now())


# In[10]:


import datetime
print(datetime.datetime(2019,5,22)) 


# In[11]:


import datetime
print(datetime.datetime(2019,5,22,14,15,10)) 


# In[31]:


import datetime
print(datetime.datetime.today()) 


# In[26]:


import datetime
print("Date:",datetime.date.fromtimestamp(1326244364))  


# In[25]:


import datetime

today = datetime.date.today()

print("Current year:",today.year)
print("Current year:",today.month)
print("Current year:",today.day)


# In[22]:


import datetime

tm = datetime.time(12,36,45)

print("hour:",tm.hour)
print("minute:",tm.minute)
print("second:",tm.second)
print("microsecond:",tm.microsecond)


# In[40]:


#from datetime import date
import datetime

dt = datetime.datetime(2017,11,28,23,55,59,342380)

print("year:",dt.year)
print("month:",dt.month)
print("date:",dt.date)
print("hour:",dt.hour)
print("minute:",dt.minute)
print("timestamp:",dt.timestamp())


# In[46]:


'''

%Y - year
%m - month
%d - day
%H - hour
%M - minutes
%S - second

'''

import datetime

# current date and time
now1 = datetime.datetime.now()

t=now1.strftime("%H:%M:%S")
print("time:",t)

s1=now1.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted Date:",s1)


# In[56]:


import datetime
import pytz

local = datetime.datetime.now()
print("Local Time:",local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
NY_date = datetime.datetime.now(tz_NY)
print("New York date:", NY_date.strftime("%m/%d/%Y, %H:%M:%S"))
                                         
tz_London = pytz.timezone('Europe/London')
London_date= datetime.datetime.now(tz_London)
print("London Date:", London_date.strftime("%m/%d/%Y, %H:%M:%S"))


# In[59]:


import calendar
cal = calendar.month(2020,10)
print(cal)


# In[60]:


import calendar
calendar.prcal(2020)


# In[34]:


print(calendar.isleap(2019))
print(calendar.isleap(2016))
print(calendar.isleap(2019))
print(calendar.isleap(2018))
print(calendar.isleap(2017))
print(calendar.isleap(2016))
print(calendar.isleap(2015))
print(calendar.isleap(2014))
print(calendar.isleap(2013))
print(calendar.isleap(2012))
print(calendar.isleap(2011))
print(calendar.isleap(2010))
print(calendar.isleap(2009))
print(calendar.isleap(2008))
print(calendar.isleap(2007))
print(calendar.isleap(2006))
print(calendar.isleap(2005))
print(calendar.isleap(2004))
print(calendar.isleap(2003))
print(calendar.isleap(2002))
print(calendar.isleap(2001))
print(calendar.isleap(2000))


# In[33]:


print(calendar.leapdays(2000,2019))#this actually gives the number of leap years inbetween the given range


# In[61]:


print(calendar.weekheader(2)) # fontsize of the weekheader
print(calendar.weekheader(3))
print(calendar.weekheader(4))


# In[41]:


print(calendar.weekday(2019,10,4))  # 0 to 6 0=mon, 6=sun


# In[62]:


print(calendar.monthrange(2020,10))  # format (what will be firstdate of that month ,no of days)


# In[7]:


import calendar

day = int(input("Enter the date of your birth?"))
month = int(input("Enter the month of your birth?"))
year = int(input("Enter the year of your birth?"))

birthday = calendar.weekday(year,month,day)

if birthday == 0:
    print("MONDAY")
elif birthday == 1:
    print("TUESDAY")
elif birthday == 2:
    print("WEDNESDAY")
elif birthday == 3:
    print("THURSDAY")
elif birthday == 4:
    print("FRIDAY")
elif birthday == 5:
    print("SATURDAY")
elif birthday == 6:
    print("SUNDAY")


# In[58]:


import time

print(time.localtime(time.time()))


# In[55]:


import datetime
import pytz

US_TZ = pytz.timezone('Australia/Brisbane')
print(datetime.datetime.now(US_TZ))
print(datetime.datetime.now('12'))
print(datetime.date.today())


# In[ ]:




