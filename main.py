from operator import index

for i in range(12):
    print("5 X",i,"=",5*i)
    if(i==5):
        break

print("Loop se bhago")


for i in range(12):
    print("5 X",i,"=",5*i)
    if(i==5):
        print("Yha space de rha hou jiska matlab ye hai kii continue statement lagaii haii")
        continue
# Ye upar break aur continue hmara khatam hogya


#Ab yha se suru honge functions of python
def calculateGmean(a,b):
    K=(a*b)/(a+b)
    print(K)
def isgreater(a,b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
def islesser(a,b):
    pass


a=8
b=9
isgreater(a,b)

calculateGmean(a,b)

c=8
d=7
isgreater(c,d)
calculateGmean(c,d)

# Ab yha se hum suru karenge phir python arguments.
def average(a=6,b=6,):
  print("The average is",(a+b)//2)
average(5,5,)

def average(fname="Vedic",mname="pundir",lname="mehta"):
    print("My name is",fname,mname,lname)
average("eshaan")


def average(*numbers):
     P=0
     for i in numbers:
      P= P + i
     print("The sum of these numbers are:",P/len(numbers))
average(5,5,5,5)



def average(*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  return sum / len(numbers)
c= average(5,5,5,5)
print(c)

# List suru horhi haii hmari yhaa see

marks=[10,4,7,9,2,]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(type(marks))



# List comprehension with proper variable naming
squares = [t * t for t in range(10)]
print(squares)
list1 = [t * t for t in range(10) if t % 3 == 0]
print(list1)


# Now comes the list method
l=[1,2,3,4,5,6,7,8,9]
print(l)
l.append(10)
print(l)
G=[11,2,3,45,5,6,76,8,9]
G.sort()
print(G)
#Ye upar ki lines mai ascending to descending order houa haii
O=[11,2,3,45,5,6,76,8,9]
O.sort(reverse=True)
print(O)
l.reverse()
print(l)
p=[1,2,3,4,5,6,7,8,9]
print(p.index(7))
print(p.count(3))

m=p.copy()
print(m)
p.insert(1,355)
print(p)
g=[700,800,900]
p.extend(g)
print(p)
#Concatination of the lists
k=p+g
print(k)
# Ab yhaa se suru hogi hmari tuples
tup=(1,)#yha par ek chiz note karne wali hai aur vo ye hai ki agar ek element ho jaise yha 1 tha tou hmme , ka use karna hai
print(type(tup),tup)



fruits=("apple","kela","grapes","kiwi","Watermelon","oranges")
city=list(fruits)
city.append("cherry")
city.pop(1)
fruits=tuple(city)
print(fruits)



countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)






cities=("delhi","goa","maharastra","punjab","bihar","chattisgarh")
s=list(cities)
s.append("kashmir")
s.pop(2)
cities=tuple(s)
print(cities)

#Ab yha se suru hongi hmarii f-string
name="Sharvan"
country="India"
print(f"Hey my name is {name} and i am from {country}")

price=49.06666
txt=f"For price only {price:.2f}  dollars !"
print(txt)
print(f"{5*5}")
print(type(f"{4*3}"))

#Ab yha se suru hogi hmari docstrings
def p(n):
    '''Takes a number n provides the square of n'''
    print(n**2)
p(5)
print(p.__doc__)

#Recursion in python
def factorial(n):
  if(n==0 or n==1):
      return 1
  else:
      return n * factorial(n-1)
factorial(5)
print(factorial(5))
# isi kaa extension hai ekk fibonacci sequence
def fib(n):
 a=0
 b=1
 if n==0:
     print(a)
 else:
     print(a)
     print(b)
     for i in range(2,n):
         c=a+b
         a=b
         b=c
         print(c)
fib(9)

# Ab yhaa se hmara sets suru horhe haii
s={False,56,"Fish",56,56,"Moksh"}
print(s)

moksh=set()
print(type(moksh))

moksh={""}
print(type(moksh))

for value in s:
    print(value)
#Ab aayenge set methods
s1={1,4,5,6,8,9}
s2={3,5,7,2,8}
print(s1.union(s2))
s1.update(s2)
print(s1)
s2.update(s1)
print(s2)
#intersection
cities={"berlin","tokyo","delhi","wdc"}
cities2={"berlin","wuhang","bangkok","wdc"}
print(cities.intersection(cities2))
cities.intersection_update(cities2)
print(cities,cities2)
#symmetric difference
fruits={"apple","kela","grapes","mango","cherry"}
fruits2={"apple","grapes","cherry"}
print(fruits.symmetric_difference(fruits2))
z=fruits.symmetric_difference_update(fruits2)
print(fruits)
x=fruits2.symmetric_difference_update(fruits)
print(fruits2)
#difference
sports={"cricket","football","badminton","racing",}
sports2={"javelin throw","cricket","chess","ludo"}
print(sports.difference(sports2))
sports.difference_update(sports2)
print(sports)
sports2.difference_update(sports)
print(sports2)
#Ab yha se suru hongii hmarii dictionaries
dic = {"Name":"Moksh","subject":"BCA","roll no":"02524202022"}
print(dic)
print(dic["roll no"])
#print(dic["Name2"])#Ye jo haii error throw karega
print(dic.get("Name2"))#ye wali line none print karki degi
print(dic.keys())
print(dic.values())
for key in dic.keys():
    print(f"The value of the corresponding key {key} is {dic[key]} ")

print(dic.items())
for key, value in dic.items():
    print(f"The value of the corresponding key {key} is {value}")
#Exception handling(Try and except handling)
s=(input("Enter the number:"))
print(f"Multipication table of your number {s} would be:")
try:
 for i in range(1,11):
    print(f"{int(s)*i}")
except:
    print("Invalid Output")

try:
    num=int(input("Enter an number:"))
    a=[4,6]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Number entered is out of range")
#Finally keyword ka usee
def func():
 try:
     p=[1,3,5,7]
     i=int(input("Enter the number:"))
     print(p[i])
     return 4
 except:
    print("Some error ocurred")
    return 0
 finally:
   print("I am always executed")
x=func()
print(x)

#Raising custom errors
try:
    user_input = input("Enter your number between 5 and 9 (or type 'quit' to exit): ")


    if user_input.lower() == "quit":
        print("quit")
    else:

        a = int(user_input)
        if a < 5 or a > 9:
            raise IndexError("Your number should be between 5 and 9")
        else:
            print(f"Your number {a} is valid!")
except ValueError:
    print("Invalid input! Please enter a number.")







s=input("Enter your word:")
p=list(s)
q=p.pop(0)
p.append(q)
p.insert(0,"z")
p.insert(1,"x")
p.insert(2,"y")
z=["f","g","h"]
p.extend(z)
print(p)
#Short hand if else statement
a=5000
b=5000
print("a is greater than b") if a>b else print("a is eqvivalent to b") if a==b else print("b is greater than a")
#Enumerate function
names=["Dev","Moksh","Vedic","Shorey"]
index=0
for naam in names:
    print(naam)
    if index==2:
     print("Very poor! Call your parents")
    index +=1



colors=["red","green","yellow","orange","purple"]
for index,color in enumerate(colors):
    print(index,color)
    if index==3:
        print("Very bright! Good color")

colors=["red","green","yellow","orange","purple"]
for index,color in enumerate(colors,start=2):
    print(index,color)
    if index==3:
        print("Very bright! Good color")
#Ab yha se suru hoga hmara import ka khel
import math
q=math.sqrt(9)

from math import sqrt,pi
result=sqrt(16)*pi

#from math import * (isse se sab kuch import ho jayega jo bhi math function me hai)
from math import sqrt,pi as s
result1=sqrt(9)*s
print(result1)
#import math
#print(dir(math))
print(math.sqrt,type(sqrt))
print(type(math.nan))
#from Moksh import pop,welcome
#print(pop)
#welcome()
import Moksh
Moksh.welcome1()













