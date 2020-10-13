#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''

1.What is function and its use??
2.def keyword ??
3.syntax - def function_name():
                //code of the function
               
'''


# In[2]:


def wish():
    print("have a good day")


# In[3]:


wish()


# In[4]:


def test1():
    print("i am test1 function")
def test2():
    print("i am test2 function")
def test3():
    print("i am test3 function")
def test4():
    print("i am test4 function")
    
test1()
test2()
test3()
test4()  


# In[5]:


def test1():
    print("i am test1 function")
    
def test2():
    test1()
    print("i am test2 function")
    
test2()


# In[1]:


def test1():
    print("i am test1 function")
def test2():
    print("i am test2 function")
def test3():
    print("i am test3 function")
def test4():
    print("i am test4 function")
    
def callfunction():
    print("i am call function")
    test1()
    test2()
    test3()
    test4()
    
callfunction()


# In[9]:


def test1():
    print("i am test1 function")
    test2()
    
def test2():
    print("i am test2 function")
    test3()
    
def test3():
    print("i am test3 function")
    test4()
    
def test4():
    print("i am test4 function")
    
def callfunction():
    print("i am call function")
    test1()
    
callfunction()


# In[2]:


#function with inputs/parameters/arguments

def wish(towhom):
    print("Hi",towhom,"have a good day")
    
wish("Team")


# In[11]:


#function with inputs/parameters/arguments

def wish(towhom):
    print("Hi",towhom,"have a good day")
    
name = input("Enter name to whom you want to wish:")
    
wish(name)


# In[13]:


def addno(no1,no2):
    return no1+no2

no1 = int(input("Enter no1:"))
no2 = int(input("Enter no2:"))

print("Add is:",addno(no1,no2))


# In[14]:


def test1():
    def test2():
        print("test2 is called")
        
    print("test1 is called")
    test2()
    
test1()


# In[1]:


def employeeDetails(id,name,age,email):
    return(id,name,age,email)

id = int(input("Enter id:"))

name = input("Enter name:")

age = int(input("Enter age:"))

email = input("Enter email:")

print("Details are:=",employeeDetails(id,name,age,email))


# def BaicCalc(no1,no2):
#     sum=no1+no2
#     sub=no1-no2
#     mul=no1*no2
#     div=no1/no2
#     return sum,sub,mul,div
# no1 = int(input("Enter no1:"))
# no2 = int(input("Enter no2:"))
# 
# print("Results are: =", BasicCalc(no1,no2))

# In[4]:


def BasicCalc(no1,no2): 
    sum=no1+no2 
    sub=no1-no2 
    mul=no1*no2 
    div=no1/no2 
    return sum,sub,mul,div 

no1 = int(input("Enter no1:")) 
no2 = int(input("Enter no2:"))

print("Results are: =", BasicCalc(no1,no2))


# In[23]:


def getdomains(*domainnames):
    print("type of passed argument is:",type(domainnames))
    
    for name in domainnames:
        print(name)
        
getdomains("ASDC","MIG","Finance","Insurance")
print(".............")
getdomains("ASDC","MIG")
getdomains("ASDC",10)


# In[24]:


def printinfo(arg1,*values):
    print("Output is:")
    print(arg1)
    print(".........")
    
    for var in values:
        print(var)
        
printinfo( 10)
printinfo(70,60,50)
printinfo(70,"abc","xyz",True)


# In[25]:


def sum(*n):
    result=0
    for x in n:
        result=result+x
    print("Result is:",result)
    
sum()
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)


# In[27]:


def sum(name,*n):
    result=0
    for x in n:
        result=result+x
    print("name is:",name,",result is:",result)
    
sum("ram")
sum("raj",10,20)
sum("Rajesh",10,20,30)
sum("Vikas",10,20,30,40)


# In[30]:


def sum(*n,name):    #here name is a keyword argument
    result=0
    for x in n:
        result=result+x
    print("name is:",name,",result is:",result)
    
sum(name="ram")
sum(10,20,name="raj")
sum(10,20,30,name="Ravjesh")
sum(10,20,30,40,name="Vikas")
sum(10,20,30,40,name="Vikas")


# In[39]:


def greet(name,msg):
    print("Hello",name,",",msg)
    print("Hello",name+", "+msg)
    
greet("Ram","Good Morning!")


# In[40]:


def greet(name,msg="Good morning!"):
    print("Hello",name+", ",msg)
    
greet("Ram")
greet("Rajesh","Good Evening")


# In[41]:


'''

personDetails(name="abc",marks=100,age=30,email="abc@gmail.com")
personDetails(name="xyz",email="abc@gmail.com",GF="Sunny",Address="Bangalore")
personDetails(name="pqr",Address="Banglore",weight=90,wife1="Lata",Wife2="Radhika",Wife3="Rama")

'''


# In[5]:


def personDetails(** kwargs):
    print(type(kwargs))
    
personDetails(name="abc",marks=100,age=30,email="abc@gmail.com")
personDetails(name="xyz",email="abc@gmail.com",GF="Sunny",Address="Bangalore")
personDetails(name="pqr",Address="Banglore",weight=90,wife1="Lata",Wife2="Radhika",Wife3="Rama")


# In[46]:


def personDetails(** kwargs):
    print("*******************")
    print("all the person details are:")
    for k,v in kwargs.items():
        print(k,"----------",v)
        
personDetails(name="abc",marks=100,age=30,email="abc@gmail.com")
personDetails(name="xyz",email="abc@gmail.com",GF="Sunny",Address="Bangalore")
personDetails(name="pqr",Address="Banglore",weight=90,wife1="Lata",Wife2="Radhika",Wife3="Rama")


# In[61]:


import math 

def pi(x,y): 
    'Calculates the pi value.' 
    return x/y

#print(pi.__doc__)

help(math.pi)

help(pi)

y=pi(22,7) 
print(y)


# In[62]:


# Retun keyword
def inc(x):
    return x+1

a=10
b=inc(a)
print(b)


# In[63]:


# retun multiple values
def nocube(x):
    return x**2, x**3

a,b = nocube(3)
print(a)
print(b)


# In[65]:


# Local and Global variables

def test1():
    var1=10
    print("i am in test1 function:",var1)
    
def test2():
    var2=20
    print("i am in test2 function:",var2)
    
def test3():
    var3=30
    print("i am in test3 function:",var3)
    
def test4():
    var4=40
    print("i am in test4 function:",var4)
    
test1()
test2()
test3()
test4()


# In[66]:


def test1():
    var1=10
    print("i am in test1 function:",var1)
    print("here is variable:",var2)
    
def test2():
    var2=20
    print("i am in test2 function:",var2)
    
def test3():
    var3=30
    print("i am in test3 function:",var3)
    
def test4():
    var4=40
    print("i am in test4 function:",var4)
    
test1()
test2()
test3()
test4()


# In[67]:


def test1():
    var1=10
    print("i am in test1 function:",var1)    
    
def test2():
    var2=20
    print("i am in test2 function:",var2)
    
def test3():
    var3=30
    print("i am in test3 function:",var3)
    
def test4():
    var4=40
    print("i am in test4 function:",var4)
    print("here is variable:",var2)
    
test1()
test2()
test3()
test4()


# In[69]:


gvar=100

def test1():
    var1=10
    print("i am in test1 function:",var1)   
    print("value of global variable:",gvar) 
    
def test2():
    var2=20
    print("i am in test2 function:",var2)
        
def test3():
    var3=30
    print("i am in test3 function:",var3)
    print("value of global variable:",gvar)
    
gvar2=200
    
def test4():
    var4=40
    print("i am in test4 function:",var4)
    print("value of global variable:",gvar2)
    
test1()
test2()
test3()
test4()


# In[ ]:




