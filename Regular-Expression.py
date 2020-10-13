#!/usr/bin/env python
# coding: utf-8

# In[1]:


# regular expressions examples - mobile,email ids

# to represent to the group of things whcih follows a particular pattern

# 1.Validations 2.Finidng a word in note pad (ctrl+f) or linux command like grep, find

# 3.to check the syntax in compiler

# re module is used for the regular expression

# ************************************

# finding some word

# step1 - create a Regex(regular expression object)

# step2 - create a matcher object


# In[11]:


import re
count=0
pattern1=re.compile("language")

print(type(pattern1))

matcher=pattern1.finditer("python is a programming language and this language is easy to study")

print(matcher)

for match in matcher:
    print(match)
    count+=1
    print("match is avalable at....",match.start())
print("no of occurance is....",count)   


# In[12]:


import re
count=0
pattern1=re.compile("java")

print(type(pattern1))

matcher=pattern1.finditer("python is a programming language and this language is easy to study")

print(matcher)

for match in matcher:
    print(match)
    count+=1
    print("match is avalable at....",match.start())
print("no of occurance is....",count)   


# In[13]:


import re
count=0
pattern1=re.compile("language")

print(type(pattern1))

matcher=pattern1.finditer("python is a programming language and this language is easy to study")

print(matcher)

for match in matcher:
    print(match)
    count+=1
    print("match is avalable at....",match.start())
    print("match is avalable at....",match.end())
    print("match is avalable at....",match.group())
print("no of occurance is....",count)  


# In[14]:


import re
count=0
matcher=re.finditer("language","python is a programming language and this language is easy to study")

print(matcher)

for match in matcher:
    print(match)
    count+=1
    print("match is avalable at....",match.start())
    print("match is avalable at....",match.end())
    print("match is avalable at....",match.group())
print("no of occurance is....",count) 


# In[15]:


# seraching of group like any digit or any alphabet

'''

1.[abc]        -> will search for either a or b or c
2.[^abc]       -> will search for characters except a,b,c
3.[a-z]        -> will search for alphabet a to z
4.[A-Z]        -> will search for alphabet A to Z
5.[0-9]        -> will search for digit 0-9
6.[a-zA-Z]     -> will search for alphabet a to z and A to Z
7.[a-zA-Z0-9]  -> will search for alphabet a to z, A to Z and 0 to 9
8.[^a-zA-Z0-9] -> will search for characters except a to z, A to Z and 0 to 9

'''


# In[41]:


import re

matcher1=re.finditer('[abc]','a78b@9kuio')  # returns the positions of the character a and b and c

matcher2=re.finditer('[^abc]','a78b@9kuio') # returns the positions of all the character except a and b and c  

matcher3=re.finditer('[a-z]','a78b@9kuio')  # returns the positions of all the character from a to z

matcher4=re.finditer('[A-Z]','a78bB@9kKuUiIoO')   # returns the positions of all the character from A to Z

matcher5=re.finditer('[0-9]','a78b@9kuio')  # returns the positions of all the character from 0 to 9 

matcher6=re.finditer('[a-zA-Z]','a78bB@9kKuUiIoO') # returns the positions of all the character from a to z and A to Z

matcher7=re.finditer('[a-zA-Z0-9]','a78bB@9kKuUiIoO') # returns the positions of all the character from a to z,A to Z and 0 to 9

matcher8=re.finditer('[^a-zA-Z0-9]','@a78b@9kuio') # returns the positions of all the character except a to z,A to Z and 0 to 9

for m1 in matcher1:
    print(m1)
    print(m1.start(),",",m1.end(),"********",m1.group())
    
print("****************************************")
    
for m2 in matcher2:
    print(m2)
    print(m2.start(),",",m2.end(),"********",m2.group())
    
print("****************************************")
    
for m3 in matcher3:
    print(m3)
    print(m3.start(),",",m3.end(),"********",m3.group())
    
print("****************************************")
    
for m4 in matcher4:
    print(m4)
    print(m4.start(),",",m4.end(),"********",m4.group())
    
print("****************************************")
    
for m5 in matcher5:
    print(m5)
    print(m5.start(),",",m5.end(),"********",m5.group())
    
print("****************************************")
    
for m6 in matcher6:
    print(m6)
    print(m6.start(),",",m6.end(),"********",m6.group())
    
print("****************************************")
    
for m7 in matcher7:
    print(m7)
    print(m7.start(),",",m7.end(),"********",m7.group())
    
print("****************************************")
    
for m8 in matcher8:
    print(m8)
    print(m8.start(),",",m8.end(),"********",m8.group())


# In[42]:


# seraching of group like any digit or any alphabet

'''

\s -> match space character
\S -> except space character
\d -> match any digit
\D -> except any digit 
\w -> any word character(alphanumeric) 
\W -> except any word character(alphanumeric)(like special character)
.  -> any character including alphanumeric and special character

'''


# In[54]:


import re

matcher1=re.finditer('\s','a78 b@9kuio')  # match space character

matcher2=re.finditer('\S','a78b@9kuio') # match except space character

matcher3=re.finditer('\d','a78b@9kuio')  # match any digit

matcher4=re.finditer('\D','a78bB@9kKuUiIoO')   # match except any digit

matcher5=re.finditer('\w','a78b@9kuio')  # match any word character(alphanumeric) not special character 

matcher6=re.finditer('\W','a78bB@9kKuUiIoO') # match except any word character(alphanumeric)(like special character)

matcher7=re.finditer('.','a78bB@9kKuUiIoO') # match any character including alphanumeric and special character

for m1 in matcher1:
    print(m1)
    print(m1.start(),",",m1.end(),"********",m1.group())
    
print("****************************************")
    
for m2 in matcher2:
    print(m2)
    print(m2.start(),",",m2.end(),"********",m2.group())
    
print("****************************************")
    
for m3 in matcher3:
    print(m3)
    print(m3.start(),",",m3.end(),"********",m3.group())
    
print("****************************************")
    
for m4 in matcher4:
    print(m4)
    print(m4.start(),",",m4.end(),"********",m4.group())
    
print("****************************************")
    
for m5 in matcher5:
    print(m5)
    print(m5.start(),",",m5.end(),"********",m5.group())
    
print("****************************************")
    
for m6 in matcher6:
    print(m6)
    print(m6.start(),",",m6.end(),"********",m6.group())
    
print("****************************************")
    
for m7 in matcher7:
    print(m7)
    print(m7.start(),",",m7.end(),"********",m7.group())


# In[55]:


# seraching of group like any digit or any alphabet

'''

a      -> matching only one a
a+     -> either one a or more than one a (like 2a(aa) or 3a(aaa))(atleast 1a(a))
a*     -> any no of a(including zero no of a also)
a?     -> atmost either 1a(a) or zero a(no a)
a{3}   -> repetitive 3a(aaa)
a{m,n} -> minimum value m of a and maximum value of a
^a     -> whether target string starts with a are not
a$     -> whether target string ends with a are not 
[^a]   -> except a all remaining

'''


# In[92]:


import re

#matcher1=re.finditer('a','a78b@9akauiao')      # matching only one a throughout the string 

#matcher2=re.finditer('a+','a78baa@9kaaauio')   # either one a or more than one a (like 2a(aa) or 
                                                # 3a(aaa))(atleast 1a(a))

#matcher3=re.finditer('a*','a78bBa@9kKauUiIoO')    # any no of a(including zero no of a also)checks character a in all 
                                                # positions

#matcher4=re.finditer('a?','a78bBa@9kKauUiIoO')   # atmost either 1a(a) or zero a(no a) same as 'a*'

#matcher5=re.finditer('a{3}','a78baaa@9kuio')      # repetitive 3a(aaa) - returns the position of aaa 

#matcher6=re.finditer('a{2,4}','a78baaB@9aaakKaaaaauUiIoO') # minimum value m of a and maximum 
                                                            # value of a(checks aa, aaa, aaaa)

#matcher7=re.finditer('^a','a78bB@9kKuUiIoO')   # whether target string starts with a are not

#matcher8=re.finditer('a$','a78bB@9kKuUiIoOa')   # whether target string ends with a are not 

matcher9=re.finditer('[^a]','a78bBaaa@9kaaaaKuUiIoO') # except a all remaining

for m1 in matcher1:
    print(m1)
    print(m1.start(),",",m1.end(),"********",m1.group())
    
#print("****************************************")
    
for m2 in matcher2:
    print(m2)
    print(m2.start(),",",m2.end(),"********",m2.group())
    
#print("****************************************")
    
for m3 in matcher3:
    print(m3)
    print(m3.start(),",",m3.end(),"********",m3.group())
    
#print("****************************************")
    
for m4 in matcher4:
    print(m4)
    print(m4.start(),",",m4.end(),"********",m4.group())
    
#print("****************************************")
    
for m5 in matcher5:
    print(m5)
    print(m5.start(),",",m5.end(),"********",m5.group())
    
#print("****************************************")
    
for m6 in matcher6:
    print(m6)
    print(m6.start(),",",m6.end(),"********",m6.group())
    
#print("****************************************")
    
for m7 in matcher7:
    print(m7)
    print(m7.start(),",",m7.end(),"********",m7.group())
    
#print("****************************************")
    
for m8 in matcher8:
    print(m8)
    print(m8.start(),",",m8.end(),"********",m8.group())
    
#print("****************************************")
    
for m9 in matcher9:
    print(m9)
    print(m9.start(),",",m9.end(),"********",m9.group())


# In[93]:


'''

1.match()      -> to check the given pattern is at begining of target string are not
2.fullmatch()  -> complete string should match with the target string
3.search()     -> searching of given pattern
4.findall()    -> returns a list of matched element 
5.finditer()   -> returns the matched iterator 
6.sub()        -> substitution or replacement (Ctrl+H command) - search and replace
7.subn()       -> it replace and tells how many replacement happened
8.split()      -> split the string based on some pattern
9.compile()    -> 

'''


# In[104]:


import re

s=input("enter the pattern to check??")

m=re.match(s,"abcdefghabz")

if m!=None:
    print("match is avaiable from",m.start(),"to",m.end())
else:
    print("Match is not available")      


# In[99]:


import re

s=input("enter the pattern to check??")

m=re.fullmatch(s,"abcdefghabz")

if m!=None:
    print("match is avaiable from",m.start(),"to",m.end())
else:
    print("Match is not available")   


# In[101]:


import re

s=input("enter the pattern to check??")

m=re.search(s,"abcdefghabz")   #searches a character in the given string

if m!=None:
    print("match is avaiable from",m.start(),"to",m.end())
else:
    print("Match is not available")   


# In[108]:


import re

m=re.findall("[0-9]","abc2587def545679ghabz")   #returns a list to denote all the found values

print("match is avaiable from",m)


# In[109]:


import re

m=re.sub("[0-9]","$","abc2587def545679ghabz") #where the digit is replaced with $

print("replaced string :",m)


# In[110]:


import re

m=re.subn("[0-9]","$","abc2587def545679ghabz") #where the digit is replaced with $

print("replaced :",m)


# In[112]:


import re

m=re.split("-","56-32-6jh-s8y-uteu-*4-9") 

print("splitted :",m)


# In[113]:


'''

define a RE for the following rules:

1.first character must be alphabet and from d to t only

2.second character should be any digit divisible by 5

3.the length must be atleast 2.

'''


# In[115]:


import re

expression1=input("please enter the expression you want to match?")

m=re.fullmatch("[d-t][05][a-zA-Z0-9#]*", expression1)

if m!=None:
    print("the expression is matching")
else:
    print("the expression is not matching")   


# In[1]:


# check if a green mobile no is valid or not

# first digit must be 6 or 7 or 8 or 9

# [6789][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9] or [6789]\d{9}


import re

mob_no=input("please enter the number to be checked whether mobile no is valid are not?")

m=re.fullmatch("[6789]\d{9}", mob_no)

if m!=None:
    print("the mobile number is valid")
else:
    print("the mobile number is not valid") 


# In[4]:


# reading the mobile number from the file and store in another file

import re

f1=open("/home/sriniintraining/Desktop/test1.txt","r")
f2=open("/home/sriniintraining/Desktop/test2.txt","w")

for line in f1:
    list=re.findall("[7-9]\d{9}",line)
    print(list)
    for n in list:
        f2.write(n+"\n")
        
print("Extracted all mobile numbers into test2.txt")


# In[2]:


# to check a given gmail id is valid are not

import re

email_id=input("please enter the email id to be checked is valid are not?")

m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", email_id)

if m!=None:
    print("the email id is valid")
else:
    print("the email id is not valid") 


# In[7]:


# to check a given mail id is valid are not

import re

email_id=input("please enter the email id to be checked is valid are not?")

m=re.fullmatch("\w[a-zA-Z0-9_.]*@[a-z0-9]+[.][a-z]+[.][a-z]+", email_id)

if m!=None:
    print("the email id is valid")
else:
    print("the email id is not valid") 


# In[5]:


# to check a given vehicle registration is valid are not

import re

reg_no=input("please enter the vehicle number id to be checked is valid are not?")

m=re.fullmatch("KA[0-7][0-9][A-Z][A-Z]\d{4}", reg_no)

if m!=None:
    print("the regno id is valid")
else:
    print("the regno id is not valid") 


# In[4]:


a = 10
b = 10

print(a | b)
print(a or b)
print(a & b)
print(a and b)


# In[8]:


a = {1,2,3,4,5,6}
b = {2,4,6,8,10}

print(a.union(b))

print(a & b)

print(a.intersection(b))

print(a | b)


# In[22]:


def hi(l):
    for i in range(0,l):
        yield(i)
        #print("Bye",i)
        
for i in hi(5):
    print("Hi",i)      


# In[ ]:




