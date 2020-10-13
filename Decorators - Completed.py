#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Nested Function -> function inside function

# to define function specific repeat functionality we use nested functions


# In[36]:


def outerFunction():
    def innerFunction(a,b):
        print("sum of numbers is",a+b)
        print("mul of numbers is",a*b)
        
    innerFunction(10,20)
    innerFunction(20,30)
    innerFunction(5,10)        
        
outerFunction()


# In[4]:


# one function can take another function as a argument ex-map, filter, reduce

# same way a function can return another function


# In[6]:


def outerFunction():
    print("outer function started")
    
    def innerFunction():
        print("Inner function executed")
        
    print("outer function is returning inner function")
    return innerFunction

f1=outerFunction()  # here we are holding inner function with f1 variable

f1()                # inner function is assigned to f1 so directly also we can call that inner function


# In[7]:


# f1=outerFunction()   -> here function is called and executed and return the value(inner function)

# f1=outerFunction     -> here outer function we are assigning a new name


# In[8]:


# Decorator - info about and example (beauty parlour example)

# input function -> Decorator -> output function with extra added functionality

# Decorator is also a function and it takes a function as input and adds some functionality and returns
# the output function

# Decorator will not modify the exisitng function but it generates or adds extra functionality to already
# existing function only


# In[9]:


def greeting(name):
    print("hello",name,"Good morning")
    
greeting("Ram")
greeting("Raj")
greeting("Kami")


# In[13]:


# without touch want to extend the functionality of greeting function

def decorFunction(func):    # decorator function takes a function as argument
    def innerFunction(name):
        if name == 'Ramesh':
            print("Hello", name, "Good Evening")
        else:
            func(name)
            
    return innerFunction

#@decorFunction
def greeting(name):
    print("hello",name,"Good Morning")
    
greeting("Ram")
greeting("Ramesh")
greeting("Kami")


# In[14]:


# linking the decorator to the innerfunction

def decorFunction(func):    # decorator function takes a function as argument
    def innerFunction(name):
        if name == 'Ramesh':
            print("Hello", name, "Good Evening")
        else:
            func(name)
            
    return innerFunction

@decorFunction              # Linking the decorator to the function
def greeting(name):
    print("hello",name,"Good Morning")
    
greeting("Ram")
greeting("Ramesh")
greeting("Kami")


# In[16]:


# enabling and disabling the decorator - correct example

def decorFunction(func):    # decorator function takes a function as argument
    def innerFunction(name):
        if name == 'Ramesh':
            print("Hello", name, "Good Evening")
        else:
            func(name)
            
    return innerFunction

decorator_func = decorFunction(greeting)   # now we can call wish alone also or wish with also

def greeting(name):
    print("hello",name,"Good Morning")
    
greeting("Ramesh")                         # greeting function directly without decorator

decorator_func('Ramesh')                   # now we are calling the greeting with decorator function

print("****************")

decorator_func("Kami")                      # calling with decorator again with Kami input


# In[5]:


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide        # divide = smart_divide(divide)
def divide(a, b):
    print(a/b)
    
divide(10,2)


# In[6]:


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):              # printer = star(percent(printer))
    print(msg)


printer("Hello")

'''

First,

@star
@percent
def printer(msg):
    print(msg)
    
is converted as,

printer = star(percent(printer))

Step 1: Firstly, the function call "star(percent(printer))" reaches the following function definition 
"def star(func):" and the func variable holds the value "percent(printer)"

Step 2:After the function call of "def star(func)", the function returns the function name "inner" to 
printer variable, and again the inner function is called through the stmt "printer("Hello")"

Step 3 : During the inner function call, the flow reaches the following defintion "def inner(*args,**kwargs)",
args[0] will hold "Hello", this inner function now will print a row of 30 "*" characters, 
then the flow moves to "func(*args, **kwargs)", which will convert as "percent(printer("Hello")"

Step 3:Next the flow moves to the function defintion "def percent(func):", so again here func variable 
becomes as printer(*args, **kwargs), and args[0] will still hold "Hello", which can be interpreted as 
printer("Hello"), here directly inner function will be returned to

Step 4:Now this inner function now will print a row of 30 "%" characters,
and now the statement,func(*args, **kwargs) is executed which calls as, printer("Hello") and prints "Hello"

Step 5: Now again a row of 30 "%" characters, is printed, inner function name is returned 
to the calling position


# In[33]:


a=14
print(a)
print(type(a))
str1=str("14")
print(str1)
print(type(str1))

a  = '14'
print(a)
print(a[0:1])
print(a[1:2])

for x in str:
    print(x)


print(type(a))


list = a.split(',')
print(list)


# In[34]:


def srini(func):
    print("Srini function")
    
def vasu():
    print("Vasu function")
    
srini(vasu())
            


# In[35]:


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star                       # printer = star(percent(printer))
@percent
def printer(msg):
    print(msg)

printer("Hello")
'''
First,

@star
@percent
def printer(msg):
    print(msg)

is converted as, printer = star(percent(printer))

Step 1 : Firstly, the decorator @star and @percent, creates the function call in the below format,
                    
                                printer = star(percent(printer))

Step 2 : The function call "star(percent(printer))", first reaches the following function definition "def percent(func):", 
         as the inner function will be called first, and "printer" is assigned to the "func" variable, to create the 
         calling parameter for the outer function "star()" which in turn reaches the following function definition 
         "def star(func):".

Step 3 : The inner function call "percent(printer)", returns the function name "inner" to the
         calling place, so now the outer function call becomes "star(inner)"

Step 4 : The outer function call "star(inner)", returns the function name "inner" again to the callina place, and now 
         printer variable becomes inner,
         
                                printer = star(percent(printer))
                                printer = star(inner)
                                printer = inner

Step 5 : Now the function call "printer("Hello")", becomes "inner("Hello")", and will reach the function definition 
         "inner(*args, **kwargs)", inside the outer function call "star()".
        
Step 6 : The inner function call the outer function call star(), will prints "*" character 30 times and will call 
         "func(*args, **kwargs)", which becomes as "inner("Hello")", where args[0] holds "Hello" 

Step 7 : Now the function call "inner("Hello")", prints "%" character 30 times, and will call "func(*args, **kwargs)", 
         which becomes "printer("Hello")", where args[0] holds "Hello"

Step 8:  Now the function call "printer("Hello")", prints the "Hello" message, and returns to the calling place inside 
         the percent () function call, and prints "%" character 30 times and returns to the calling place inside 
         the star () function call and prints "*" character 30 times 
'


# In[9]:


def decor_sum(func):
    print("Here we are decorating the sum function");
    def inner(*args):
        print("The function is decorated")
        func(*args)
    return inner

#@decor_sum
def sum(*args):
    ans=0
    for x in args:
        ans+=x        
    print(ans)

sum=decor_sum(sum)

sum(10,20)


# In[ ]:




