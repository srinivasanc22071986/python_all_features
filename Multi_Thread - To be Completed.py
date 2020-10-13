#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''

# Multi Tasking

# process based multi tasking -executing multiple task where every task is independent task 
(System example) -OS level

# Thread Based Multi tasking -executing the independent parts of same task at same time - Programming Level

# Thread - Seperate flow of execution

# where ever a group of independent jobs of each other then we execute them same time (multithreading) 
not one by one jobs

# python supports internally thread(90% by python and 10% by developer using threading module)

'''


# In[2]:


import threading
print("current executing thread is:",threading.current_thread())


# In[3]:


dir(threading)


# In[4]:


print("current executing thread is:",threading.current_thread().getName())


# In[19]:


#Ways to create the Threads

import threading

def display():
    print("this code is executed by child thread: ",threading.current_thread().getName())
    
print("current executing thread is: ",threading.current_thread().getName())

t1=threading.Thread(target=display)

print("current executing thread is: ",threading.current_thread().getName())


# In[20]:


#Ways to create the Threads

import threading

def display():
    print("this code is executed by child thread: ",threading.current_thread().getName())
    
print("current executing thread is: ",threading.current_thread().getName())

print("*******")

t1=threading.Thread(target=display)
t1.start()

print("*******")

print("current executing thread is: ",threading.current_thread().getName())


# In[10]:


#Ways to create the Threads

import threading

#job of child thread
def display():
    for x in range(10):
        print("Child Thread")

t=threading.Thread(target=display)
t.start()

#job of parent thread
for x in range(10):
    print("Parent Thread")


# In[19]:


dir(Thread)


# In[13]:


#2nd way to create a thread by extending the Thread class way

import threading

class MyDemo(threading.Thread):
    def run(self):    #in run method we specifiy the job need to execute by child thread
        for x in range(10):
            print("Child Thread Executes")
            
#create object and starting the thread (no need to tell target here)
t=MyDemo()
t.start()

for x in range(10):
    print("Parent Thread Executes")     


# In[12]:


#3rd way to create a thread by extending the Thread class way

import threading

class MyDemo():
    def display(self):    #in run method we specifiy the job need to execute by child thread
        for x in range(10):
            print("Child Thread Executes")
            
#create object and starting the thread (no need to tell target here)
obj=MyDemo()                      #creating object of class
t=threading.Thread(target=obj.display)      #creating the thread class object with target
t.start()                         #starting the thread

for x in range(10):
    print("Parent Thread Executes")   


# In[14]:



import threading

class MyDemo():
    def display(self):    #in run method we specifiy the job need to execute by child thread
        for x in range(10):
            print("Child Thread Executes by:",current_thread().getName())
            
obj=MyDemo()
t1=threading.Thread(target=obj.display)
t2=threading.Thread(target=obj.display)
t3=threading.Thread(target=obj.display)
t4=threading.Thread(target=obj.display)

t1.start()
t2.start()
t3.start()
t4.start()


# In[31]:


# advantage of thread is - improve the perfomance here

import time

numbers=[10,20,30,40,50]

def getDoubleofNo(numbers):
    for n in numbers:
        time.sleep(1)
        print("double of no is:",n*2)
        
def getSquareofNo(numbers):
    for n in numbers:
        time.sleep(1)
        print("square of no is:",n*n)
        
begintime=time.time()

getDoubleofNo(numbers)
getSquareofNo(numbers)

endtime=time.time()

print("total time taken is:", endtime-begintime)


# In[33]:


# advantage of thread is - improve the perfomance here
import threading
import time

numbers=[10,20,30,40,50]

def getDoubleofNo(numbers):
    for n in numbers:
        time.sleep(1)
        print("double of no is:",n*2)
        
def getSquareofNo(numbers):
    for n in numbers:
        time.sleep(1)
        print("square of no is:",n*n)
        
begintime=time.time()

t1=Thread(target=getDoubleofNo(numbers))
t2=Thread(target=getSquareofNo(numbers))
t1.start()
t2.start()

endtime=time.time()

print("total time taken is:", endtime-begintime)


# In[34]:


# advantage of thread is - improve the perfomance here
import threading
import time

numbers=[10,20,30,40,50]

def getDoubleofNo(numbers):
    for n in numbers:
        time.sleep(1)
        print("double of no is:",n*2)
        
def getSquareofNo(numbers):
    for n in numbers:
        time.sleep(1)
        print("square of no is:",n*n)
        
begintime=time.time()

t1=Thread(target=getDoubleofNo,args=(numbers,))
t2=Thread(target=getSquareofNo,args=(numbers,))
t1.start()
t2.start()

endtime=time.time()

print("total time taken is:", endtime-begintime)


# In[37]:


# advantage of thread is - improve the perfomance here
import threading
import time

numbers=[10,20,30,40,50]

def getDoubleofNo(numbers):
    for n in numbers:
        time.sleep(1)
        print("double of no is:",n*2)
        
def getSquareofNo(numbers):
    for n in numbers:
        time.sleep(1)
        print("square of no is:",n*n)
        
begintime=time.time()

t1=Thread(target=getDoubleofNo,args=(numbers,))
t2=Thread(target=getSquareofNo,args=(numbers,))

t1.start()
t2.start()

t1.join()  # main thread should wait until the child thread gets executed
t2.join()

endtime=time.time()

print("total time taken is:", endtime-begintime)


# In[39]:


# changing or setting the names of the python thread (getName() and setName() function)

import threading

print(current_thread().getName())

current_thread().setName("Salman Khan")

print(current_thread().getName())


# In[40]:


import threading

def Demo():
    print("child thread")
    
t1=Thread(target=Demo)
t1.start()

print("main thread identification is:",current_thread().ident)
print("child thread identification is:",t1.ident)


# In[43]:


#active_count()

import threading
import time

def display():
    print(current_thread().name,".........started")
    time.sleep(3)
    print(current_thread().name,".........ended")
    
print("the no of active thread are",active_count())

t1=Thread(target=display,name="Child Thread1")
t2=Thread(target=display,name="Child Thread2")
t3=Thread(target=display,name="Child Thread3")

t1.start()
t2.start()
t3.start()

print("the no of active thread are",active_count())


# In[45]:


import threading
import time

def display():
    print(current_thread().name,".........started")
    time.sleep(3)
    print(current_thread().name,".........ended")
    
print("the no of active thread are",active_count())

t1=Thread(target=display,name="Child Thread1")
t2=Thread(target=display,name="Child Thread2")
t3=Thread(target=display,name="Child Thread3")

t1.start()
t2.start()
t3.start()

time.sleep(10)  # since we have marked a sleep time as 10 seconds all our child threads will complete 
                # before the count is checked

print("the no of active thread are",active_count())


# In[46]:


#enumerate() - get all active thred info

import threading
import time

def display():
    print(current_thread().name,".........started")
    time.sleep(3)
    print(current_thread().name,".........ended")
    
print("the no of active thread are",active_count())

t1=Thread(target=display,name="Child Thread1")
t2=Thread(target=display,name="Child Thread2")
t3=Thread(target=display,name="Child Thread3")

t1.start()
t2.start()
t3.start()

list1=enumerate()  #get all active thred info

for t in list1:
    print("thread name is:",t.name)
    print("thread id is:",t.ident)

time.sleep(10)  # since we have marked a sleep time as 10 seconds all our child threads will complete 
                # before the count is checked

print("the no of active thread are",active_count())


# In[50]:


#isAlive - to check the thread is alive or dead

import threading
import time

def display():
    print(current_thread().name,".........started")
    time.sleep(3)
    print(current_thread().name,".........ended")
    
print("the no of active thread are",active_count())

t1=Thread(target=display,name="Child Thread1")
t2=Thread(target=display,name="Child Thread2")
t3=Thread(target=display,name="Child Thread3")

t1.start()
t2.start()
t3.start()

list1=enumerate()  #get all active thred info

print(t1.name,"is Alive:",t1.isAlive())
print(t2.name,"is Alive:",t2.isAlive())

for t in list1:
    print("thread name is:",t.name)
    print("thread id is:",t.ident)

time.sleep(10)  # since we have marked a sleep time as 10 seconds all our child threads will complete 
                # before the count is checked
    
print(t1.name,"is Alive:",t1.isAlive())
print(t2.name,"is Alive:",t2.isAlive())

print("the no of active thread are",active_count())


# In[51]:


import threading
import time

def display():
    for x in range(10):
        print("GF Thread")
        time.sleep(3)
    
t1=Thread(target=display)
t1.start()

t1.join()

for y in range(10):
    print("BF Thread")


# In[52]:


import threading
import time

def display():
    for x in range(10):
        print("GF Thread")
        time.sleep(3)
    
t1=Thread(target=display)
t1.start()

t1.join(10)

for y in range(10):
    print("BF Thread")


# In[58]:


# Deamon Thread - thread running in background
# purpose - to provide support for non-deamon thread -ex GC

import threading

mt=current_thread()
print(mt.daemon)
print(mt.isDaemon())


# In[60]:


# to make a thread a deamon thread
# rule to make a thread a deamon - after start (active thread) cant change

import threading

mt=current_thread()
print(mt.daemon)
print(mt.isDaemon())

print("**********")
mt.setDaemon(True)    #main thread is started so cant change the main to daemon

# main thread can not set to daemon its by default non-daemon and started by python VM only

print(mt.daemon)
print(mt.isDaemon())


# In[61]:


# Daemon status gets from parent to child

# if parent is daemon then child is daemon and if parent is non-daemon(active) then child also will 
# be non-daemon

# by default the new created thread will be as parent thread only


# In[62]:


import threading

def work1():
    print("executed by the child thread")
    
t1=Thread(target=work1)  # created by main so by default it will be non daemon because the main threadis 
                         # non-deamon

print(t1.daemon)

t1.setDaemon(True)
print(t1.daemon)


# In[64]:


import threading

def work1():
    print("executed by the t1 thread")
    t2=Thread(target=work2)   #t2 is started by t1 so parent of t2 is t1
    print("********")
    print("t2 is daemon before??..",t2.isDaemon())
    t2.setDaemon(False)
    print("t2 is daemon before??..",t2.isDaemon())
    t2.start()
    
def work2():
    print("executed by the child thread")
    
t1=Thread(target=work1)  # created by main so non daemon 

print(t1.daemon)

t1.setDaemon(True)

print(t1.daemon)

t1.start()


# In[65]:


# whenever last non-daemon thread terminates then all daemon thread also terminates automatically

# daemon thread is required until non-daemon thread executes its supports the main thread from backround

# the background activity are done by daemon threads but main activity are done by non-daemon threads


# In[68]:


import threading
import time

def work1():
    for x in range(10):
        time.sleep(2)
        print("child thread execution")
        
t1=Thread(target=work1)
t1.start()
time.sleep(10)
print("main thread executes end")


# In[70]:


import threading
import time

def work1():
    for x in range(10):
        time.sleep(2)
        print("child thread execution")
        
t1=Thread(target=work1)
t1.setDaemon(True)
t1.start()
time.sleep(10)
print("main thread executes end")


# In[ ]:




