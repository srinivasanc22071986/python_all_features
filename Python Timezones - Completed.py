#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pytz

for tz in pytz.all_timezones:
     print(tz)


# In[24]:


from datetime import datetime,timedelta
import pytz

#ind_NY = pytz.timezone('Asia/Kolkata')
dt1 = datetime.now()
dt2 = dt1 + timedelta(hours=5) + timedelta(minutes=30)
print(dt1)
print(dt2)


# In[22]:


dir(pytz.all_timezones)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




