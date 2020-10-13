#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''

Class definition

Object definition

Reference definition


1 class multiple objects
1 object one or more multiple references

Syntax - class ClassName
                #code inside the class

'''


# In[ ]:


'''

Class vs Object vs Instance

with 9 comments

In OO Programming, we often hear of terms like “Class”, “Object” and “Instance”; 
but what actually is a Class / Object / Instance?

In short, 

An object is a software bundle of related state and behavior. 

A class is a blueprint or prototype from which objects are created. 

An instance is a single and unique unit of a class.

Example, 
we have a blueprint (class) represents student (object) with fields like name, age, course (class member). 
And we have 2 students here, Foo and Bob. So, Foo and Bob is 2 different instances of the class 
(Student class) that represent object (Student people).

Let me go into details…

Object
Real world objects shares 2 main characteristics, state and behavior. 
Human have state (name, age) and behavior (running, sleeping). 
Car have state (current speed, current gear) and behavior (applying brake, changing gear). 
Software objects are conceptually similar to real-world objects: they too consist of state and related behavior. An object stores its state in fields and exposes its behavior through methods.

Class
Class is a “template” / “blueprint” that is used to create objects. 
Basically, a class will consists of field, static field, method, static method and constructor. 
Field is used to hold the state of the class (eg: name of Student object). 
Method is used to represent the behavior of the class (eg: how a Student object going to stand-up). 
Constructor is used to create a new Instance of the Class.

Instance
An instance is a unique copy of a Class that representing an Object. 
When a new instance of a class is created, the JVM will allocate a room of memory for that class instance.


'''


# In[ ]:


# https://www.youtube.com/watch?v=hLC6GL_YBGM

# https://www.w3schools.com/python/python_classes.asp

# https://www.programiz.com/article/python-self-why

# To understand the meaning of classes we have to understand the __init__() function, which is a constructor

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:

# Note : The __init__() function is called automatically every time the class is being used to 
# create a new object.

# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Note: The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

# It does not have to be named self , you can call it whatever you like, 
# but it has to be the first parameter of any function in the class.


# In[3]:


'''Please dont edit this example, As this example explains the self parameter clearly'''

class PersonDetails:
    def __init__(self, ssid, name):    # here the self parameter is srini
        self.ssid1=ssid                # here the ssid1 is the instance variable 
        self.name1=name                # here the name1 is the instance variable 
        
    def tellDetails(self, vasu1):       # here the self parameter is vasu
        print("vasu1",vasu1)            # here the method parameter is vasu1 is a pass by parameter
        print("my ssid is:",self.ssid1) # here the ssid1 is the instance variable
        print("my name is:",self.name1) # here the name1 is the instance variable
        
p1=PersonDetails(12345,"Raj")           # p1 is the object of the class PersonDetails here

p2=PersonDetails(45678,"Ram")           # p2 is the object of the class PersonDetails here

print(p1.ssid1)                         # printing the variable ssid of the object p1
print(p1.name1)                         # printing the variable name of the object p1

print("------------")

print(p2.ssid1)                         # printing the variable ssid of the object p2
print(p2.name1)                         # printing the variable name of the object p2

print("--------------")

p1.tellDetails(10)                      # same as PersonDetails.tellDetails(p1,10)
p2.tellDetails(10)                      # same as PersonDetails.tellDetails(p2,10) 

print("--------------")

PersonDetails.tellDetails(p1,10)        # same as p1.tellDetails(10)
PersonDetails.tellDetails(p2,10)        # same as p2.tellDetails(10)

print("--------------")

 
'''

p1.tellDetails(10) is same as PersonDetails.tellDetails(p1,10)

As per the above statement the self parameter is always required to be first paramenter in the methods 
of the class as internally the stmt " p1.tellDetails(10)" will be always converted as 
"PersonDetails.tellDetails(p1,10)" so to match the internal conversion we need to insert the self parameter
only through which we can identify the object reference p1.

So the syntax becomes as,

<Class Name>.<Method Name>(<Object name>, <argument for the method>)

which is same as,

<Object name>.<Method Name>(<arguement for the method>)

so hence the method definition should also be maintained as,

<Method Name>(<self parameter>, <arguement for the method>)

'''


# In[3]:


# Example 1 - A Class with the __init__ constructor and a method, no class variable

class PersonDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def __init__(self, ssid, name):   # here the self parameter is self
        self.ssid=ssid                # here the ssid is the instance variable
        self.name=name                # here the name is the instance variable
        
    def tellDetails(self):            # here the self parameter is self
        print("my ssid is:",self.ssid)
        print("my name is:",self.name)
        
p1=PersonDetails(12345,"Raj")  #p1 is the object of the class PersonDetails here
p2=PersonDetails(45678,"Ram")  #p2 is the object of the class PersonDetails here

print(p1.ssid)  #printing the variable ssid of the object p1
print(p1.name)  #printing the variable name of the object p1

print("------------")

print(p2.ssid)  #printing the variable ssid of the object p2
print(p2.name)  #printing the variable name of the object p2


# In[85]:


# Example 2 - A Class without the __init__ constructor, but with a method and two class variables

class PersonDetails:
    
    ssid=12345   # field 1, variable declared as member of class, this is a class variable, 
                 # can be used in all methods of the class
    name="Raj"   # field 2, variable declared as member of class, this is a class variable, 
                 # can be used in all methods of the class
  
    def tellDetails(self2):            
        print("my ssid is:",self2.ssid)
        print("my name is:",self2.name)
        
p1=PersonDetails()  #p1 is the object of the class PersonDetails here

print(p1.ssid)  #printing the variable ssid of the object p1
print(p1.name)  #printing the variable name of the object p1

print("------------")

p1.tellDetails() #same as PersonDetails.tellDetails(p1)

print("------------")

PersonDetails.tellDetails(p1) #same as p1.tellDetails()


# In[110]:


# Example 3 - A Class without the __init__ constructor, but with a method and variable within it 
# and no class variables

# Here val1 is a local variable inside the method tellDetails() which is defined as a pass by parameter method

class PersonDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def tellDetails(self,val1):            # here the self parameter is self
        print("my val1 is:",val1)
        
p1=PersonDetails()  #p1 is the object of the class PersonDetails here
p2=PersonDetails()  #p2 is the object of the class PersonDetails here

p1.tellDetails(10)

print("------------")

p2.tellDetails(20)


# In[112]:


# Example 4 - A Class without the __init__ constructor, but with a method within it and no class variables

# Here val1 is a local variable inside the method tellDetails()

class PersonDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def tellDetails(self):            # here the self parameter is self
        val1=10
        print("my val1 is:",val1)
        
p1=PersonDetails()  #p1 is the object of the class PersonDetails here
p2=PersonDetails()  #p2 is the object of the class PersonDetails here

p1.tellDetails()

print("------------")

p2.tellDetails()


# In[4]:


print(id(p1))
print(id(p2))


# In[5]:


print(type(p1))
print(type(p2))


# In[6]:


# Normal Example - where one constructor __init__ and a method tellCompanyInfo is made in the 
# class CompanyDetails

class CompanyDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def __init__(self,name, address, no_of_emp, no_of_dept, company_description, no_of_product):
        self.name=name
        self.address=address
        self.no_of_emp=no_of_emp
        self.no_of_dept=no_of_dept
        self.company_description=company_description
        self.no_of_product=no_of_product
    
    def tellCompanyInfo(self):
        print("**********************")
        print("company name is",self.name)
        print("company address is",self.address)
        print("company no of employees are",self.no_of_emp)
        print("company no of departments are",self.no_of_dept)
        print("company description is",self.company_description)
        print("company no of products are",self.no_of_product)
        
c1=CompanyDetails("Infosys","E-City",2000,6,"Infosys Company",10) #c1 is the object of the class CompanyDetails here
c2=CompanyDetails("CGI","Whitefield",5000,8,"CGI Company",15) #c2 is the object of the class CompanyDetails here
c3=CompanyDetails("TCS","MG_Road",10000,10,"TCS Company",20) #c3 is the object of the class CompanyDetails here

c1.tellCompanyInfo()
c2.tellCompanyInfo()
c3.tellCompanyInfo()      


# In[7]:


# doc string

CompanyDetails.__doc__


# In[8]:


# Normal Example - where only one constructor __init__ is made in the class Demo

class Demo:
    def __init__(self):
        print("inside of class",id(self)) #both ids refer to same object

      
d=Demo()  #d is the object of the class Demo here
print("outside of class - d object",id(d)) #both ids refer to same object
print("*****************")
d1=Demo() #d1 is the object of the class Demo here 
print("outside of class - d1 object",id(d1)) #both ids refer to same object       


# In[14]:


# Normal Example - where one constructor __init__ and a method tellCompanyInfo is made in the class 
# CompanyDetails, also we have a local variable name inside the method tellCompanyInfo 

# the first argument to the constructor(__init(self)) self must be there

# python virtual machine is responsible to provide the self for constructor and methods in the class

class CompanyDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def __init__(self,name, address, no_of_emp, no_of_dept, company_description, no_of_product):
        self.name=name
        self.address=address
        self.no_of_emp=no_of_emp
        self.no_of_dept=no_of_dept
        self.company_description=company_description
        self.no_of_product=no_of_product
    
    def tellCompanyInfo(self):
        print("**********************")
        
        '''
        in case if i use local variable and dont use the self variable then it takes local variable
        to differ local variable and current object variable we use self
        
        '''
        
        name="cisco"
        print("Local company name is:",name)
        
        print("company name is",self.name)
        print("company address is",self.address)
        print("company no of employees are",self.no_of_emp)
        print("company no of departments are",self.no_of_dept)
        print("company description is",self.company_description)
        print("company no of products are",self.no_of_product)
        
c1=CompanyDetails("Infosys","E-City",2000,6,"Infosys Company",10) #c1 is the object of the class CompanyDetails here
c2=CompanyDetails("CGI","Whitefield",5000,8,"CGI Company",15) #c2 is the object of the class CompanyDetails here
c3=CompanyDetails("TCS","MG_Road",10000,10,"TCS Company",20) #c3 is the object of the class CompanyDetails here

c1.tellCompanyInfo()
c2.tellCompanyInfo()
c3.tellCompanyInfo()

CompanyDetails.__doc__


# In[11]:


# Normal Example - where one constructor __init__ and a method tellCompanyInfo is made in the class 
# CompanyDetails, also we have a local variable name inside the method tellCompanyInfo 

# the self variable can differ by name, we can use any name instead of self 

class CompanyDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def __init__(self1, name, address, no_of_emp, no_of_dept, company_description, no_of_product):
        self1.name=name
        self1.address=address
        self1.no_of_emp=no_of_emp
        self1.no_of_dept=no_of_dept
        self1.company_description=company_description
        self1.no_of_product=no_of_product
    
    def tellCompanyInfo(self2):
        print("**********************")
        
        '''
        in case if i use local variable and dont use the self variable then it takes local variable
        to differ local variable and current object variable we use self
        
        '''
        
        name="cisco"
        print("Local company name is:",name)
        
        print("company name is",self2.name)
        print("company address is",self2.address)
        print("company no of employees are",self2.no_of_emp)
        print("company no of departments are",self2.no_of_dept)
        print("company description is",self2.company_description)
        print("company no of products are",self2.no_of_product)
        
c1=CompanyDetails("Infosys","E-City",2000,6,"Infosys Company",10) #c1 is the object of the class CompanyDetails here
c2=CompanyDetails("CGI","Whitefield",5000,8,"CGI Company",15) #c2 is the object of the class CompanyDetails here
c3=CompanyDetails("TCS","MG_Road",10000,10,"TCS Company",20) #c3 is the object of the class CompanyDetails here

c1.tellCompanyInfo()
c2.tellCompanyInfo()
c3.tellCompanyInfo()

CompanyDetails.__doc__


# In[10]:


'''
lets talk about __init__ now
Its a constructor and responsible declare and intialize the variable values

in java constructor is className()

ex- class Student -> Student() - constructor
ex- class Company -> Student() - constructor

But in python name always -> __init__()

whenever we create a object, constructor is executed automatically and execute only once per object creation

every constructor must take atleast one argument as self and then any no of argument it can take

if we dont provide constructor the python only provides 1 constructor like its special

__init(self)

'''


# In[19]:


# if we dont give atleast 1 argument here??
class Demo:
    def __init__(self):
                print("construtor is getting execute here")
                      
d1=Demo() #d1 is the object of the class Demo here
d2=Demo() #d2 is the object of the class Demo here


# In[114]:


# Normal Example - where one constructor __init__ and a method tellCompanyInfo is made in the class 
# CompanyDetails, here the tellCompanyInfo method is called multiple times

class CompanyDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def __init__(self1,name, address, no_of_emp):
        self1.name=name
        self1.address=address
        self1.no_of_emp=no_of_emp
            
    def tellCompanyInfo(self2):
        print("company name is",self2.name)
        print("company address is",self2.address)
        print("company no of employees are",self2.no_of_emp)
                
c1=CompanyDetails("Infosys","E-City",2000) #c1 is the object of the class CompanyDetails here

c1.tellCompanyInfo()
c1.tellCompanyInfo()


# In[21]:


'''

Vaiables inside the class

1. Instance Varibles

2. Static Varibles

3. Local Varibles


Methods inside the class

1. Instance Methods

2. Static Methods

3. Local Methods


(Instance -> Object) variable


(Static -> Class level) variable


(Local -> Method level) variable

'''


# In[138]:


# Instance varible changes from time to time

# Normal Example - where one constructor __init__ and a method tellCompanyInfo is made in the class 
# CompanyDetails, here an additional instance variable no_of_offices is added to the object insatance c1

class CompanyDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def __init__(self1, name, address, no_of_emp):
        self1.name=name
        self1.address=address
        self1.no_of_emp=no_of_emp

    def tellCompanyInfo(self2):
        print("company name is",self2.name)
        print("company address is",self2.address)
        print("company no of employees are",self2.no_of_emp)
        
# variable values are changing object by object so its instance variable 
# variable which are declared using self function are instance varibles
        
c1=CompanyDetails("Infosys","E-City",2000) #c1 is the object of the class CompanyDetails here
c1.tellCompanyInfo()
print("*******************")

c2=CompanyDetails("CGI","Whitefield",5000) #c2 is the object of the class CompanyDetails here
c2.tellCompanyInfo()
print("*******************")

c3=CompanyDetails("TCS","MG_Road",10000) #c3 is the object of the class CompanyDetails here
c3.tellCompanyInfo()

#printing instance variable

print("***********")
print("Instance varible are .......",c1.__dict__)  #printing the object instances in a dictionary format
print("***********")
print("Instance varible are .......",c2.__dict__)  #printing the object instances in a dictionary format
print("***********")
print("Instance varible are .......",c3.__dict__)  #printing the object instances in a dictionary format


# In[137]:


# Instance varible changes from time to time

# Normal Example - where one constructor __init__ and a method tellCompanyInfo is made in the class 
# CompanyDetails, here an additional instance variable no_of_offices is added to the object insatance c1

class CompanyDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def __init__(self1, name, address, no_of_emp):
        self1.name=name
        self1.address=address
        self1.no_of_emp=no_of_emp

    def tellCompanyInfo(self2):
        print("company name is",self2.name)
        print("company address is",self2.address)
        print("company no of employees are",self2.no_of_emp)
        
# variable values are changing object by object so its instance variable 
# variable which are declared using self function are instance varibles
        
c1=CompanyDetails("Infosys","E-City",2000) #c1 is the object of the class CompanyDetails here
c1.tellCompanyInfo()
print("*******************")

c2=CompanyDetails("CGI","Whitefield",5000) #c2 is the object of the class CompanyDetails here
c2.tellCompanyInfo()
print("*******************")

c3=CompanyDetails("TCS","MG_Road",10000) #c3 is the object of the class CompanyDetails here
c3.tellCompanyInfo()

#printing instance variable

print("***********")
print("Instance varible are .......",c1.__dict__)  #printing the object instances in a dictionary format
print("***********")
print("Instance varible are .......",c2.__dict__)  #printing the object instances in a dictionary format
print("***********")
print("Instance varible are .......",c3.__dict__)  #printing the object instances in a dictionary format

# from outside of class the with object reference so this variable becomes the instance variable

c1.no_of_offices = 10  #an addtional variable for the same object instance c1

# now no of instance variables are 4(one more variable is added5r)

print("***********")
print("Instance varible are .......",c1.__dict__) #printing the object instances in a dictionary format
print("***********")
print("Instance varible are .......",c2.__dict__) #printing the object instances in a dictionary format
print("***********")
print("Instance varible are .......",c3.__dict__) #printing the object instances in a dictionary format


# In[136]:


# Class variable can be used by all objects

# Normal Example - where one constructor __init__ and a method tellCompanyInfo is made in the class 
# CompanyDetails, here an additional instance variable no_of_offices is added to the object insatance c1

class CompanyDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    no_of_products=100  #static variable, can be used in all methods of the class, this is a class variable
    
    def __init__(self1,name, address, no_of_emp):
        self1.name=name
        self1.address=address
        self1.no_of_emp=no_of_emp
                                
    def tellCompanyInfo(self2):
        print("company name is",self2.name)
        print("company address is",self2.address)
        print("company no of employees are",self2.no_of_emp)
        print("company product is",self2.no_of_products)
        
# variable values are changing object by object so its instance variable, 

# variable which are declared using self function are instance varibles
        
c1=CompanyDetails("Infosys","E-City",2000)
c1.tellCompanyInfo()

print("*******************")

c2=CompanyDetails("CGI","Whitefield",5000)
c2.tellCompanyInfo()

print("*******************")

c3=CompanyDetails("TCS","MG_Road",10000)
c3.tellCompanyInfo()

#printing instance variable

print("***********")
print("Instance varible are .......",c1.__dict__) #printing the object instances in a dictionary format
print("***********")
print("Instance varible are .......",c2.__dict__) #printing the object instances in a dictionary format
print("***********")
print("Instance varible are .......",c3.__dict__) #printing the object instances in a dictionary format


# In[135]:


# Local variable can ne used only within the function

class CompanyDetails:
    '''this class is for learning purpose and gives the details about the company information'''
    
    def __init__(self1,name, address, no_of_emp):
        self1.name=name
        self1.address=address
        self1.no_of_emp=no_of_emp

    def tellCompanyInfo(self2):
        no_of_products=10       # local variable in the method tellCompanyInfo can be used only within this method
        print("company product is",no_of_products)        
        print("company name is",self2.name)
        print("company address is",self2.address)
        print("company no of employees are",self2.no_of_emp)
        
# variable values are changing object by object so its instance variable, 
# variable which are declared using self function are instance varibles
        
c1=CompanyDetails("Infosys","E-City",2000)
c1.tellCompanyInfo()
print("*******************")

c2=CompanyDetails("CGI","Whitefield",5000)
c2.tellCompanyInfo()
print("*******************")

c3=CompanyDetails("TCS","MG_Road",10000)
c3.tellCompanyInfo()

#printing instance variable

print("***********")
print("Instance variable are .......",c1.__dict__) #printing the object instances in a dictionary format
print("***********")
print("Instance variable are .......",c2.__dict__) #printing the object instances in a dictionary format
print("***********")
print("Instance variable are .......",c3.__dict__) #printing the object instances in a dictionary format


# In[9]:


# Static variable can be used within the class function

class CompanyDetails:
        
    industryType="IT-Industry"  #static variable
    
    def __init__(self1, name, address, no_of_emp):
        
        self1.name=name
        self1.address=address
        self1.no_of_emp=no_of_emp

    def tellCompanyInfo(self2):
                
        print("company name is",self2.name)
        print("company address is",self2.address)
        print("company no of employees are",self2.no_of_emp)
        
    #@classmethod   # this is a decorator *******************
    def getIndustryType(cls1):
        print("Type of industry is:",cls1.industryType)
        
        # this method is using class level variableso its class level method
        # cls is alternate to self (in instance we use self and in class method)        
        # self and cls are not predefined we can use any name
        
    def findSum(self, no1, no2):  #local method
        print("sum is:",(no1+no2))
        
def findAverage(no1, no2):       #local method
    print("Average is:",(no1+no2)/2)
            
c1=CompanyDetails("Infosys","E-City",2000)
            
c1.tellCompanyInfo()
            
CompanyDetails.getIndustryType(c1)

c1.getIndustryType()

print("*********************")

c1.findSum(10,10)    # method1 to call findSum

CompanyDetails.findSum(c1, 10, 10) # method2 to call findSum

findAverage(10, 10)


# In[158]:


# Local variable can ne used only within the local function

class CompanyDetails:
        
    def __init__(self1,name, address, no_of_emp):
        
        self1.name=name
        self1.address=address
        self1.no_of_emp=no_of_emp

    def tellCompanyInfo(self2):
                
        print("company name is",self2.name)
        print("company address is",self2.address)
        print("company no of employees are",self2.no_of_emp)
        
    @staticmethod   # this is a decorator *******************
    def findSum(no1, no2):  #local method - no self or cls keyword is required
        print("sum is:",(no1+no2))
        
def findAverage(no1, no2):       #local method
    print("Average is:",(no1+no2)/2)
            
c1=CompanyDetails("Infosys","E-City",2000)

c2=CompanyDetails("Infosys","E-City",2000)
            
c1.tellCompanyInfo()

print("*********************")

c2.tellCompanyInfo()
            
print("*********************")

c1.findSum(10,10)    # method1 to call findSum
CompanyDetails.findSum(13, 10) # method2 to call findSum

print("*********************")

c2.findSum(20,10)    # method1 to call findSum
CompanyDetails.findSum(14, 10) # method2 to call findSum

findAverage(10, 10)


# In[160]:


# deleting the variables

class Demo:
    def __init__(self):
        self.x=10
        self.y=20
        self.z=30
        
    def delete(self):
        del self.x
        del self.y
        
d1=Demo()

print(d1.__dict__)
print(".........")
d1.delete()
print(d1.__dict__)

del d1.z
print(".........")
print(d1.__dict__) 


# In[161]:


# deleting the variables

class Demo:
    def __init__(self):
        self.x=10
        self.y=20
        self.z=30
        
d1=Demo()
d2=Demo()

del d1.x
del d2.y

print(d1.__dict__)
print(".........")
print(d2.__dict__)


# In[ ]:


'''

Setter and Getter Functions (Alternative to Constructor)

def setvariableName(self, variableName):
    self.variableName=variableName
    
def getvariableName(self):
    return self.variableName
    
1.Inside the Constructor(__init__) we can not write validation but in getter function we can write the validation

'''


# In[164]:


# Setter and Getter Way

class CompanyDetails:
    
    def setName(self, name):
        self.name=name
        
    def getName(self):
        return self.name
    
    def setAddress(self, address):
        self.address=address
    
    def getAddress(self):
        return self.address
    
    def setNo_of_Employees(self, no_of_emp):
        self.no_of_emp=no_of_emp
    
    def getNo_of_Employees(self):
        return self.no_of_emp
    
c2=CompanyDetails()

c2.setName("TCS")
c2.setAddress("E-City")
c2.setNo_of_Employees(2000)

print("company name is:",c2.getName())
print("company address is:",c2.getAddress())
print("company no of employees is:",c2.getNo_of_Employees())


# In[167]:


# Inheritance in Python

# extending the functionality from parent to child class and code re-usability

# if child class dont want or not satisfied with the parent implementation then in child also we can create
# the method here

# syntax - 

# class childclassname(parentclass1, parentclass2....)

class PoliticalFamily:
    def givingProperty(self):
        print("Cash + gold + diamond + Farm House + Land + business")
        
    def kidMarriage(self):
        print("family is doing marriage of kid with Rani")
        
class FamilyKid(PoliticalFamily): 
    pass  # Note: Use the pass keyword when you do not want to add any other properties or 
          #methods to the class.

kid=FamilyKid()

kid.givingProperty()
kid.kidMarriage()


# In[168]:


# if child class is not satisfied with parent class method then child can override that method in parent class

class PoliticalFamily:
    def givingProperty(self):
        print("Cash + gold + diamond + Farm House + Land + business")
        
    def kidMarriage(self):
        print("family is doing marriage of kid with Rani")
        
class FamilyKid(PoliticalFamily): 
    def kidMarriage(self):
        print("Kid is doing marriage with Katrina.......")

kid=FamilyKid()

kid.givingProperty()
kid.kidMarriage()


# In[187]:


# if child wants to call the parent class method also then we can use super()

class PoliticalFamily:
    def givingProperty(self):
        print("Cash + gold + diamond + Farm House + Land + business")
        
    def kidMarriage(self):
        print("family is doing marriage of kid with Rani")
        
class FamilyKid(PoliticalFamily): 
    def kidMarriage(self):
        print("Kid is doing marriage with Katrina.......")
        super().kidMarriage()
        
kid=FamilyKid()

kid.givingProperty()
kid.kidMarriage()


# In[279]:


class Bird:
    
    def __init__(self):
        self.hungry = 1
        
    def eat(self):
        if self.hungry == 1:
            print('hungry....')
            self.hungry = 0
        else:
            print('No, thanks!')
            
class SongBird(Bird):
    
    def __init__(self):
        #super(SongBird, self).__init__()  
        super().__init__()                    # same as super(SongBird, self).__init__() 
        self.sound = 'Squawk!'
        
    def sing(self):
        print(self.sound)

sb = SongBird()

sb.sing()
sb.eat()
sb.eat()


# In[11]:


class Person:
    
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
        
    def showName(self):
        print(self.name)    # directly prints the data
    
    def showAge(self):
        print(self.age)
        
class Student:
    
    def __init__(self, studentId):
        self.studentId  = studentId
        
    def getId(self):
        return self.studentId  # should be used in a print statement to print the studentId
    
class Resident(Person, Student):
    
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)
        
resident1 = Resident('John', 30, '102')
resident1.showName()
resident1.showAge()
#resident1.getId()
print(resident1.getId())


# In[287]:


# calling parent class members from child class - Normal Type

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.marks=marks
    
    def showStudent(self):
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Student RollNo :",self.rollno)
        print("Student Marks :",self.marks)                 
        
class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        self.name=name
        self.age=age
        self.salary=salary
        self.subject=subject
        
    def showTeacher(self):
        print("Teacher Name :",self.name)
        print("Teacher Age :",self.age)
        print("Teacher Salary :",self.salary)
        print("Teacher Subject :",self.subject) 
        
s1=Student("Raj",23, 110, 80)

s1.showStudent()

print("***************")

p1=Teacher("Ramesh", 40, 60000, "Python")

p1.showTeacher()

# here the name and age are by default will come to child class and code we have to write multiple time

# if parent class have 100 properties then in every child class have to take 100 proper intialization is 

# coming in child


# In[317]:


# calling class members of one class in another class - no inheritance involved here

class Person:
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
class Student():
    
    def __init__(self, name, age, rollno, marks):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.marks=marks 
        
    def showStudent(self):
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Student RollNo :",self.rollno)
        print("Student Marks :",self.marks)   
        
class Teacher():
    
    def __init__(self, name, age, salary, subject):
        self.name=name
        self.age=age
        self.salary=salary
        self.subject=subject
        
    def showTeacher(self):
        print("Teacher Name :",self.name)
        print("Teacher Age :",self.age)
        print("Teacher Salary :",self.salary)
        print("Teacher Subject :",self.subject) 
        
s1=Student("Raj", 23, 110, 80)    # Student.__init__(s1, "Raj", 23, 110, 80)

s1.showStudent()                  # Student.showStudent(s1)

print("***************")

p1=Teacher("Ramesh", 40, 60000, "Python") # Teacher.__init__(p1, "Raj", 23, 110, 80)

p1.showTeacher()                          # Teacher.showTeacher(p1)


# In[339]:


# calling parent class members from child class - Analysis example without __init__ constructor

class Person:
    def getNameAge(self, name, age):
        self.name=name
        self.age=age
                
class Student(Person):
    
    def getRollnomarks(self, rollno, marks):
        self.rollno=rollno
        self.marks=marks
    
    def showStudent(self):
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Student RollNo :",self.rollno)
        print("Student Marks :",self.marks)                
        
class Teacher(Person):

    def getsalarysubject(self, salary, subject):
        self.salary=salary
        self.subject=subject
        
    def showTeacher(self):
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Teacher Salary :",self.salary)
        print("Teacher Subject :",self.subject)
        
s11=Student()

Person.getNameAge(s11, "Raj", 23)    # Student.__init__(s1, "Raj", 23, 110, 80)

Student.getRollnomarks(s11, 110, 80)    # Student.__init__(s1, "Raj", 23, 110, 80)

s11.showStudent()                  # Student.showStudent(s1)

print("***************")

t11=Teacher()

Person.getNameAge(t11, "Ramesh", 40)    # Teacher.__init__(t1, "Ramesh", 40, 60000, "Python") 

Teacher.getsalarysubject(t11, 60000, "Python")  # Teacher.__init__(t1, "Ramesh", 40, 60000, "Python")  

t11.showTeacher()                          # Teacher.showTeacher(t1)

# here the name and age are by default will come to child class and code we have to write multiple time

# if parent class have 100 properties then in every child class have to take 100 proper intialization is 

# coming in child


# In[347]:


# calling parent class members from child class - Analysis example with __init__ constructor - Correct Example
# better understanding

class Person:
    def __init1__(self):
    #def __init__(self):
        self.name="Srinivasan"
        self.age=34
        print("Student Name :",self.name)
        print("Student Age :",self.age)
                
class Student(Person):
    
    def __init__(self):
        self.rollno=110
        self.marks=80
    
    def showStudent(self):
        print("Student RollNo :",self.rollno)
        print("Student Marks :",self.marks)                
        
class Teacher(Person):

    def __init__(self):
        self.salary=60000
        self.subject="Python"
        
    def showTeacher(self):
        print("Teacher Salary :",self.salary)
        print("Teacher Subject :",self.subject)
        
s22=Student()

s22.__init1__()

s22.showStudent()                  # Student.showStudent(s1)

print("***************")

t22=Teacher()

t22.__init1__()

t22.showTeacher()                          # Teacher.showTeacher(t1)

# here the name and age are by default will come to child class and code we have to write multiple time

# if parent class have 100 properties then in every child class have to take 100 proper intialization is 

# coming in child


# In[288]:


# calling class members of one class in another class - no inheritance involved here

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
class Student():
    def __init__(self, name, age, rollno, marks):
        Person.__init__(self, name, age)      # Person.__init__(s1, "Raj", 23)
        self.rollno=rollno
        self.marks=marks 
        
    def showStudent(self):
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Student RollNo :",self.rollno)
        print("Student Marks :",self.marks)   
        
class Teacher():
    def __init__(self, name, age, salary, subject):
        Person.__init__(self, name, age)       # Person.__init__(p1, "Raj", 23, 110, 80)
        self.salary=salary
        self.subject=subject
        
    def showTeacher(self):
        print("Teacher Name :",self.name)
        print("Teacher Age :",self.age)
        print("Teacher Salary :",self.salary)
        print("Teacher Subject :",self.subject) 
        
s1=Student("Raj", 23, 110, 80)    # Student.__init__(s1, "Raj", 23, 110, 80)

s1.showStudent()                  # Student.showStudent(s1)

print("***************")

p1=Teacher("Ramesh", 40, 60000, "Python") # Teacher.__init__(p1, "Raj", 23, 110, 80)

p1.showTeacher()                          # Teacher.showTeacher(p1)


# In[ ]:


# calling class members of one class in another class - Type 2

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        Person.__init__(self, name, age)      # Person.__init__(s1, "Raj", 23)
        self.rollno=rollno
        self.marks=marks 
        
    def showStudent(self):
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Student RollNo :",self.rollno)
        print("Student Marks :",self.marks)   
        
class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        Person.__init__(self, name, age)       # Person.__init__(p1, "Raj", 23, 110, 80)
        self.salary=salary
        self.subject=subject
        
    def showTeacher(self):
        print("Teacher Name :",self.name)
        print("Teacher Age :",self.age)
        print("Teacher Salary :",self.salary)
        print("Teacher Subject :",self.subject) 
        
s1=Student("Raj", 23, 110, 80)    # Student.__init__(s1, "Raj", 23, 110, 80)

s1.showStudent()                  # Student.showStudent(s1)

print("***************")

p1=Teacher("Ramesh", 40, 60000, "Python") # Teacher.__init__(p1, "Raj", 23, 110, 80)

p1.showTeacher()                          # Teacher.showTeacher(p1)


# In[282]:


# super() method - to call parent class members(__init__ alone) from child class we use super() method

class Person:
    def __init__(self, name, age):
        print("Super Constructor is called")
        self.name=name
        self.age=age
        
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno=rollno
        self.marks=marks 
        
    def showStudent(self):
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Student RollNo :",self.rollno)
        print("Student Marks :",self.marks)   
        
        
class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary=salary
        self.subject=subject
        
    def showTeacher(self):
        print("Teacher Name :",self.name)
        print("Teacher Age :",self.age)
        print("Teacher Salary :",self.salary)
        print("Teacher Subject :",self.subject) 
        
s1=Student("Raj",23, 110, 80)

s1.showStudent()

print("***************")

p1=Teacher("Ramesh", 40, 60000, "Python")

p1.showTeacher()

# here the name and age are by default will come to child class and code we have to write multiple time

# if parent class have 100 properties then in every child class have to take 100 proper intialization is 

# coming in child


# In[13]:


# super() method - to call parent class members(__init__ and print) from child class we use super() method

class Person:
    def __init__(self, name, age):
        print("Super Constructor is called")
        self.name=name
        self.age=age
    
    def showPerson(self):
        print("Name :",self.name)
        print("Age :",self.age)
        
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno=rollno
        self.marks=marks 
        
    def showStudent(self):
        Person.showPerson(self)
        print("Student RollNo :",self.rollno)
        print("Student Marks :",self.marks)   
        
class Teacher(Person):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary=salary
        self.subject=subject
        
    def showTeacher(self):
        Person.showPerson(self)
        print("Teacher Salary :",self.salary)
        print("Teacher Subject :",self.subject) 
        
s1=Student("Raj",23, 110, 80)

s1.showStudent()

print("***************")

p1=Teacher("Ramesh", 40, 60000, "Python")

p1.showTeacher()

# here the name and age are by default will come to child class and code we have to write multiple time

# if parent class have 100 properties then in every child class have to take 100 proper intialization is 

# coming in child


# In[212]:


class Company1:
    def companyinfo(self):
        print("Company1 info is here")
                
class Company2(Company1):
    def companyinfo(self):
        print("Company2 info is here")
        super().companyinfo()
        
class Company3(Company2):
    def companyinfo(self):
        print("Company3 info is here")
        super().companyinfo()
        
class Company4(Company3):
    def companyinfo(self):
        print("Company4 info is here")
        super().companyinfo()
        
class Company5(Company4):
    def companyinfo(self):
        print("Company5 info is here")
        super().companyinfo()
        
c1=Company5()

c1.companyinfo()


# In[213]:


class Company1:
    def companyinfo(self):
        print("Company1 info is here")
                
class Company2(Company1):
    def companyinfo(self):
        print("Company2 info is here")
        super().companyinfo()
        
class Company3(Company2):
    def companyinfo(self):
        print("Company3 info is here")
        super().companyinfo()
        
class Company4(Company3):
    def companyinfo(self):
        print("Company4 info is here")
                
class Company5(Company4):
    def companyinfo(self):
        print("Company5 info is here")
        super().companyinfo()
        
c1=Company5()

c1.companyinfo()


# In[214]:


class Company1:
    def companyinfo(self):
        print("Company1 info is here")
                
class Company2(Company1):
    def companyinfo(self):
        print("Company2 info is here")
        super().companyinfo()
        
class Company3(Company2):
    def companyinfo(self):
        print("Company3 info is here")
        super().companyinfo()
        
class Company4(Company3):
    pass

class Company5(Company4):
    def companyinfo(self):
        print("Company5 info is here")
        super().companyinfo()
        
c1=Company5()

c1.companyinfo()


# In[217]:


class Company1:
    def companyinfo(self):
        print("Company1 info is here")
                
class Company2(Company1):
    def companyinfo(self):
        print("Company2 info is here")
                
class Company3(Company2):
    def companyinfo(self):
        print("Company3 info is here")
                
class Company4(Company3):
    pass

class Company5(Company4):
    def companyinfo(self):
        super().companyinfo()
        
c1=Company5()

# c1.companyinfo()


# In[14]:


# calling a particular parent class method

class Company1:
    def companyinfo(self):
        print("Company1 info is here")
                
class Company2(Company1):
    def companyinfo(self):
        print("Company2 info is here")
                
class Company3(Company2):
    def companyinfo(self):
        print("Company3 info is here")
                
class Company4(Company3):
    def companyinfo(self):
        print("Company4 info is here")
        
class Company5(Company4):
    def companyinfo(self):
        #super().companyinfo()
        super(Company2, self).companyinfo()
        
c1=Company5()

c1.companyinfo()


# In[20]:


class Parent:
    
    x=10                   # here x is a static variable
    
    def __init__(self):    # constructor
        self.y=20
        print(self.y)
                
class Child(Parent):
    
    def __init__(self):    # constructor
        Parent.__init__(self)    
        self.z=30
        print(self.z)
        
# even though Parent class is inherited in the child class it has to be intialized again 
# in the child class if __init__constructor is available in the child class
                       
    def display(self):
        
        print(self.x)
           
c3=Child()
print("Value of x is:",c3.x)
print("Value of y is:",c3.y)
c3.display() 
print("Value of x is:",c3.x)
print("Value of y is:",c3.y)


# In[26]:


# from child constructor can we call the parent constructor, class method, static method, instance method 

# here super() is  used insted of the parent class name


class Demo:
    def __init__(self):
        print("parent constructor got executed")
        
    def test1(self):
        print("parent instance got executed")
    
    def test2(cls):
        print("parent class method got executed")
        
    def test3(cls):
        print("parent static method got executed")
        
class Child(Demo):
    
    def __init__(self):
        super().__init__()
        super().test1()
        super().test2()
        super().test3()
        
c1=Child()


# In[10]:


# from child instance method can we call the constructor, class method, static method, instance method 
# can be called using super()


class Demo:
    def __init__(self):
        print("parent constructor got executed")
        
    def test1(self):
        print("parent instance got executed")
    
    @classmethod
    def test2(self):
        print("parent class method got executed")
        
    #@staticmethod
    def test3():
        print("parent static method got executed")
        
class Child(Demo):
    
    def display(self):
        #super().__init__()
        super().test1()
        super().test2()
        test3()
        
c1=Child()
c1.display()


# In[11]:


# from child class method can we call the constructor, class method, static method, instance method 
# can be called using super()

# Doubt - ?????????????


class Demo:
    def __init__(self):                          # this method will be called by default, as it is a constructor
        print("parent constructor got executed") # but calling for the second time using super() throws an error
                                                 # since self parameter is used and in the function call cls 
    def test1(self):
        print("parent instance got executed")    # this method is a instance method which cannot be called
                                                 # from a class method, since self parameter is used and in the 
                                                 # function call cls
    @classmethod
    def test2(cls):                              # this method is a class method which can be called          
        print("parent class method got executed")# from a class method
        
    @staticmethod
    def test3():                                   # this method is a static method which can be called 
        print("parent static method got executed") # from a class method
        
class Child(Demo):
    
    @classmethod
    def display(cls):
        super().__init__()
        super().test1()
        super().__init__(cls)
        super().test1(cls)
        #super().test2()
        #super().test3()
        
c1=Child()
c1.display()


# In[9]:


# how to call parent class constructor, instance method from the class method of child class

# Solution for the above problem - ???? - delf or self just a name here

# Doubt - ?????????????

class Demo:
    def __init__(self):
        print("parent constructor got executed")
        
    def test1(self):
        print("parent instance got executed")
    
    @classmethod
    def test2(cls):
        print("parent class method got executed")
        
    @staticmethod
    def test3():
        print("parent static method got executed")
        
class Child(Demo):
    
    @classmethod
    def display(delf):
    #def display(self):
        super(Child, delf).__init__(delf)
        super(Child, delf).test1(delf)
        super().test2()
        super().test3()
        
c1=Child()
c1.display()


# In[393]:


# from child static method can we call the constructor, class method, static method, instance method 
# can be called using super()

# Doubt - ?????????????


class Demo:
    def __init__(self):                          # this method will be called by default, as it is a constructor
        print("parent constructor got executed") # but calling for the second time using super() throws an error
                                                 # since self parameter is used and in the function call cls 
    def test1(self):
        print("parent instance got executed")    # this method is a instance method which cannot be called
                                                 # from a class method, since self parameter is used and in the 
                                                 # function call cls
    @classmethod
    def test2(cls):                              # this method is a class method which can be called          
        print("parent class method got executed")# from a class method
        
    @staticmethod
    def test3():                                   # this method is a static method which can be called 
        print("parent static method got executed") # from a class method
        
class Child(Demo):
    
    @staticmethod
    def display():
        super().__init__()
        super().test1()
        super().test2()        
        super().test3()
        
c1=Child()
c1.display()


# In[402]:


# from child static method can we call the constructor, class method, static method, instance method 
# can be called using super()

# Doubt - ?????????????


class Demo:
    def __init__(self):                          # this method will be called by default, as it is a constructor
        print("parent constructor got executed") # but calling for the second time using super() throws an error
                                                 # since self parameter is used and in the function call cls 
    def test1(self):
        print("parent instance got executed")    # this method is a instance method which cannot be called
                                                 # from a class method, since self parameter is used and in the 
                                                 # function call cls
    @classmethod
    def test2(cls):                              # this method is a class method which can be called          
        print("parent class method got executed")# from a class method
        
    @staticmethod
    def test3():                                   # this method is a static method which can be called 
        print("parent static method got executed") # from a class method
        
class Child(Demo):
    
    @staticmethod
    def display():
        #super().__init__()
        super(Child,Child).test1()
        super(Child,Child).test2()        
        super(Child,Child).test3()
        
c1=Child()
c1.display()

# Child, Child - go to super class of child and then call the static method with classname so 2 args


# In[8]:


# Abstraction in Python
# abc => abstract base calss module

from abc import ABC, abstractmethod 
#from abc import *
class Demo:
    @abstractmethod     # creating an abstract method
    def demomethod(self):
        pass  


# In[407]:


dir(abc)


# In[3]:


import abc

class Demo():
    pass

d1=Demo()


# In[4]:


#creating abstract class by extendding ABC class
import abc

class Demo(ABC):  # extending ABC class to create abstract class    
    pass

d1=Demo()


# In[414]:


import abc

class Demo(ABC):    # extending ABC class to create abstract class
    
    @abstractmethod # creating an abstract method
    def demomethod(self):
        pass

d1=Demo()


# In[5]:


import abc

#class Demo(ABC):   # extending ABC class to create abstract class    
class Demo(): 
    
    @abstractmethod # creating an abstract method
    def demomethod(self):
        pass

d1=Demo()


# In[7]:


# Eventhough the child class doesn't implement the abstract method of parent class, But its an abstract class 
# then it cant create object for itself (child class)

import abc

class Musician(abc):
    def payment(self):
        print("Payment is happening for all musicians.......")
        
    @abstractmethod
    def thememusic(self):
        pass
    
class Guitarplayer(Musician):
    pass

gp=Guitarplayer() 
#m1=Musician()


# In[425]:


import abc

class Musician(ABC):
    def payment(self):
        print("Payment is happening for all musicians.......")
        
    @abstractmethod
    def thememusic(self):
        pass
    
class Guitarplayer(Musician):
    #def thememusic1(self):         # here the thememusic method of the child class overrides the abstract
                                    # method of the parent class, so it works here
    def thememusic(self):         
        print("Strum Strum Strum Strum Strum.........")
    #pass

gp=Guitarplayer() 
#gp.thememusic1()
gp.thememusic()


# In[426]:


import abc

class Musician(ABC):
    def payment(self):
        print("Payment is happening for all musicians.......")
        
    @abstractmethod
    def thememusic(self):
        pass
    
class Guitarplayer(Musician):
    #def thememusic1(self):         # here the thememusic method of the child class overrides the abstract
                                    # method of the parent class, so it works here
    def thememusic(self):         
        print("Strum Strum Strum Strum Strum.........")
    #pass
    
class Drumplayer(Musician):
    #def thememusic1(self):         # here the thememusic method of the child class overrides the abstract
                                    # method of the parent class, so it works here
    def thememusic(self):         
        print("Dum Dum Dum Dum Dum.........")
    #pass

gp=Guitarplayer() 
#gp.thememusic1()
gp.thememusic()

dp=Drumplayer() 
#gp.thememusic1()
dp.thememusic()


# In[431]:


# interfaces - if and abstract class contains only abstract methods such type of abstract class
# is considered as interface

import abc

class DBInterface(ABC):   # this class is an interface
    
    @abstractmethod
    def connectdatabase(self):
        pass
    
    @abstractmethod
    def disconnectdatabase(self):
        pass
    
class MySQLDB(DBInterface):
    
    def connectdatabase(self):      # here the connectdatabase method of the child class overrides the abstract
                                    # method of the parent class, so it works here
        print("Connect with the mysql database.....")
    
    def disconnectdatabase(self):   # here the connectdatabase method of the child class overrides the abstract
                                    # method of the parent class, so it works here
         print("Disconnect with the mysql database.....")
            
class OracleDB(DBInterface):
    
    def connectdatabase(self):      # here the connectdatabase method of the child class overrides the abstract
                                    # method of the parent class, so it works here
        print("Connect with the oracle database.....")
    
    def disconnectdatabase(self):   # here the connectdatabase method of the child class overrides the abstract
                                    # method of the parent class, so it works here
         print("Disconnect with the oracle database.....")
        
dbname=input("Enter Database name:")
print(type(dbname))
classname=globals()[dbname]
x=classname()
x.connectdatabase()
x.disconnectdatabase()

# The inbuilt function globals()[str] converts the string 'str' into a class name and returns the classname.


# In[436]:


name = 'Pankaj'

print(globals()['name'])

# print(globals()[name]) - this will convert the string 'Pankaj' into a class name, But the same 
# cannot be printed

# This function returns the dictionary of the current module.


# In[442]:


def globalstuff():
    global g1
    g1 = 'Global'
    
    
globalstuff()  # calling globalstuff() to set the variables

# print(globals())

print(globals() ['g1'])


# In[443]:


# public, protected, private 

# Default every candidate is public. We can access from anywhere either within the class or from 
# outside of the class(No underscore)

# Protected attributes can be accessed within the class anywhere and from the child classes(Single underscore)

# Private attributes can be accessed only from inside the class not outside class(Double underscore)


# In[444]:


class Demo:
    
    x=10     # public    - We can access from anywhere either within the class or from outside of the class
    _y=20    # protected - can be accessed within the class anywhere and from the child 
    __z=30   # private   - can be accessed only from inside the class not outside class
    
    def getvalues(self):
        print(Demo.x)
        print(Demo._y)
        print(Demo.__z)
        
d1=Demo()
d1.getvalues()


# In[447]:


class Demo:
    
    x=10     # public    - We can access from anywhere either within the class or from outside of the class
    _y=20    # protected - can be accessed within the class anywhere and from the child 
    __z=30   # private   - can be accessed only from inside the class not outside class
    
    def getvalues(self):
        print(Demo.x)
        print(Demo._y)
        print(Demo.__z)
        
d1=Demo()
d1.getvalues()

print("**********")

print(Demo.x)
print(Demo._y)
print(Demo.__z)


# In[456]:


class Demo:
    
    x=10     # public    - We can access from anywhere either within the class or from outside of the class
    _y=20    # protected - can be accessed within the class anywhere and from the child 
    __z=30   # private   - can be accessed only from inside the class not outside class
    
    def getvalues(self):
        print(Demo.x)
        print(Demo._y)
        print(Demo.__z)
        
d1=Demo()
d1.getvalues()

print("**********")

print(Demo.x)
print(Demo._y)
print(d1._Demo__z)


# In[29]:


class Demo:
    
    x=10     # public    - We can access from anywhere either within the class or from outside of the class
    _y=20    # protected - can be accessed within the class anywhere and from the child 
    __z=30   # private   - can be accessed only from inside the class not outside class
    
    def getvalues(self):
        print(Demo.x)
        print(Demo._y)
        print(Demo.__z)
        
d1=Demo()
d1.getvalues()

print("**********")

print(d1.x)
print(d1._y)
print(d1.__z)


class Demo1(Demo):
    
    pass
        
d2=Demo1()
d2.getvalues()


# In[477]:


class Demo:
    
    x=10     # public    - We can access from anywhere either within the class or from outside of the class
    _y=20    # protected - can be accessed within the class anywhere and from the child 
    __z=30   # private   - can be accessed only from inside the class not outside class
    
    def getvalues(self):
        print(Demo.x)
        print(Demo._y)
        print(Demo.__z)
        
d1=Demo()
d1.getvalues()

print("**********")

print(Demo.x)
print(Demo._y)
print(d1._Demo__z)


class Demo1():
    
    pass
        
d2=Demo1()
d2.getvalues()


# In[9]:


# here how _y which is a protected variable is still printing, __z will not print as it is a private varible

class Demo:
    
    x=10     # public    - We can access from anywhere either within the class or from outside of the class
    _y=20    # protected - can be accessed within the class anywhere and from the child 
    __z=30   # private   - can be accessed only from inside the class not outside class
    
    def getvalues(self):
        print(Demo.x)
        print(Demo._y)
        print(Demo.__z)
        
d1=Demo()
d1.getvalues()

print("**********")

print(Demo.x)
print(Demo._y)
print(d1._Demo__z)


class Demo1():
    
    def getvalues(self):
        print(Demo.x)
        print(Demo._y)
        #print(Demo.__z)
        
d2=Demo1()
d2.getvalues()


# In[46]:


class Parent:
    def __init__(self,a):
        print(a)
        
class Child(Parent):
    def __init__(self,a,b):
        super().__init__(a)
        print(b)
        
    def show1(self,b):
        print(b)
    
    def show2(self,c):
        print(c)
        
c1=Child(10,20)


# In[54]:


#global a
a=10

def srini():
    nonlocal b
    b=20
    print(a)
    
def vasu():
    print(b)
    print(a)
    
srini()
vasu()


# In[2]:


class simple:
    pass

s1 = simple()

s1.name = 'xyz'

print(s1.name)


# In[ ]:





# In[ ]:





# In[ ]:



