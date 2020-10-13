#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Difference between console and local files

# Python have function for creating, reading, updating and deleting files.

'''

open () function in Python to open a file in read or write mode.

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists


Mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images, audio, video)

'''


# In[15]:


file1 = open("/home/sriniintraining/kotak courier","r")

#file1.write("Srinivasan is a good person")

#file1.close()



print(file1.read(5))    # Prints the path of the file and also gives the mode and the encoding format

#file1.close()


# In[16]:


file1 = open("/home/sriniintraining/skillsoft id","w")

file1.write("Srinivasan is a fantastic person")

file1.close()

#print(file1.read()) # Prints all the contents of the file


# In[17]:


file1 = open("/home/sriniintraining/skillsoft id","r")

print(file1.read(6)) # Prints the first 6 characters of the file


# In[18]:


file1 = open("/home/sriniintraining/kotak courier","r") 

for i in file1:
    print(i)          # Prints all the contents of the file through a for loop 


# In[29]:


file1 = open("/home/sriniintraining/kotak courier","r") 

print(file1.readlines(50)) # Prints the contents of the first line of the file
print(file1.readline(5)) # Prints the contents of the first line of the file
print(file1.readline(2)) # Prints the contents of the first line of the file
print(file1.readline(5)) # Prints the contents of the first line of the file
print(file1.readline(7)) # Prints the contents of the first line of the file
print(file1.readline(2)) # Prints the contents of the first line of the file
print(file1.readline(7)) # Prints the contents of the first line of the file


# In[20]:


file1 = open("/home/sriniintraining/kotak courier","r") 

print(file1.readline()) # Prints the first 6 characters of the first line of the file


# In[21]:


file1 = open("/home/sriniintraining/kotak courier","r") 

print(file1.readline()) # Prints the contents of the first line of the file

print(file1.readline()) # Prints the contents of the second line of the file

print(file1.readline()) # Prints the contents of the third line of the file

print(file1.readline()) # Prints the contents of the fourth line of the file

print(file1.readline()) # Prints the contents of the fifth line of the file

print(file1.readline()) # Prints the contents of the sixth line of the file

print(file1.readline()) # Prints the contents of the seventh line of the file

print(file1.readline()) # Prints the contents of the eight line of the file

print(file1.readline()) # Prints the contents of the ninth line of the file


# In[23]:


file1 = open("/home/sriniintraining/kotak courier","r") 

String1 = "This is 1st line."

print(len(String1))       # The length of the string is 17 characters 

print(file1.readline(7))  # Prints the first 7 characters of the first line of the file
print(file1.readline(10)) # Prints the remaining 10 characters of the first line of the file
print(file1.readline(17)) # Prints a space might be a "\n" character
print(file1.readline(17)) # Prints the contents of the second line of the file
print(file1.readline(17)) # Prints a space might be a "\n" character
print(file1.readline(17)) # Prints the contents of the third line of the file
print(file1.readline(17)) # Prints a space might be a "\n" character
print(file1.readline(17)) # Prints the contents of the forth line of the file
print(file1.readline(17)) # Prints a space might be a "\n" character
print(file1.readline(17)) # Prints the contents of the fifth line of the file
print(file1.readline(17)) # Prints a space might be a "\n" character
print(file1.readline(17)) # Prints the contents of the sixth line of the file
print(file1.readline(17)) # Prints a space might be a "\n" character
print(file1.readline(17)) # Prints the contents of the seventh line of the file
print(file1.readline(17)) # Prints a space might be a "\n" character
print(file1.readline(17)) # Prints the contents of the eight line of the file
print(file1.readline(17)) # Prints a space might be a "\n" character
print(file1.readline(17)) # Prints the contents of the ninth line of the file


# In[10]:


file1 = open("/home/sriniintraining/kotak courier","r") 

String1 = "This is 1st line."

print(len(String1))       # The length of the string is 17 characters 

print(file1.readline(7))  # Prints the first 6 characters of the first line of the file
print(file1.readline(11)) # Prints the remaining 11 characters of the first line of the file including 
                          # space or "\n" at the end
print(file1.readline(18)) # Prints the contents of the second line of the file including 
                          # space or "\n" at the end
print(file1.readline(18)) # Prints the contents of the third line of the file including 
                          # space or "\n" at the end
print(file1.readline(18)) # Prints the contents of the forth line of the file including 
                          # space or "\n" at the end
print(file1.readline(18)) # Prints the contents of the fifth line of the file including 
                          # space or "\n" at the end
print(file1.readline(18)) # Prints the contents of the sixth line of the file including 
                          # space or "\n" at the end
print(file1.readline(18)) # Prints the contents of the seventh line of the file including 
                          # space or "\n" at the end
print(file1.readline(18)) # Prints the contents of the eight line of the file including 
                          # space or "\n" at the end
print(file1.readline(18)) # Prints the contents of the ninth line of the file including 
                          # space or "\n" at the end


# In[11]:


file1 = open("/home/sriniintraining/kotak courier","r") 

print(file1.read()) # Prints all the contents of the file


# In[12]:


file1 = open("/home/sriniintraining/kotak courier1","r") # First check the length and then the type

print(len(file1.readline()))  # Returns the length of the contents of the first line of the file
print(len(file1.readline()))  # Returns the length of the contents of the second line of the file
print(len(file1.readline()))  # Returns the length of the contents of the first line of the file
print(len(file1.readline()))  # Returns the length of the contents of the second line of the file
print(len(file1.readline()))  # Returns the length of the contents of the first line of the file
print(len(file1.readline()))  # Returns the length of the contents of the second line of the file
print(len(file1.readline()))  # Returns the length of the contents of the second line of the file
print(len(file1.readline()))  # Returns the length of the contents of the second line of the file
print(len(file1.readline()))  # Returns the length of the contents of the second line of the file
print(type(file1.readline())) # Returns the type of the contents of the first line of the file
print(type(file1.readline())) # Returns the type of the contents of the second line of the file


# In[32]:


file1 = open("/home/sriniintraining/kotak courier","r") 

print(file1.readlines()) # Returns the contents of all the lines of a file as a list


# In[4]:


file1 = open("/home/sriniintraining/kotak courier","r")

String1 = "This is 1st line."

print(len(String1))       # The length of the string is 17 characters 

print(file1.readlines(17)) 

print(file1.readlines(34)) 

#print(file1.readlines(51)) 

#print(file1.readlines(68)) 

#print(file1.readlines(85)) 

#print(file1.readlines(102)) 

#print(file1.readlines(119)) 

#print(file1.readlines(136)) 

#print(file1.readlines(153)) 

#This is 1st line. - Size is 17

#This is 2nd line. - Size is 17 - Total 34 - readlines(34)

#This is 3rd line. - Size is 17 - Total 51 - readlines(51)

#This is 4th line. - Size is 17 - Total 68 - readlines(68)

#This is 5th line. - Size is 17 - Total 85 - readlines(85)

#This is 6th line. - Size is 17 - Total 102 - readlines(102)

#This is 7th line. - Size is 17 - Total 119 - readlines(119)

#This is 8th line. - Size is 17 - Total 136 - readlines(136)

#This is 9th line. - Size is 17 - Total 153 - readlines(153)


# In[15]:


file1 = open("/home/sriniintraining/kotak courier","r") 

print(len(file1.readlines()))  # Returns the length of the contents of the first line of the file

print(type(file1.readlines())) # Returns the type of the contents of the first line of the file


# In[33]:


file1 = open("/home/sriniintraining/kotak courier write","a")  # Entries are written in the second run 
                                                               # without flush and close

file1.write("Srinivasan is a hero append\n")

file1.write("Srinivasan is a hero append\n")

file1.write("Srinivasan is a hero append\n")

file1.write("Srinivasan is a hero append\n")

#file1.flush()

file1.close()


# In[49]:


file2 = open("/home/sriniintraining/kotak courier write1","w")   # Entries are written in the second run
                                                                 # without flush and close

file2.write("Srinivasan is a hero write\n")

file2.write("Srinivasan is a hero write\n")

file2.write("Srinivasan is a hero write\n")

file2.write("Srinivasan is a hero write\n")

#file2.flush()

file2.close()


# In[52]:


file3 = open("/home/sriniintraining/kotak courier write2","r")   

content = file3.readline()

print(content)

print(type(content))


# In[37]:


file_list = ['This is line1.\n', 'This is line2.\n', 'This is line3.\n', 'This is line4.\n', 'This is line5.\n', 'This is line6.\n', 'This is line7.\n', 'This is line8.\n']

file4 = open("/home/sriniintraining/kotak courier write","w")   

print(file4.writelines(file_list))

file4.close()


# In[65]:


file5 = open("/home/sriniintraining/kotak courier write4","w")  

file5.write("Hi Srinivasan Good Morning\n")

file5.write("Hi Srinivasan Good Afternoon\n")

file5.write("Hi Srinivasan Good Evening\n")

file5.write("Hi Srinivasan Good Night\n")

file5.flush()

file5.close()


# In[67]:


file6 = open("/home/sriniintraining/kotak courier write4","a")  

file6.write("Hi Srinivasan Bad Morning\n")

file6.write("Hi Srinivasan Bad Afternoon\n")

file6.write("Hi Srinivasan Bad Evening\n")

file6.write("Hi Srinivasan Bad Night\n")

file6.flush()

file6.close()


# In[35]:


file7 = open("/home/sriniintraining/kotak courier write","r")  

print(file7.tell())

print(file7.readlines())

print(file7.tell())


# In[40]:


file8 = open("/home/sriniintraining/kotak courier write","r")  

print(file8.tell())

print(file8.readlines())

print(file8.tell())

file8.seek(200)

print(file8.tell())

print(file8.readlines())

print(file8.tell())


# In[41]:


# OS Module - to perform Operating Systems dependent oprations such  as making a folder, listing contents of a folder, know about a process, end a process etc

import os

os.rename("/home/sriniintraining/kotak courier write","/home/sriniintraining/kotak courier wri4")


# In[75]:


os.remove("/home/sriniintraining/kotak courier wri") # This will permanently delete the file


# In[47]:


os.removedirs("/home/sriniintraining/hi1/sri1/33") # This will permanently delete only the empty folders


# In[45]:


os.mkdir("/home/sriniintraining/hi1/sri1/33") # This will create the folder


# In[43]:


os.makedirs("/home/sriniintraining/hi1/sri1/1/2/3/4/5/6/7/8/9") # This will create the folders within folders in the same order


# In[84]:


print(os.getcwd()) # This will tell the current working directory


# In[ ]:


# dont execute in thismachine
# os.chdir("new working directory name")


# In[85]:


dir(os)


# In[86]:


print(os.path.getsize("/home/sriniintraining/hi1/sri1/1/2/3/4/5/6/7/8/9"))


# In[89]:


print(os.listdir("/home/sriniintraining/hi/sri"))


# In[90]:


print(os.path.isfile("/home/sriniintraining/hi/sri/1/kotak courier write"))


# In[91]:


print(os.path.isfile("/home/sriniintraining/hi/sri/1"))


# In[92]:


print(os.path.isdir("/home/sriniintraining/hi/sri/1"))


# In[93]:


print(os.path.isdir("/home/sriniintraining/hi/sri/1/kotak courier write3"))


# In[ ]:




