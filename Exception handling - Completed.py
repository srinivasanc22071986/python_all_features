#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''

The Python Exception class hierarchy - https://airbrake.io/blog/python-exception-handling/class-hierarchy

Syntax Errors 
Exceptions

ZeroDivisionError : Occurs when a number is divided by zero.
Name Error        : It occurs when a name is not found. It may be local or global
Indentation Error : If incorrect indendation is given.
IOError           : It occurs when Inout Output operation fails.
EOFError          : It occurs when the end of the file is reached, 
                    and yet operations are being performed.
                    
'''


# In[2]:


no1 = int(input("Enter no1:"))
no2 = int(input("Enter no2:"))
resultno = no1/no2;
print(resultno)



# In[ ]:


'''

try:
    #code where we have doubt

except Exception1:
    #code to execute if exception1 comes

expect Exception2:
    #code to execute if exception2 comes

finally:
    #this cide will gets execute at any cost

'''


# In[1]:


try:
    no1 = int(input("Enter no1:"))
    no2 = int(input("Enter no2:"))
    resultno = no1/no2;
    print(resultno)
    
except:
    print("can't divide by zero")
    


# In[2]:


try:
    no1 = int(input("Enter no1:"))
    no2 = int(input("Enter no2:"))
    resultno = no1/no2;
    print(resultno)
    
except ArithmeticError as ex:
    print("can't divide by zero:",ex)


# In[3]:


try:
    no1 = int(input("Enter no1:"))
    no2 = int(input("Enter no2:"))
    resultno = no1/no2;
    print(resultno)
    
except Exception as ex:
    print("can't divide by zero:",ex)


# In[4]:


print (ZeroDivisionError.__bases__)


# In[ ]:


print (ArithmeticError.__bases__)


# In[ ]:


print (Exception.__bases__)


# In[ ]:


print (BaseException.__bases__)


# In[ ]:


print (object.__bases__)


# In[ ]:


print (ArithmeticError.__doc__)


# In[1]:


try:
    print(int(input("Enter a no here:")))    
except Exception as ex:
    print("this is not value:",ex)
else:
    print("No Exception happened")
          


# In[ ]:


import math


# In[ ]:


import srinivasan


# In[2]:


try:
    import srinivasan

except ModuleNotFoundError as ex:
    print("This module is not available:",ex)
    
else:
    print("No exception happened")


# In[ ]:


print(ModuleNotFoundError.__bases__)


# In[ ]:


print(ImportError.__bases__)


# In[ ]:


print(Exception.__bases__)


# In[ ]:


print(BaseException.__bases__)


# In[ ]:


print(object.__bases__)


# In[ ]:


print(Exception.__subclasses__())


# In[ ]:


print(ArithmeticError.__subclasses__())


# In[ ]:


print(ZeroDivisionError.__subclasses__())


# In[10]:


list1=[100,200,300]
print(list1[4])


# In[11]:


try:
    list1=[100,200,300]
    print(list1[4])
    
except IndexError as ex:
    print(ex)


# In[ ]:


dict1 = {'a':1,'b':2}
print (dict1['c'])


# In[ ]:


try:
    dict1 = {'a':1,'b':2}
    print (dict1['c'])
    
except KeyError as ex:
    print("The given key is not available in dict1:",ex)
    


# In[ ]:


try:
    no1 = int(input("Enter no1:"))
    no2 = input("Enter no2:")
    result = no1+no2
    print(result)
    
except TypeError as ex1:
    print("Vasu")
    print(ex1)
    
    
except ValueError as ex2:
    print("Srini")
    print(ex2)
    
else:
    print("No exception has happened")  


# In[ ]:


try:
    file1=open("/home/sriniintraining/kotak courier write3","r")
    file1.write("Hi Srinivasan")
    
except IOError as ex1:
    print(ex1)

else:
    print("No Exception has happened")
    
finally:
    print("We are closing the file now")
    file1.close()


# In[3]:


try:
    no1 = int(input("Enter no1:"))
    #no2 = input("Enter no2:")
    no2 = int(input("Enter no2:"))
    try:
        result = no1+no2
        print(result)
    
    except TypeError as ex1:
        print("Error in inner try block:",ex1)

    else:
        print("No Exception has happened in inner try block")
    
    finally:
        print("The inner try block has been handled")
 
except ValueError as ex2:
    print("Error in outer try block:",ex2)

else:
    print("No Exception has happened in outer try block")
    
finally:
    print("The outer try block has been handled")


# In[ ]:


'''

Lets Hava a Case Study Here

try:
    stmt1
    stmt2
    stmt3
    
    try:
        stmt4
        stmt5
        stmt6
    except x:
        stmt7
    finally:
        stmt8
    
    stmt9
except Y:
    stmt10
finally:
    stmt11

stmt12

case 1 - If no exception occurs all statments will be executed except stmt7 and stmt10, as these are the
         only stmts placed inside the exception block

case 2 - If exception occurs in stmt2 and the corresponding exception block got matched then, 
         stmt1, stmt2, stmt10, stmt11 and stmt12 only will execute, And since stmt4, stmt5, stmt6 are 
         placed inside the nested try block since stmt7 is placed inside the nested exception block, 
         and since stmt8 is placed inside the nested finally block, and also stmt9 is kept outside 
         the inner try-exception-finally blocks, all these statements will not execute, The reason behind this 
         control jump is as soon as the error happens and matched with the exception the control is directly
         passed to its correcponding exception block and there after continues with further statements, 
         without executing the middle statements
         
case 3 - If exception occurs in stmt5 and the corresponding inner exception block got matched then, 
         stmt1, stmt2, stmt3, stmt4, stmt5, stmt7, stmt8, stmt9, stmt11 and stmt12 only will execute, And since 
         stmt6 comes after stmt5 and since stmt10 is kept inside the outer exception block 
         which will execute only while there is any issue with stmt1, stmt2, stmt3, those statements will not 
         execute 
         
case 4 - If exception occurs in stmt5 and the outer exception block got matched then, 
         stmt1, stmt2, stmt3, stmt4, stmt5, stmt8, stmt9, stmt10, stmt11 and stmt12 only will execute, And since 
         stmt6 comes after stmt5 that statements will not execute 
         
'''


# In[ ]:


'''

try:
    Risky code

except:
    exception handling code (gets execute if exception in try block)

else:
    gets execute if no exception in try block
    
finally:
    100% executable code (cleanup code is written here)
    
'''


# In[ ]:


try:
    #print("i am in try block")
    print(10/0)
    
except:
    print("in except block")
    
else:
    print("inside the else block")
    
finally:
    print("finally block")


# In[9]:


print("Statements outside the outer try block is executed")

try:
    print("Statements in the outer try block is executed")
    
    no1 = int(input("Enter no1:"))
    
    #no2 = input("Enter no2:")
    
    no2 = int(input("Enter no2:"))
    
    try:
        print("Statements in the inner try block is executed")
        result = no1+no2
        result = no1/no2
            
    except TypeError as ex1:
        print("Statements in the inner exception block is executed")

    else:
        print("Statements in the else block of the inner exception block is executed")
    
    finally:
        print("Statements in the finally block of the inner try block is executed")
    
    print("Statements outside the inner try block but inside the outer try block is executed")
 
#except ValueError as ex2:

#except Exception as ex2:

except ValueError as ex2:
    print("Statements in the outer exception block is executed")

else:
    print("Statements in the else block of the outer exception block is executed")
    
finally:
    print("Statements in the finally block of the outer try block is executed")
    
print("Statements outside the outer try block is executed")


# In[1]:


'''

****************************************************************************************************************

Case 1 : If no exception happens, then the below will be output,

Statements outside the outer try block is executed
Statements in the outer try block is executed
Enter no1:10
Enter no2:10
Statements in the inner try block is executed
Statements in the else block of the inner exception block is executed
Statements in the finally block of the inner try block is executed
Statements outside the inner try block but inside the outer try block is executed
Statements in the else block of the outer exception block is executed
Statements in the finally block of the outer try block is executed
Statements outside the outer try block is executed

****************************************************************************************************************

Case 2 : If the exception happens in stmt 5(no2 = input("Enter no2:"))(ValueError), and if the same is 
         matched with the outer exception then the below will be output,

Statements outside the outer try block is executed
Statements in the outer try block is executed
Enter no1:10
Enter no2:a
Statements in the outer exception block is executed
Statements in the finally block of the outer try block is executed
Statements outside the outer try block is executed

****************************************************************************************************************

Case 3 : If the exception happens in stmt 5(no2 = input("Enter no2:"))(ValueError), and if the same is not 
         matched with the outer exception then the below will be output,

Statements outside the outer try block is executed
Statements in the outer try block is executed
Enter no1:10
Enter no2:a
Statements in the finally block of the outer try block is executed

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-9dc4a006c65d> in <module>
      4     no1 = int(input("Enter no1:"))
      5     #no2 = input("Enter no2:")
----> 6     no2 = int(input("Enter no2:"))
      7     try:
      8         print("Statements in the inner try block is executed")

ValueError: invalid literal for int() with base 10: 'a'

****************************************************************************************************************

Case 4 : If the exception happens in stmt 9(result = no1+no2)(TypeError), and if the same is matched with the 
         inner exception then the below will be output,

Statements outside the outer try block is executed
Statements in the outer try block is executed
Enter no1:10
Enter no2:a
Statements in the inner try block is executed
Statements in the inner exception block is executed
Statements in the finally block of the inner try block is executed
Statements outside the inner try block but inside the outer try block is executed
Statements in the else block of the outer exception block is executed
Statements in the finally block of the outer try block is executed
Statements outside the outer try block is executed

****************************************************************************************************************

Case 5 : If the exception happens in stmt 10(result = no1/no2)(ZeroDivisionError), and if the same is not matched with the inner but matched 
         with the outer exception then the below will be output,

Statements outside the outer try block is executed
Statements in the outer try block is executed
Enter no1:10
Enter no2:0
Statements in the inner try block is executed
Statements in the finally block of the inner try block is executed
Statements in the outer exception block is executed
Statements in the finally block of the outer try block is executed
Statements outside the outer try block is executed

****************************************************************************************************************

Case 6 : If the exception happens in stmt 10(result = no1/no2), and if the same is not matched with 
         both the inner and outer exception then the below will be output,

Statements outside the outer try block is executed
Statements in the outer try block is executed
Enter no1:10
Enter no2:0
Statements in the inner try block is executed
Statements in the finally block of the inner try block is executed
Statements in the finally block of the outer try block is executed

---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-1-5de23434cc63> in <module>
      8         print("Statements in the inner try block is executed")
      9         result = no1+no2
---> 10         result = no1/no2
     11 
     12     except TypeError as ex1:

ZeroDivisionError: division by zero

****************************************************************************************************************

'''


# In[ ]:




