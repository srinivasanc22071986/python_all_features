#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Module 1

def hello(name):
    print ("Hello World " + name)


# In[2]:


# Client 1

import Module1

Module1.hello("vasu")

Module1.hello("kalyani")

Module1.hello("4")

#Module1.hello(4)

Module1.hello("kalyani")


# In[3]:


# Module 2

def myAdd(no1 ,no2):
    return no1+no2

def mySub(no1 ,no2):
    return no1-no2

def myMul(no1,no2):
    return no1*no2


# In[ ]:


# Client 2

import Module2

salary=10000
bonous=3000
deduction=2500

def salaryWithBonous():
    return Module2.myAdd(salary,bonous)

def salarywithDeduction():
    return Module2.mySub(salary,deduction)
    

print(salaryWithBonous())
print(salarywithDeduction())


# In[4]:


# Client 2

# -*- coding: utf-8 -*-

import Module2

runsbybatsman=int(input("how many runs made by batsmans??"))

extraruns=int(input("how many runs runs given extra by bowlers??"))

no_of_six=int(input("how many four were hit by batsman??"))

no_of_four=int(input("how many four were hit by batsman??"))



totalbounderies=Module2.myAdd(no_of_six,no_of_four)

totalruns=Module2.myAdd(runsbybatsman,extraruns)

run_by_six=Module2.myMul(no_of_six , 6)
run_by_four=Module2.myMul(no_of_four , 4)

print("Total runs of team:..",totalruns)
print("Total bounderies are ...",totalbounderies)
print("Total runs came by six" , run_by_six)
# Client 3print("Total runs came by four" , run_by_four)


# In[6]:


# Module 3

# -*- coding: utf-8 -*-
"""

Special variable __name__: 
    
  If the program executed as an individual program then the value of this 
  variable is __main__.
  
  Hence by using this __name__ variable we can identify whether the program 
  executed directly or as a module. 
    

"""

def f1():
    if __name__=='__main__':
        print("The code executed as a program")
    else:
        print("The code executed as a module from some other program")
                
f1()


# In[ ]:


# Client 3

import Module3


Module3.f1()

