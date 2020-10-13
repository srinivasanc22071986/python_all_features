#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Logging example

# advantage of logging - track purpose, perform debugging and get RCA(Root Cause Analysis)

# Logging Levels - waht type of information we are going to store in logging file

# 1.CRITICAL(50) (Needs High Attention)

# 2.ERROR - (40) 

# 3.WARNING(30) - represent the warning message (Default Level Warning and its higher level will display)

# 4.INFO(20)

# 5.DEBUG(10) (if  we set DEBUG then all type of message will display)

# 6.NOTSET(0)


# In[2]:


# Implement Logging - 

# step1 - create a log file

# step2 - which level of logging we need to keep


# In[6]:


import logging

logging.basicConfig(filename="/home/sriniintraining/Desktop/test1",level=logging.WARNING,filemode='w')

print("Logging Module Demo")

logging.debug("Debugging information")
logging.info("Info information")
logging.warning("Warning information")
logging.error("Error information")
logging.critical("Critical information")


# In[8]:


import logging

logging.basicConfig(filename="/home/sriniintraining/Desktop/test1",level=logging.WARNING,filemode='w',
                    format='%(levelname)s')

print("Logging Module Demo")

logging.debug("Debugging information")
logging.info("Info information")
logging.warning("Warning information")
logging.error("Error information")
logging.critical("Critical information")


# In[10]:


import logging

logging.basicConfig(filename="/home/sriniintraining/Desktop/test1",level=logging.WARNING,filemode='w',
                    format='%(levelname)s:%(messsage)s')

print("Logging Module Demo")

logging.debug("Debugging information")
logging.info("Info information")
logging.warning("Warning information")
logging.error("Error information")
logging.critical("Critical information")


# In[11]:


import logging

logging.basicConfig(filename="/home/sriniintraining/Desktop/test1",level=logging.WARNING,filemode='w',
                    format='%(asctime)s:%(levelname)s:%(messsage)s')

print("Logging Module Demo")

logging.debug("Debugging information")
logging.info("Info information")
logging.warning("Warning information")
logging.error("Error information")
logging.critical("Critical information")


# In[12]:


import logging

logging.basicConfig(filename="/home/sriniintraining/Desktop/test1",level=logging.WARNING,filemode='w',
                    format='%(asctime)s:%(levelname)s:%(messsage)s,datefmt='%d/%m/%y %H:%M:%S %p')

print("Logging Module Demo")

logging.debug("Debugging information")
logging.info("Info information")
logging.warning("Warning information")
logging.error("Error information")
logging.critical("Critical information")  


# In[ ]:




