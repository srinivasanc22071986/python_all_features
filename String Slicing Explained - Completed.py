#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Splicing Direction : Forward 
#
# (+00)-->(+01)-->(+02)-->(+03)-->(+04)-->(+05)-->(+06)-->(+07)-->(+08)-->(+09)-->(+10)-->(+11)-->(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Slicing Direction>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||  
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||       
# (-13)-->(-12)-->(-11)-->(-10)-->(-09)-->(-08)-->(-07)-->(-06)-->(-05)-->(-04)-->(-03)-->(-02)-->(-01)

# ******************************************************************************************************

# Splicing Direction : Reverse
#
# (+00)<--(+01)<--(+02)<--(+03)<--(+04)<--(+05)<--(+06)<--(+07)<--(+08)<--(+09)<--(+10)<--(+11)<--(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     ||| 
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Slicing Direction<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||   
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||                                                                                             |       
# (-13)<--(-12)<--(-11)<--(-10)<--(-09)<--(-08)<--(-07)<--(-06)<--(-05)<--(-04)<--(-03)<--(-02)<--(-01)


# In[29]:


sample_str = 'Python String'

# Slicing Direction : Forward
#
# (+00)-->(+01)-->(+02)-->(+03)-->(+04)-->(+05)-->(+06)-->(+07)-->(+08)-->(+09)-->(+10)-->(+11)-->(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --P------>y------>t------>h------>o------>n------> >----->S------>t------>r------>i------>n------>g--
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||  
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||       
# (-13)-->(-12)-->(-11)-->(-10)-->(-09)-->(-08)-->(-07)-->(-06)-->(-05)-->(-04)-->(-03)-->(-02)-->(-01)

# *****************************************************************************************************

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

print("****************************************************************************************************")

# Slicing Direction : Forward
#
# (+00)-->(+01)-->(+02)-->(+03)-->(+04)-->(+05)-->(+06)-->(+07)-->(+08)-->(+09)-->(+10)-->(+11)-->(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --P------>y------>t------>h------>o------>n------> >----->S------>t------>r------>i------>n------>g--
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||  
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||       
# (-13)-->(-12)-->(-11)-->(-10)-->(-09)-->(-08)-->(-07)-->(-06)-->(-05)-->(-04)-->(-03)-->(-02)-->(-01)
      
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


# In[30]:


sample_str = 'Python String'

# Slicing Direction : Forward
#
# (+00)-->(+01)-->(+02)-->(+03)-->(+04)-->(+05)-->(+06)-->(+07)-->(+08)-->(+09)-->(+10)-->(+11)-->(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --P------>y------>t------>h------>o------>n------> >----->S------>t------>r------>i------>n------>g--
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||  
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||       
# (-13)-->(-12)-->(-11)-->(-10)-->(-09)-->(-08)-->(-07)-->(-06)-->(-05)-->(-04)-->(-03)-->(-02)-->(-01)

# *****************************************************************************************************

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


# In[31]:


sample_str = 'Python String'

# Slicing Direction : Reverse
#
# (+00)<--(+01)<--(+02)<--(+03)<--(+04)<--(+05)<--(+06)<--(+07)<--(+08)<--(+09)<--(+10)<--(+11)<--(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     ||| 
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# --P<------y<------t<------h<------o<------n<-----< <------S<------t<------r<------i<------n<------g-- 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||   
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||                                                                                             |       
# (-13)<--(-12)<--(-11)<--(-10)<--(-09)<--(-08)<--(-07)<--(-06)<--(-05)<--(-04)<--(-03)<--(-02)<--(-01)

# *****************************************************************************************************

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


# In[43]:


sample_str = 'Python String'

# Slicing Direction : Reverse
#
# (+00)<--(+01)<--(+02)<--(+03)<--(+04)<--(+05)<--(+06)<--(+07)<--(+08)<--(+09)<--(+10)<--(+11)<--(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     ||| 
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# --P<------y<------t<------h<------o<------n<-----< <------S<------t<------r<------i<------n<------g-- 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||   
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||                                                                                             |       
# (-13)<--(-12)<--(-11)<--(-10)<--(-09)<--(-08)<--(-07)<--(-06)<--(-05)<--(-04)<--(-03)<--(-02)<--(-01)

# *****************************************************************************************************

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

print("*************************************************************")

print("sample_str[-13:00:-1] : ",sample_str[-13:0:-1]) 
print("sample_str[-13:01:-1] : ",sample_str[-13:1:-1]) 
print("sample_str[-13:02:-1] : ",sample_str[-13:2:-1]) 
print("sample_str[-13:03:-1] : ",sample_str[-13:3:-1]) 
print("sample_str[-13:04:-1] : ",sample_str[-13:4:-1]) 
print("sample_str[-13:05:-1] : ",sample_str[-13:5:-1]) 
print("sample_str[-13:06:-1] : ",sample_str[-13:6:-1]) 
print("sample_str[-13:07:-1] : ",sample_str[-13:7:-1]) 
print("sample_str[-13:08:-1] : ",sample_str[-13:8:-1]) 
print("sample_str[-13:09:-1] : ",sample_str[-13:9:-1]) 
print("sample_str[-13:10:-1] : ",sample_str[-13:10:-1]) 
print("sample_str[-13:11:-1] : ",sample_str[-13:11:-1]) 
print("sample_str[-13:12:-1] : ",sample_str[-13:12:-1])


# In[44]:


sample_str = 'Python String'

# Slicing Direction : Reverse
#
# (+00)<--(+01)<--(+02)<--(+03)<--(+04)<--(+05)<--(+06)<--(+07)<--(+08)<--(+09)<--(+10)<--(+11)<--(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     ||| 
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# --P<------y<------t<------h<------o<------n<-----< <------S<------t<------r<------i<------n<------g-- 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||   
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||                                                                                             |       
# (-13)<--(-12)<--(-11)<--(-10)<--(-09)<--(-08)<--(-07)<--(-06)<--(-05)<--(-04)<--(-03)<--(-02)<--(-01)

# *****************************************************************************************************

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
print("sample_str[0:-13:-1] : ",sample_str[0:-13:-1]) 

print("*************************************************************")

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
print("sample_str[1:-13:-1] : ",sample_str[1:-13:-1])

print("*************************************************************")

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
print("sample_str[2:-13:-1] : ",sample_str[2:-13:-1]) 

print("*************************************************************")

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
print("sample_str[12:-13:-1] : ",sample_str[12:-13:-1])


# In[45]:


sample_str = 'Python String'

# Slicing Direction : Reverse
#
# (+00)<--(+01)<--(+02)<--(+03)<--(+04)<--(+05)<--(+06)<--(+07)<--(+08)<--(+09)<--(+10)<--(+11)<--(+12)
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     ||| 
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# --P<------y<------t<------h<------o<------n<-----< <------S<------t<------r<------i<------n<------g-- 
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||   
#  |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||     |||                                                                                             |       
# (-13)<--(-12)<--(-11)<--(-10)<--(-09)<--(-08)<--(-07)<--(-06)<--(-05)<--(-04)<--(-03)<--(-02)<--(-01)

# *****************************************************************************************************

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
print("sample_str[-1:-13:-1] : ",sample_str[-1:-13:-1])

print("*************************************************************")

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
print("sample_str[-2:-13:-1] : ",sample_str[-2:-13:-1])

print("*************************************************************")

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
print("sample_str[-3:-13:-1] : ",sample_str[-3:-13:-1])

print("*************************************************************")

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
print("sample_str[-4:-13:-1] : ",sample_str[-4:-13:-1])

print("*************************************************************")

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
print("sample_str[-1:-13:-1] : ",sample_str[-1:-13:-1])

print("*************************************************************")

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
print("sample_str[-6:-13:-1] : ",sample_str[-6:-13:-1])

print("*************************************************************")

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
print("sample_str[-7:-13:-1] : ",sample_str[-7:-13:-1])

print("*************************************************************")

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
print("sample_str[-8:-13:-1] : ",sample_str[-8:-13:-1])

print("*************************************************************")

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
print("sample_str[-9:-13:-1] : ",sample_str[-9:-13:-1])

print("*************************************************************")

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
print("sample_str[-10:-13:-1] : ",sample_str[-10:-13:-1])

print("*************************************************************")

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
print("sample_str[-11:-13:-1] : ",sample_str[-11:-13:-1])

print("*************************************************************")

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
print("sample_str[-12:-13:-1] : ",sample_str[-12:-13:-1])


# In[ ]:




