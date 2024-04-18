'''user_name = 'Novac'
user_age = 25
user_profit = 33.58
print("My name is %s. My age is %d and I made profit %g." %(user_name, user_age, user_profit))

student_name = ['Lisa', 'Moon', 'Trout']
for e in student_name:
    print(e)

a = list(range(1, 10))
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for e in a:
    print("value",e)
    total += e
print(total) # 45

a = list(range(1, 10))
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for e in a:
    if e % 2 == 0:
        total += e
print(total) # 20

a=10
for b in range (a):
    print(b)

total = 0
j = 1
while j < 10:
    total +=j
    j +=1
    print(j)
    print(total)
name = [ "Mahfuj", "Arish", "Amena" ]
countries = [ "Bangladesh", "Australia", "USA", "Sweden" ]
for n in name:
    for c in countries:
        print(n," visited ", c)
try:
    print(x)
    print(Exception.x)
except:
    print('How are you')
function1():
    print('This is my first function.')
    print('The job of this function is to print two sentences.')
function1()

def calcultor(name,weight,height):
    cal=weight/height **2
    print (cal)
    if(cal<25):
        return name + "not overweight"
    else:
        return name + "overweight"

name= input("enter name")
weight=float(input("enter weight"))
height= float(input("enter height"))
total=calcultor(name,weight,height)
print(total)

def primegenrator(num):
    for i in range(2,num):
        if num % 2==0:
            return False
        return True
    
def primenumber(n):
    num =2
    while n:
        if primegenrator(num):
            yield num
            n-=1
        num+=1
    return

it=primenumber(90)
for e in it:
    print(e, end=', ')

j=1,0,2,0,3,0
i=0
while i<=5:
    if j[i]==0:
     print(j[i], end=" ")
    i+=1

j= "ssssiiii"
i=7


i=int(input("enter a starting no"))
j=int(input("enter a ending no"))
while i<=j:
    print(i, end=" ")
    i+=1 


i=1
j=list (int(input("total even no generate")))
while i<=j[list]:
   if i%2==0:
     print(i, end=" ")
   i+=1
   

i=1
j=int(input("how many times you want to print Sonu"))

while i<=j:
   print("sonu")
   i+=1
   print(i)

        
j= str(input("please enter string"))
count=1
for x in j:
    if x=="a":
       print(x, end="")
       count+=1
print("count",count ) 
    
i=1
j= int(input("please enter a no to print natural no"))

while i<=j:
   ## print(i, end="")
    
    if i<=j:
         print(i,end=" ,")
    i+=1 '''
k= input("enter a string")
for i in k:
    if i == "r":
        break
    print(i, end="")
    
