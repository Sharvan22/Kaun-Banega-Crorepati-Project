#def welcome():
 #print("Hello swagat hai aapka")
#pop="Hello world"


def welcome1():
    print("Vedic is gay")
print(__name__)
if __name__ == "__main__":
  welcome1()

#Global and local variable
x=10
def function():
    global x
    x=5
    y=6
    print(y)
function()
print(x)
#File io or handling in python
#x=open("mehta.txt")
#z=x.read()
#print(z)
#z=open("mehta.txt","w")
#x=z.write("Hello i am mehta moksh!!!")
#print(x)
x=open("mehta.txt","a")
#z=x.write("Hey i am again mehta!!")
#print(z)
#c=open("mehta.txt","rt")
#b=c.read()
#print(b)
#c=open("mehta.txt","rb")
#b=c.read()
#print(b)
with open("mehta.txt","a"):
    x.write("Sharvan Mehta")
u=open("Sharvan.txt","w")
v=u.write("This is a new file 1.")
print(v)
#####read,readlines and other methods
a=open("zx.txt","r")
while True:
    b=a.readline()
    print(b)
    if not b:
        break


a=open("dev.txt","r")
i = 0
while True:
    i = i + 1
    b=a.readline()
    if not b:
      break
    m1=b.split(",")[0]
    m2=b.split(",")[1]
    m3=b.split(",")[2]
    print(f"Marks of student {i} in maths are:{m1}")
    print(f"Marks of student {i} in English are:{m2}")
    print(f"Marks of student {i} in SST are:{m3}")
    print(b)
#writelines
d=open("Naruto.txt","w")
p=["line\n","roll no02524202022\n"]
o=d.writelines(p)
print(o)

f = open("cvm.txt", 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
    q=f.write
    print(q)






