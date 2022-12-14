# -*- coding: utf-8 -*-
"""Python Codes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pnrdEN-kTNLorHrMHEcWFnrUit6e4lS_
"""

m= int(input()) #coloumn
n= int(input()) #rows

a = [[i*j for i in range(m)] for j in range(n)]
  
print(a)

m= int(input()) #coloumn
n= int(input()) #rows

a=

import sympy as sym
from sympy import *

x= sym.Symbol('x')
exp= x**2+ sym.cosh(x)
print(sym.integrate(exp,x))

pip install automata

import sympy as sym
from sympy import *
import math

print(sqrt(2).evalf(100))

import sympy as sym
from sympy import *

a= Rational(1,2)
b= Rational(1,3)
print(a+b)

import sympy as sym
from sympy import *

x,y = symbols("x y")
exp= (x+y)**6
print(sym.expand(exp))

import sympy as sym
from sympy import *

x= Symbol('x')
exp= sym.sin(x)/sym.cos(x)
print(exp.trigsimp())

import sympy as sym
from sympy import *

x= Symbol('x')
exp= (sym.sin(x)-x)/x**3
print(sym.limit(exp,x,0))

import sympy as sym
from sympy import *

x= Symbol('x')
print(sym.diff(sym.log(x),x))
print(sym.diff(sym.sin(x),x))
print(sym.diff(sym.cos(x),x))
print(sym.diff(1/x,x))

import sympy as sym
from sympy import *

x,y= sym.symbols('x y')
equation1= sym.Eq(x+y,2)
equation2= sym.Eq(2*x+y,0)
print(sym.linsolve([equation1,equation2],(x,y)))

import sympy as sym
from sympy import *

print(sym.integrate(x**2,x))
print(sym.integrate(sym.sin(x),x))
print(sym.integrate(sym.cos(x),x))

pip install sympy

"""# OBJECT ORIENTED PROGRAMMING"""

class Computer:

  def config(self): #this is a method/ behavior
    print("i5, 16gb, 1TB")

#creating an object/instance of class computer
#object_name= Class_name()
comp1= Computer()
comp2= Computer()
#how to access the method inside class? Class_name.method_name(object)
Computer.config(comp1) 
Computer.config(comp2)
#works exactly the same as above method
comp1.config()

class Computer:

  def __init__(self): #this is called immediately once an object is created
     print("im inside init")
  def config(self): #this is a method
    print("i5, 16gb, 1TB")

comp1= Computer()
comp2= Computer()

comp1.config()
comp2.config()

class Computer:

  def __init__(self,cpu,ram):
     print("im inside init")
     self.cpu= cpu
     self.ram= ram

  def config(self): #this is a method
    print("The config is", self.cpu, self.ram)

comp1= Computer("i5",16)
comp2= Computer('Ryzen',8)

comp1.config()
comp2.config()

class Computer:

  def __init__(self):

    #Doing this means both the objects have the same name and age

    self.name= "Pallavi" 
    self.age= 20

  def update(self):
    self.age= self.age+20

comp1= Computer()
comp2= Computer()
print(comp1.name)
print(comp2.name)

comp1.name= "Mehvish"

print("After modification")
comp1.update()
print(comp1.age)
print(comp1.name)
print(comp2.name)

class Computer:

  def __init__(self):
    self.name= "Pallavi"  
    self.age= 20
  
  #using the compare fucntion
  def compare(self,other):
    if(self.age==other.age): print("same")
    else: print("not same")

comp1= Computer()
comp2= Computer()
print(comp1.name)
print(comp2.name)

comp1.compare(comp2)

comp2.age= 45
comp2.compare(comp1)

#DIFFERENT TYPES OF VARIABLES
class Car:
  wheels=4 #class variable


  def __init__(self):

    #instance variables 

    self.mil=10
    self.com= "BMW"
  
car1= Car()
car2= Car()

car1.name= "Mercedes"
print(car1.com, car1.mil, Car.wheels)

#class inside a class
class

'''1. Write a Python class named SRMIST with six attributes school, dept1,
dept2, dept2 and dept3. Add a new attribute specialization and display the
entire attribute and their values of the said class. Now remove the dept1
and dept2 attribute and display the entire attribute with values.'''


class SRMIST:
  def __init__(self,dept1,dept2):
    self.dept1= dept1
    self.dept2= dept2
    self.dept3= "CTECH"
    self.school= "School of computing"

admin= SRMIST("CINTEL","NWS")
admin.dept4= "BIOTECH"

print(admin.dept1)
print(admin.dept2)
print(admin.dept3)
print(admin.dept4)

#removing attributes from the class

delattr(admin,'dept1')
delattr(admin,'dept2')

print(admin.dept3)
print(admin.dept4)

'''2. Write a Python program to crate four empty classes, CTECH,
CINTEL, NWC and DSBS. Now create some instances and check
whether they are instances of the said classes or not. Also, check whether
the said classes are subclasses of the built-in object class or not.'''

#USE OF isinstance(obj,instance) and issubclass()

class CTECH:
  pass
class CINTEL:
  pass
class NWC:
  pass
class DSBS:
  pass

obj1= CTECH()
obj2= CINTEL()
obj3= DSBS()

print(isinstance(obj1,CTECH))
print(isinstance(obj2,CINTEL))
print(isinstance(obj3,NWC))

'''3. Write a program to print the names of the departments students by
creating a Dept class. If no name is passed while creating an object of the
Dept class, then the name should be "SCO", otherwise the name should
be equal to the String value passed while creating the object of the Dept
class.'''

class Dept:
  def __init__(self, dept1="SCO"):
      self.dept1= dept1

obj1= Dept("NWC") #name is passed while creating object
obj2= Dept()      #no name is passed

print(obj1.dept1)
print(obj2.dept1)

'''4. Create a class named 'Rectangle' with two data members- length and breadth 
and a function to calculate the area which is 'length*breadth'. 
The  class has three constructors which are : 
1 - having no parameter - values of both length and breadth are assigned  zero. 
2 - having two numbers as parameters - the two numbers are assigned as  length 
and breadth respectively. 
3 - having one number as parameter - both length and breadth are  assigned that
 number. 
Now, create objects of the'Rectangle' class having none, one and two parameters
and print their areas. '''

class Rectangle:
  length= 0
  breadth=0
  
  def __init__(self,*args):
    
    if(len(args)==0):
      self.length= 0
      self.breadth=0
    
    elif(len(args)==1):
      self.length= args[0]
      self.breadth= args[0]
    
    else:
      self.length= args[0]
      self.breadth= args[1]
  def area(self):
    print("The area is:", self.length*self.breadth)

rec1= Rectangle()
rec2= Rectangle(4,5)
rec3= Rectangle(3)

rec1.area()
rec2.area()
rec3.area()

'''5. Create a class named 'PrintDT' to print various numbers of different
datatypes by creating different functions with the same name
'python_data??? having a parameter for each datatype. (example : tuple, list,
string)'''

class PrintDT:
  def python_data(self,tuple):
    self.tuple= ()
    print(self.tuple)

  def python_data(self,list):
    self.list= []
    print(self.list)

  def python_data(self,str1):
    self.str1= ""
    print(self.str1)

p= PrintDT()
p.python_data((1,2,3,4,5))
p.python_data([1,2,3,"appale"])
p.python_data("this is a string")

'''6. A student from SRMIST has his/her money deposited Rs.15000,
Rs.30000 and Rs. 40,000 in banks-CUB, HDFC and Indian Bank
respectively. We have to print the money deposited by him/her in a
particular bank.
Create a class named 'Banks_SRMIST' with a function 'getBalance'
which returns 0. Make its three subclasses named 'CUB', 'HDFC' and
'Indian_Bank' with a function with the same name 'getBalance' which
returns the amount deposited in that particular bank. Call the function
'getBalance' by the object of each of the three banks.'''

class Banks_SRMIST():
  def getBalance(self): 
    return 0
class CUB(Banks_SRMIST): 
  def getBalance(self):
    return 15000
class HDFC(Banks_SRMIST):
  def getBalance(self): 
    return 30000
class Indian_Bank(Banks_SRMIST): 
  def getBalance(self):
    return 45000 
    
obj1_499=CUB()
obj2_499=HDFC() 
obj3_499=Indian_Bank() 

print(obj1_499.getBalance()) 
print(obj2_499.getBalance()) 
print(obj3_499.getBalance())

'''7. Create a Time class and initialize it with hours and minutes.

1. Make a method addTime which should take two time object and add
them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
2. Make a method displayTime which should print the time.
3. Make a method DisplayMinute which should display the total minutes
in the Time. E.g.- (1 hr 2 min) should display 62 minute.'''


class Time:
  def __init__(self,hours,minutes):
    self.hours=hours
    self.minutes=minutes
    
    def addTime(t1,t2):
      t3= Time(0,0)
      t3.hours= t1.hours +t2.hours
      t3.minutes= t1.minutes+ t2.minutes

'''8. Write a program to print the area and perimeter of a triangle having
sides of 3, 4 and 5 units by creating a class named 'Triangle' with a
function to print the area and perimeter.'''

class Triangle:

  def __init__(self):
    self.side1= 3
    self.side2= 4
    self.side3= 5

  def area(self):
    print("The area is:",self.side1*self.side2*self.side3)
  
  def perimeter(self):
    print("The perimeter is:",self.side1+self.side2+self.side3)

#instantiating a class
obj1= Triangle()
obj1.area()
obj1.perimeter()

"""# DECLARATIVE PROGRAMMING"""

import sqlite3
conn = sqlite3.connect("worker.db")
conn.execute("""CREATE table work(
  workerid int primary key not null,
  fname text not null,
  lname text not null,
  salary int not null,
  j_date date not null,
  dept text not null
)""")

#inseting values into the table

conn.execute("insert into work values(104,'raj','ganesh',15000,'12-02-2000','cse')")
conn.execute("insert into work values(106,'rajes','kumar',340000,'12-02-2000','cse')")
conn.execute("insert into work values(107,'arun','kumar',10500,'12-02-2000','cse')")
conn.execute("insert into work values(111,'surya','kumar',23000,'12-02-2000','ece')")
conn.execute("insert into work values(121,'suresh','kumar',40000,'12-02-2000','ece')")
conn.execute("insert into work values(141,'chandra','babu',270000,'12-02-2000','ece')")
conn.execute("insert into work values(1251,'arun','surendar',23000,'12-02-2000','eee')")
conn.execute("insert into work values(129,'abhishek','kumar',40000,'12-02-2000','eee')")
conn.execute("insert into work values(131,'chandru','surya',270000,'12-02-2000','eee')")

res= conn.execute("select fname as worker_name from work")
for row in res:
  print(row[0])

res= conn.execute("select upper(fname) from work")
for row in res:
  print(row[0])

res= conn.execute("select distinct dept from work")
for row in res:
  print(row[0])

res= conn.execute("select substr(fname,1,3) from work")
for row in res:
  print(row[0])

res= conn.execute("select instr(fname, 'a') from work")
for row in res:
  print(row[0])

res= conn.execute("select fname from work order by fname asc")
for row in res:
  print(row[0])

res= conn.execute("select substr(fname,2) from work")
for row in res:
  print(row[0])

res= conn.execute("select fname from work where fname like '%n' and length(fname)=4")
for row in res:
  print(row[0])

res= conn.execute("select fname,salary from work where salary between 10000 and 500000")
for row in res:
  print(row[0],"  ",row[1])

res= conn.execute("select count(dept) from work where dept= 'cse' ")
for row in res:
  print(row[0])

res=conn.execute("select fname from work where fname like 'a%' ")
for row in res:
  print(row[0])

res=conn.execute("select fname from work where fname like '%a' ")
for row in res:
  print(row[0])

res=conn.execute("select fname from work where fname like '%r_' ")
for row in res:
  print(row[0])

#second highest salary 

res= conn.execute("select max(salary) from work where salary not in(select max(salary) from work)")
for row in res:
  print(row[0])

res=conn.execute("select avg(salary) from work")
for row in res:
  print(row[0])

res=conn.execute("select j_date from work where j_date like '%2000'")
for row in res:
  print(row[0])

res=conn.execute("select fname from work where fname like 'a%' or 'c%' ")
for row in res:
  print(row[0])

res= conn.execute("select fname from work where salary>40000")
for row in res:
  print(row[0])

res=conn.execute("select fname from work where fname like '%aj' ")
for row in res:
  print(row[0])

res= conn.execute("update work set salary= salary + 0.1*salary ")
res= conn.execute("select * from work")
for row in res:
  print(row[0],row[1],row[2],row[3],row[4],row[5])

res= conn.execute("delete from work where workerid like 107")
res= conn.execute("select * from work")
for row in res:
  print(row[0],row[1],row[2],row[3],row[4],row[5])

"""# FUNCTIONAL PROGRAMMING"""

def square(a):
  return a*a

print(square(5))

f= lambda x: x*x
print(f(5))

from functools import reduce

list1= [1,2,3,4,5,6,7,8,9,10,15,20,25]
print(list(filter(lambda x: x%2==0, list1)))

print(list(filter(lambda x: x%2!=0,(map(lambda x: x*x, list1)))))

print(reduce(lambda x,y,:x+y, list1))

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
print(list(filter(lambda x: len(x)>7,my_names)))

list1= [1,2,3,4,5]

#finding squares
res= list(map(lambda x: x*x, list1))
print(res)

res= list(map(lambda x: x*x*x, list1))
print(res)

#filter vowels from a sequence

list1= ['a', 'b', 'u', 'i', 'o']
def vowelfind(x):
  if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    return True

result= list(filter(vowelfind, list1))
print(result)

#finding palindrome using lambda

my_list= ['car', 'bob', 'hilih', 'malayalam']
result= list(filter(lambda x: (x== x[::-1]),my_list))
print(result)

"""# LOGICAL PROGRAMMING PYDATALOG"""

pip install pyDatalog

from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,ram,raju,shyam,priya,carol,marks,grade,passm')
+marks('ram',90)
+marks('raju',45)
+marks('priya',85)
+marks('carol',70)
+marks('shyam',80)
+grades('ram','A')
+grades('raju','F')
+grades('priya','B')
+grades('carol','C')
+grades('shyam','B')

#creating the constraints/rules
passm(X) <= grades(X, 'O') or grades(X,'A') or grades(X,'B')
failm(X)<=
print(marks(X,Y))
print(marks(X,80))
print(marks('priya',Y))

import sympy as sym 
from sympy import *
a = sym.Symbol('a') 
b = sym.Symbol('b')
a2,b2= symbols('a2,b2')
eq1=Eq(a*2-a*b+a*b-b2,a2-b*2)
print(solve(eq1))

from pyDatalog import pyDatalog
pyDatalog.create_terms('N, Factorial')
Factorial[N] = N*Factorial[N-1]
Factorial[1]=1
print(Factorial[4]==N)

from pyDatalog import pyDatalog
pyDatalog.create_terms('X')
print(X.in_((0,1,2,3,4)))

pip install pyDatalog

"""# SYMBOLIC PROGRAMMING SYMPY"""

import sympy as sym
from sympy import *
import math

exp= sqrt(2).evalf(100)
print(exp)

import sympy as sym
from sympy import *

a= Rational(1,2)
b= Rational(1,3)
sum= a+b
print(sum)

import sympy as sym
from sympy import *

x,y= symbols('x,y')
exp= (x+y)**6
print(expand(exp))

import sympy as sym
from sympy import *

exp= sym.sin(x)/sym.cos(x)
print(sym.simplify(exp))
print(sym.trigsimp(exp))

import sympy as sym
from sympy import *

exp= (sym.sin(x)-x)/x**3
print(sym.limit(exp,x,0))

import sympy as sym
from sympy import *

x= sym.Symbol('x')
print(diff(log(x),x))
print(diff(1/x,x))
print(diff(sin(x),x))
print(diff(cos(x),x))

import sympy as sym
from sympy import *

eq1= Eq(x+y,2)
eq2= Eq(2*x+y,0)
res= sym.linsolve([eq1,eq2],(x,y))
print(res)

import sympy as sym
from sympy import *

x= sym.Symbol('x')
print(sym.integrate(x**2,(x,1,3)))
print(sym.integrate(sin(x),x))
print(sym.integrate(cos(x),x))

import sympy as sym
from sympy import *

x,y= sym.symbols('x,y')
exp1= 2*x**3+ 4*x+8
exp2= sym.diff(exp1,x,2)
eq= sym.Eq(exp2+9*exp1,1)
print(sym.solve(eq))

import sympy as sym
from sympy import *

x,y= sym.symbols('x,y')
exp1= (x+y)**3
exp2= x+ 3*x**2+ 2*y+3*x*y**2+y
eq= sym.Eq(exp1,exp2)
print(sym.solve(eq))

import sympy as sym
from sympy import *

a= sym.Matrix([[0,0,0],[1,2,3],[1,1,1]])
b= sym.Matrix([[0,0,0],[1,2,3],[1,1,1]])
pprint(a+b)
print()
pprint(a*b)

import sympy as sym
from sympy import *

x,y= symbols('x,y')
print(solve(x+y+x-y))
print(sym.re(x).evalf())
print(sym.I.evalf())
print(sym.im(x).evalf())
print(sym.I*sym.im(x)+sym.I*sym.im(y)+sym.re(x)+sym.re(y))

print()

print(expand(x+y,complex=True))
print()

pprint(Matrix([[1,x],[y,1]]))

"""# AUTOMATA"""

pip install automata

"""# STRUCTURAL PROGRAMMING"""

for i in range(1000,2001):
  if(i%8==0 and i%5==0):
    print(i)

import random

n= random.randint(1,9)3

while True:
  guess= int(input())
  if(guess==n):
    break
print("Well guessed!")

for i in range(0,6):
  for j in range(0,i):
    print("*", end="")
  print()

m= int(input())
n= int(input())
list1= [[i*j for i in range(m)]for j in range(n)]
print(list1)

n= int(input())
char_count=0
number_count=0

for i in range(0,len(n)):
  if(n[i].isalpha()):
    char_count= charcount+1
  if(n[i].isnumeric()):
    number_count= number_count+1
print(char_count, number_count)

import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

