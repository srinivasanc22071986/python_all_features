#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Types of Storage Area - Temporary and Permanent

Permanent - File system and DataBase
 
   Advantage and disadvantage of file and DB
   
   - Processing of files (student results example)
   - More Manual work
   - Querying the data is not there
   - any one can open the files so security problmem
   - duplicate data also can be there (files automatically cant provide such support)
   
   How DB can overcome these problems??

Limitations of DB  - Youtube ,Facebook etc..(cant hold very huge information)
                   - relational db can provide support for structred data(table format)
                   
    then we go for cloud or bigdata or advanced data storage technologies.


Steps to Communicate with the database

Step1- import the database specific module
         ex- import pymysql
    
Step2-Establish the connection in program and database
     
            creating the connection object
      
           conn=dbmodule.connect("database information")
      
           database information="URl" ,username, Password
           
Step3-create Cursor Object (to get the results from db and store the data)

         cursor=con.cursor()

Step4- execute the Query

      cursor.execute("SQL QUERY")    -to execute a single query
      
      cursor.executescript("sql queries")  -to execute multiple queries seperate by ;
      
      cursor.executemany()    -execute paramaterized queries
      
Step5- Get the result

      cursor.fetchone()  -to fatch one row
      
      cursor.fetchall()  -to fatch all rows
      
      cursor.fetchmany(n)  -to fatch the n no of rows
      
Step6- Commiting the record

      con.commit()  - to commiting the record  -save to db 
      
      con.rollback()  - to make roll back to orignal state (undo)
      
      
Step7 -close the connection

       cursor.close()
       
       con.close()   

    

"""


# In[4]:


# -*- coding: utf-8 -*-
"""
   
  
  https://dev.mysql.com/downloads/file/?id=485118
  
  https://jupyter.org/install
  
  python -m pip install –upgrade pip

  pip install mysql-connector-python
  
  or 
  
  pip install mysql-connector-python
  
  
python -m pip install --upgrade pip
python -m pip install jupyter

jupyter notebook

http://localhost:8888

"""

## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

cnx = mysql.connect(user='root', password='Primesource31#',
                              host='127.0.0.1')

print("Connection established")
print(cnx)


# In[ ]:


## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import postgresql.connector as postgresql

cnx = mysql.connect(user='root', password='Primesource31#',
                              host='127.0.0.1')

print("Connection established")
print(cnx)


# In[7]:


# -*- coding: utf-8 -*-
"""

"""

import mysql.connector as mysql

# creating connection with database
conn_obj = mysql.connect(user='root', password='Primesource31#',
                              host='127.0.0.1')
print("Connection established")


#creating new database
cursor_obj = conn_obj.cursor()

cursor_obj.execute("create database testdb3")

print("database created")


#listing all the databases

cursor_obj.execute("show databases")
for x in cursor_obj:
    print("database name is :" , x)


# In[ ]:





# In[10]:


# -*- coding: utf-8 -*-
"""

"""

#connecting with a database (if db not exit then gets error)

import mysql.connector as mysql

# creating connection with database
conn_obj = mysql.connect(user='root', password='Primesource31#',
                        host='127.0.0.1',database='testdb3')

print("Connection established")


# creating a table in db

cursor_obj = conn_obj.cursor()
'''cursor_obj.execute("create table users(sno int,name varchar(90),age int )")
print("table created")'''

#insert recoreds in table

cursor_obj.execute("insert into users values(100,'James',20)")
print("record inserted in the table")
conn_obj.commit()


# In[7]:


# -*- coding: utf-8 -*-
"""

"""



import mysql.connector as mysql


conn_obj = mysql.connect(user='root', password='Primesource31#',
                        host='127.0.0.1',database='testdb')

print("Connection established")




cursor_obj = conn_obj.cursor()
cursor_obj.execute("insert into users values(100,'James',20)")


conn_obj.commit();
print("record inserted in the table")
'.'


# In[11]:


# -*- coding: utf-8 -*-
"""

"""

# executing many queries at a time

import mysql.connector as mysql


conn_obj = mysql.connect(user='root', password='Primesource31#',
                        host='127.0.0.1',database='testdb3')

print("Connection established")

cursor_obj = conn_obj.cursor()

sql="insert into users values(%s,%s,%s)"

val = [
  (100,'James',20),
  (101,'Ram',25),
  (102,'Shyam',26),
  (103,'Piter',27),
  (104,'Dev',19),
  (105,'Ram',30),
  (106,'Abbhi',23),
  (107,'Raj',34),
  (108,'Jay',39),
  (109,'Hari',12),
  (110,'Mahesh',34),
  (111,'Rakesh',67),
  (112,'Mak',34)
]

cursor_obj.executemany(sql, val)

conn_obj.commit()

print(cursor_obj.rowcount , "Rows got inserted")



# In[ ]:


# -*- coding: utf-8 -*-

# You will be able to read the database from the MySQL Workbench only after sucessfull closure of the connection
# and the cursor
"""

"""


import mysql.connector as mysql

try: 
    conn_obj = mysql.connect(user='root', password='Primesource31#',
                        host='127.0.0.1',database='testdb')

    #print(type(conn_obj))
    print("Connection established")

    cursor_obj = conn_obj.cursor()

    while True:
        uno=int(input("Enter User Sno:"))   
        uname=input("Enter User Name:")   
        uage=float(input("Enter User Age:"))   

        sql="insert into users values(%s,%s,%s)"

        cursor_obj.execute(sql,(uno,uname,uage))
        print("Record Inserted Successfully") 
        option=input("Do you want to insert one more record[Yes|No] :")  
        if option=="No":
            conn_obj.commit()   
            break

except Exception as e:
    if conn_obj:   
        conn_obj.rollback()   
        print("There is a problem with sql :",e)   
finally:
    if cursor_obj:   
        cursor_obj.close()   

    if conn_obj:   
         conn_obj.close() 


# In[5]:


# -*- coding: utf-8 -*-
"""

"""

import mysql.connector as mysql


conn_obj = mysql.connect(user='root', password='Primesource31#',
                        host='127.0.0.1',database='testdb')


cursor_obj = conn_obj.cursor()

cursor_obj.execute("select * from users")

result_obj = cursor_obj.fetchall()

#print("The data type of result object: ", print(type(result_obj)))

for result in result_obj:
  print(result)
  print("*******")


# In[6]:


# -*- coding: utf-8 -*-
"""

"""

import mysql.connector as mysql


conn_obj = mysql.connect(user='root', password='Primesource31#',
                        host='127.0.0.1',database='testdb')


cursor_obj = conn_obj.cursor()
cursor_obj.execute("select * from users")

result_obj = cursor_obj.fetchmany(4)

for result in result_obj:
  print(result)
  print("*******")


# In[7]:


# -*- coding: utf-8 -*-
"""

"""

import mysql.connector as mysql


conn_obj = mysql.connect(user='root', password='Primesource31#',
                        host='127.0.0.1',database='testdb')


cursor_obj = conn_obj.cursor()
cursor_obj.execute("select * from users")

result_obj = cursor_obj.fetchone()

for result in result_obj:
  print(result)
  print("*******")


# In[8]:


# -*- coding: utf-8 -*-
"""

"""


import mysql.connector as mysql


conn_obj = mysql.connect(user='root', password='Primesource31#',
                        host='127.0.0.1',database='testdb')


cursor_obj = conn_obj.cursor()
cursor_obj.execute("select * from users where name ='James' ")


result_obj = cursor_obj.fetchall()

for result in result_obj:
  print(result)
  print("*******")


# In[1]:


'''
===========================================================
DDL Commands(data defination langugae:create,alter,drop)
===========================================================
drop table users;
create table users(sno int,name varchar(90),age int);
desc users;
alter table users add salery int;
alter table users modify sno varchar(90);
desc users;
alter table users drop column sno;
desc users;
rename users to student;
desc student;
drop table student;
desc student;
==============================================================
DML Commands(data manupalation language:insert,update,delete)
==============================================================
drop table person;
create table person(sno int,name varchar(90),salary int);
desc person;
insert into person values(1,'ram',12000);
insert into person values(3,'ramana',15000);
insert into person values(2,'viajy',20000);
insert into person values(4,'prince',12000);
insert into person values(2,'prince',21000);
insert into person (sno,name) values(5,'abc');
insert into person (name,salary) values('abc',12000);
insert into person (salary) values(2300);
insert into person (name,salary,sno) values('abc',26,1200);
insert into person (name,salary) values('xyz',3400);
insert into person (sno,name) values(5,'abc');
insert into person (name,salary) values('abc',1200);
insert into person (salary) values(2300);
insert into person (name,salary,sno) values('abc',26,1200);
insert into person (name,salary) values('xyz',3400);
insert into person (sno) values(34);
select * from person;
update person set name='pavan' where sno=2;
select * from person;
update person set name='pavan' where sno>3;
select * from person;
update person set name='babu',salary=23000 where name='prince';
select * from person;
update person set name='babu',salary=23000 where name='ram';
select * from person;
update person set salary=30000 where name ='babu' or name='sekhar';
select * from person;
update person set name='viajy';
select * from person;
delete from person where sno<2;
select * from person;
delete from person where sno=2;
select * from person;
delete from person where sno=3 or salary=12000;
select * from person;
delete from person;
select * from person;
desc person;
=================================================================
DQL Commands(select,group by,order by)
=================================================================
drop table customer;
create table customer(sno int,name varchar(90),age int,salery int,department varchar2(90));
insert into customer values(1,'rajesh',23,10000,'hr');
insert into customer values(1,'ramana',28,12000,'hr');
insert into customer values(1,'chintu',32,6000,'hr');
insert into customer values(2,'swami',23,7000,'se');
insert into customer values(3,'peter',15,15000,'se');
insert into customer values(5,'adam',25,3000,'se');
insert into customer values(7,'ravan',29,23000,'be');
insert into customer values(4,'hitelar',20,30000,'be');
insert into customer values(6,'sinday',25,27000,'be');
insert into customer values(10,'scott',31,50000,'ce');
insert into customer values(15,'oracle',28,25000,'ce');
insert into customer values(12,'james',17,27000,'ce');
=========================================================
SelectQuery
========================================================
select * from customer;
select sno,name from customer;
select  age,sno from customer;
select name as fullname from customer;
select * from customer where age<25;
select * from customer where sno=1;
select * from customer where name='rajesh' or age=28;
select * from customer where name='rajesh' and age=23;
=======================================================
Group By
======================================================
select * from customer;
select department from customer group by department;
select department from customer where sno>4 group by department;
select * from customer;
select department from customer group by department having department='se';
==============================================================================
ORDER BY
===============================================================================

select * from customer order by age;
select * from customer order by age asc;
select * from customer order by age desc;
select sno from customer where age>25 group by sno having sno>1 order by sno;
==========================================================================
Built in functions
==========================================================================
drop table employee;
create table employee(sno int,name varchar(90),age int,salery int);
insert into employee values(1,'abc',22,12000);
insert into employee values(2,'xyz',23,8000);
insert into employee values(3,'ramana',30,30000);
insert into employee values(6,'rama',18,15000);
insert into employee values(9,'vijay',15,20000);
insert into employee(name,salery) values('abc',2000);
select count(*) from employee;
select count(age) from employee;
select distinct(sno) from employee;
select count(sno)from employee;
select sum(salery)from employee;
select count(sno) from employee;
select sum(salery)from employee;
select sum(sno)from employee;
select max(salery) from employee;
select * from employee where salery=(select min (salery)from employee);
select min(salery) from employee;
==============================================================
finding the second max value
==============================================================
select max(salery) from employee where salery<(select max(salery)from employee);
select max(age) from employee where age<(select max(age)from employee);
=============================================================================
finding second min 
=============================================================================
select min (salery) from employee where salery>(select min(salery) from employee);
select min (age)from employee where age>(select min(age) from employee);
=======================================================================================
Between,Not between
=====================================================================================
select * from employee where salery between 10000 and 20000;
select * from employee where salery not between 10000 and 20000;
=============================================================
is null,is not null
=============================================================
select * from employee where sno is null;
select * from employee where sno is not null;
====================================================================
Like ,Not Like
====================================================================
select * from employee where name like '%am';
select * from employee where name like 'ra%';
select * from employee where name like '%z';
select * from employee where name not like '%z';
select * from employee where name like '_a%';
select * from employee where name not like '_a%';
select * from employee where name like '%r__a%';
==============================================================================
Not null constraint
=============================================================================
drop table tab1;
create table tab1(id int not null,name varchar(90),age int);
insert into tab1 values(2,'peter',4);
insert into tab1 values(2,'stanely',12);
insert into tab1 values(3,'james',23);
insert into tab1 values(4,'patil',34);
insert into tab1 values(3,'prince',24);
insert into tab1(id,name) values(5,'admin');
insert into tab1(age,id) values(45,13);
insert into tab1(name,age) values('marce',25);//Error
================================================================================
Unique Constraint
=================================================================================
drop table tab2;
create table tab2(id int,name varchar(90),age int,constraint uk24 unique(id));
insert into tab2 values(1,'abc',25);
insert into tab2 values(2,'peter',12);
insert into tab2 values(4,'scott',32);
insert into tab2 values(6,'swann',45);
insert into tab2 values(13,'stphen',23);
insert into tab2 values(9,'robert',20);
insert into tab2 values(2,'anderson',25);//error
insert into tab2(name,age) values('william',21);
insert into tab2(name) values('ramana');
insert into tab2(id) values(21);
insert into tab2(name,id) values('kumar',22);
=====================================================================================
Primary key constraint
======================================================================================
drop table tab2;
create table tab2(sno int,name varchar(90),age int,email varchar(90),constraint pk24 primary key(name));
insert into tab2 values(100,'stephen',56,'abc@a.com');
insert into tab2 values(101,'rama',66,'rama@a.com');
insert into tab2 values(10,'shree',56,'sree@a.com');
insert into tab2 values(102,'khan',27,'khan29@b.com');
insert into tab2(name,age) values('marce',3);
insert into tab2(sno,age) values(1,23);//Error
insert into tab2(sno,name,email) values(11,'ratan','ratan65@b.com');
insert into tab2(age,name,email) values(29,'abdul','ratan65@a.com');
insert into tab2(sno,email) values(24,snape@d.com);//error
=========================================================================================================
Single table multiple constraint
==========================================================================================================
drop table tab3;
create table tab3(sno int not null,name varchar(20),age int,email varchar(90),constraint uk20 unique(email),constraint pk20 primary key(name));
insert into tab3 values(1,'abc',13,'abc@g.com');
insert into tab3 values(2,'patil',22,'patil@y.com');
insert into tab3 values(4,'sahoo',31,'sahoo16@h.com');
insert into tab3 values(5,'scott',31,'sco@r.com');
insert into tab3 values(1,'patil',22,'patil@y.com');//error
insert into tab3 values(4,'sai',31,'sai@h.com');
insert into tab3 values(5,'scott',31,'scot@r.com');//error
insert into tab3(sno,name,email) values(8,'raj','raj24@g.com');
insert into tab3 values(10,'raj',24,'rajan24@g.com');//error
insert into tab3 values(10,'raja',24,'rajan@c.com');
insert into tab3(sno,email) values(8,'raju@g.com');//error
insert into tab3(sno,name) values(8,'rajhu');
insert into tab3(name) values('govinda');//error
insert into tab3(sno,email) name(15,'govinda');
==================================================================================================
two unique key and primary key for one table
==================================================================================================
drop table tab5;
create table tab5(sno int,name varchar(90),age int,constraint uk10 unique(sno),constraint uk11 unique(name));
insert into tab5 values(1,'abc',23);
insert into tab5 values(1,'xyz',23);//error
insert into tab5 values(2,'xyz',23);//error
drop table tab5;
create table tab5(sno int,name varchar(90),age int,constraint pk10 primary key (sno),constraint pk10 primar key(name));//error
=====================================================================================================
Composite unique key and primary key
=====================================================================================================
create table tab5(sno int,name varchar(90),age int,constraint pk8 primary key(sno,name));
insert into tab5 values(1,'abc',22);
insert into tab5 values(1,'abc',35);//error
insert into tab5 values(2,'abc',22);
insert into tab5 values(2,'abc',27);//error
insert into tab5 values(2,'xyz',22);
drop table tab5;
create table tab5(sno int,name varchar(90),age int,constraint uk8 unique(sno,name));
insert into tab5 values(1,'abc',22);
insert into tab5 values(1,'abc',35);
insert into tab5(name,age) values('xyz',25);
insert into tab5(age) values(29);
insert into tab5(name,sno) values('ram',13);
======================================================================================
Not null with unique key and primary key
=======================================================================================
drop table tab4;
create table tab4(id int not null,name varchar(90),age int,constraint uk23 unique(id));
insert into tab4 values(1,'ram',23);
insert into tab4 values(2,'ramu',23);
insert into tab4 values(3,'kane',23);
insert into tab4 values(4,'barud',23);
insert into tab4 values(1,'cook',23);//error
insert into tab4 values(5,'trivadi',25);
insert into tab4(name,age) values('abc',25);//error
insert into tab4(id) values(6);
insert into tab4(id,name) values(7,'babu');
insert into tab4(id,name) values(5,'storm');//error
insert into tab4(id,age) values(11,25);
insert into tab4(name,age) values('abc',25);
insert into tab4(age,id,name) values(22,15,'storm');
drop table tab5;
create table tab5(id int not null,name varchar(90),age int, constraint pk23 primary key(id));
insert into tab5 values(1,'abc',24);
insert into tab5 values(2,'xyz',24);
insert into tab5 values(4,'abaharam',24);
insert into tab5 values(3,'marc',24);
insert into tab5 values(2,'bobby',27);//error
insert into tab5(id,name) values(6,'naidu');
insert into tab5(id) values(7);
insert into tab5(id,age,name) values(17,22,'panda');
insert into tab5(age,id) values(24,9);
insert into tab5(name,age) values('china',12);//error
===========================================================================
operations on constraint
===========================================================================
drop table tab6;
create table tab6(sno int,name varchar(90),salary int);
desc tab6;
alter table tab6 add constraint uk18 unique(sno);
desc tab6;
alter table tab6 disable constraint uk18;
desc tab6;
alter table tab6 enable constraint uk18;
desc tab6;
alter table tab6 add constraint pk18 primary key (salary);
desc tab6;
alter table tab6 disable constraint pk18;
desc tab6;
alter table tab6 enable constraint pk18;
desc tab6;
alter table tab6 drop constraint pk18;
desc tab6;
===========================================================================
Foreign key Constraint(for unique,primary key);
===========================================================================
drop table person;
create table person(id int,name varchar(90),age int,constraint uk10 unique(id));
drop table address;
create table address(id int,house_no varchar(90),str varchar(90),constraint fk10 foreign key(id) references person(id));
insert into person values(100,'abc',22);
insert into person values(200,'xyz',24);
insert into address values(100,'123/9','bnaswadi');
insert into address values(200,'500/2','hrbr');
insert into address values(300,'20/2','knager');//error
delete from person where id='100';//error
delete from address where id='100';
delete from person where id='100';
drop table person;//error
drop table address;
drop table person;
===========================================================================
Sql Joins
===========================================================================
drop table class;
create table class(id int,name varchar(90),class_desc varchar(90),constraint pk11 primary key(id));
insert into class values(1,'6th','this is 6');
insert into class values(2,'7th','this is 7');
insert into class values(3,'8th','this is 8');
select * from class;
drop table section;
create table section(id int,name varchar(90),section_desc varchar(90),constraint fk11 foreign key(id) references class(id));
insert into section values(1,'a','this is a');
insert into section values(1,'b','this is b');
insert into section values(1,'c','this is c');
insert into section values(2,'a','this is a');
insert into section values(2,'b','this is b');
insert into section(name,section_desc) values('a','this is a');
select * from class;
select * from section;
select * from class c inner join section s on c.id=s.id;
select * from class c left outer join section s on c.id=s.id;
select * from class c right outer join section s on c.id=s.id;
select * from class c full outer join section s on c.id=s.id;
drop table business;
create table business(b_id int,b_name varchar(90),b_desc varchar(90),constraint bkp primary key(b_id));
insert into business values(1,'banking','some info');
insert into business values(2,'finiance','some info');
insert into business values(3,'retail','some info');
drop table dept;
create table dept(d_id int,d_name varchar(90),d_desc varchar(90),b_id int, constraint dpk primary key(d_id),constraint dfk foreign key(b_id)references business(b_id));
insert into dept values(1,'sw','some info',1);
insert into dept values(2,'hr','some info',1);
insert into dept values(3,'accounts','some info',2);
insert into dept values(4,'hr','some info',2);
insert into dept(d_id,d_name,d_desc) values(5,'sales','some info');
select * from business;
select * from dept;
select d_name from dept where b_id=2;
select d_name from dept where b_id=(select b_id from business where b_name='banking');
select * from business B inner join dept D on B.b_id=D.d_id;
select b.b_name, d.d_name from business B inner join dept D on B.b_id=D.d_id;
select * from business B left outer join dept D on B.b_id=D.d_id;
select * from business B right outer join dept D on B.b_id=D.d_id;
select * from business B full outer join dept D on B.b_id=D.d_id;
===========================================================================
Joining 3 tables
===========================================================================
drop table india;
create table india(empid int,firstname varchar(30),city varchar2(30));
insert into india values(01,'girish','nanital');
insert into india values(02,'komal','meerut');
insert into india values(03,'amit','lakhnaw');
insert into india values(04,'sandeep','lakhnaw');
select * from india;
drop table newstrack;
create table newstrack(empid int,firstname varchar2(10),email varchar2(30));
insert into newstrack values(01,'suman','girish@gmail.com');
insert into newstrack values(02,'ravi','komal@gmail.com');
insert into newstrack values(03,'santosh','amit@gmail.com');
select * from newstrack;
drop table employee;
create table employee(empid int,frist_name varchar2(30),last_name varchar2(15),city varchar2(10),description varchar2(15));
insert into employee values(01,'gisrish','tewari','nanital','programmer');
insert into employee values(02,'komal','choudhary','meerut','programmer');
insert into employee values(01,'mahindra','singh','lakhnaw','programmer');
select * from employee left join india on employee.empid=india.empid left join newstrack on employee.empid=newstrack.empid;
select * from employee full join india on employee.empid=india.empid full join newstrack on employee.empid=newstrack.empid;
select * from employee right join india on employee.empid=india.empid right join newstrack on employee.empid=newstrack.empid;
select * from employee  join india on employee.empid=india.empid  join newstrack on employee.empid=newstrack.empid;

'''


# In[2]:


dir(mysql.connector)


# In[12]:


# Connecting Oracle MySQL and Python


import mysql.connector

connection = mysql.connector.connect(user = "root",password = "Primesource31#",host = "127.0.0.1",)

print("Connection Established")

#cursor_on_connection = connection.cursor()

#cursor_on_connection = 



# In[27]:


# Connecting PostgreSQL and Python

import psycopg2

postgresql_connection = psycopg2.connect(user='postgres', password="Primesource31#", host="127.0.0.1",
                                         database="srinidjango")

print("Connection Established")

print(postgresql_connection)

cursor_over_postgresql_connection = postgresql_connection.cursor()

cursor_over_postgresql_connection.execute("select * from travello_destinations ")
 
result_cursor_over_postgresql_connection = cursor_over_postgresql_connection.fetchall()

for i in result_cursor_over_postgresql_connection:
    print(i)
    
cursor_over_postgresql_connection.close()

postgresql_connection.close()


# In[54]:


# Connecting SQLLite3 and Python

import sqlite3

sqlite3_connection = sqlite3.connect('srinivasan3.db')

print("Connection Established")

#print(sqlite3_connection)

cursor_over_sqlite3_connection = sqlite3_connection.cursor()

'''cursor_over_sqlite3_connection.execute("create table sriniv4(name vachar(50))")

cursor_over_sqlite3_connection.close()

cursor_over_sqlite3_connection1 = sqlite3_connection.cursor()

cursor_over_sqlite3_connection1.execute("insert into sriniv4 values('srinivasan')")

#print(cursor_over_sqlite3_connection)

result_sqlite3_connection = cursor_over_sqlite3_connection1.fetchall()

for i in result_sqlite3_connection:
    print(i)
'''

cursor_over_sqlite3_connection.execute("select * from sriniv4")

result_cursor_over_sqlite3_connection = cursor_over_sqlite3_connection.fetchall()

for i in result_cursor_over_sqlite3_connection:
    print(i)

cursor_over_sqlite3_connection.close()

sqlite3_connection.close()


# In[175]:


import ibm_db

from ibm_db import exec_immediate

from ibm_db import tables

from ibm_db import fetch_assoc

connection = ibm_db.connect('DATABASE=SAMPLE;'
                            'HOSTNAME=localhost;'
                            'PORT=50000;'
                            'PROTOCOL=TCPIP;'
                            'UID=sriniintraining;'
                            'PWD=prime14773-;','','')

print("Connection Successfull")

print(connection)

def results(command):

    ret = []
    result = fetch_assoc(command)
    while result:
        # This builds a list in memory. Theoretically, if there's a lot of rows,
        # we could run out of memory. In practice, I've never had that happen.
        # If it's ever a problem, you could use
        #     yield result
        # Then this function would become a generator. You lose the ability to access
        # results by index or slice them or whatever, but you retain
        # the ability to iterate on them.
        ret.append(result)
        result = fetch_assoc(command)
    return ret  # Ditch this line if you choose to use a generator.


t = results(tables(connection))

sql = 'SELECT * FROM ' + t[0]['TABLE_NAME']  # Using our list of tables t from before...

print(sql)

rows = results(exec_immediate(connection, sql))

print(rows)


# In[142]:


import ibm_db

conn = ibm_db.connect(dsn='SAMPLE', uid='sriniintraning', pwd='prime14773-')

print(conn)

print("Connection Successfull")


# In[109]:


# Connecting MongoDB and Python

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test-database"]
mycol = mydb["courses"]

myquery = { "author": "Balaji" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x) 


# In[12]:


# Connecting Redis and Python

import redis

r = redis.Redis(
host='localhost',
port=6379,
password='')

r.set('123456','123456789')

'''while(True):

    #key = ''
    #value = ''
    
    #key = input("Enter the key:")
    #value = input("Enter the value:")

    limit = input("Need to push more data, Enter 'Y' or 'y':")
    
    print(limit)
    
    r.set('srsrsrsrsr','werqwerwqrewr')

    if (limit != 'Y' or limit != 'y'):
        break  '''


# In[ ]:


# Connecting Redis and Python

import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    password='')

while (True):

    key = input("Enter the key:")
    value = input("Enter the value:")

    limit = input("Need to push more data, Enter 'Y' or 'y':")

    r.set(key, value)

    if (limit != 'Y' and limit != 'y'):
        break


# In[1]:


import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1', user="root", password="Primesource31#",database="SRINIVASAN")

print("Connection Successfull")

print(connection)

cursor_over_connection = connection.cursor()

#cursor_over_connection.execute("CREATE DATABASE SRINIVASAN")

#cursor_over_connection.execute('CREATE TABLE SRINIVASAN(NAME VARCHAR(50), AGE VARCHAR(20), EMAIL VARCHAR(20))')

cursor_over_connection.execute('INSERT INTO SRINIVASAN VALUES("SRINI","35","srini@gmail.com")')

cursor_over_connection.close()

connection.close()


# In[1]:


import mysql.connector

try:
    connection_1 = mysql.connector.connect(host='127.0.0.1', user="root", password="Primesource31#")

except Exception as err:
    print("An error has occurred during the connection to mysql:", err)

else:
    print("Connection Successful")
    database_name = input("Enter the name of the database to be created:")
    cursor_1_on_connection_1 = connection_1.cursor()

    sql = "CREATE DATABASE %s"

    try:
        cursor_1_on_connection_1.execute(sql, database_name)

    except Exception as err:
        print("An error has occurred while creating the database:",err)
        connection_1.rollback()

    else:
        print("Database creation successful")
        cursor_1_on_connection_1.execute("SHOW DATABASES")
        result_on_cursor_1_on_connection_1 = cursor_1_on_connection_1.fetchall()
        for i in result_on_cursor_1_on_connection_1:
            print(i)

finally:
    connection_1.close()


# In[ ]:




