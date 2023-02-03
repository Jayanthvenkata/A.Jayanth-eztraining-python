import random as r
x="i love sweets"
print(r.sample(x,2))

#everytime it gives different output
a=[1,2,3,4,5]

r.shuffle(a)
print(a)

a=[1,2,3,4,5,6]
print(r.choice(a))

b="welcome back"
print(r.choice(b))

a=r.random()
print(a)
#will return random under  number between 0.0 to 1.0
#0.0 includes 1.0 excludes
print(r.randint(20,30))

a=[10,20,30,40,50]
print(r.choices(a,k=10))

s="hello good day"
print(r.choices(s,k=3))

print(r.uniform(5,10))

z=dir(r)
print(z)

#Display whole year calender

import calendar

print("Full calender")
print(calendar.calendar(2023))

print("particular month")
print(calendar.month(2022,3))

print("set first day of the week")
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2022,12))



#display date times
import datetime

a=datetime.datetime.now()
print(a)

sv=a.strftime("%y") #lower case
fv=a.strftime("%y") #upper case

print("year short version",sv)
print("year full version",fv)

# without argument without return value
def sample():
    print("great day")
    print("happy times")

sample()
print("today")
sample()

#without argument with return value
def multi():
    x=int(input("Enter:"))
    y=int(input("Enter:"))
    z=int(input("Enter:"))
    prod=x*y*z
    print(prod)

multi()



def multi():
    x=int(input("Enter:"))
    y=int(input("Enter:"))
    z=int(input("Enter:"))
    prod=x*y*z
    print(prod)
res=multi()
print(res)


#with argument without return value
#static input
def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)
multi(3,4,5)
#user input
def multi1(a,b,c):
    prod=a*b*c
    print(prod)

n1=int(input("Enter:"))
n2=int(input("Enter:"))
n3=int(input("Enter:"))
multi1(n1,n2,n3)


#with  argument with return value
#static input
def multi(n1,n2,n3):
    prod=n1*n2*n3
    return prod
multi(3,4,5)
#user input
def multi1(a,b,c):
    prod=a*b*c
    return(prod)

n1=int(input("Enter:"))
n2=int(input("Enter:"))
n3=int(input("Enter:"))
res1=multi(n1,n2,n3)
print(res1)

#lemons using type 1
def lemons():
    x=int(input("no of lemons"))
    if x>21:
        print("excess lemons",x-21)
    elif x<21:
        print("required lemons",21-x)
    else:
        print("number of lemons left")


lemons()

#factors
def fact():
     for i in range(1,n+1):
        if n%i==0:
            print(i)
n=int(input("enter a number"))         
fact()

#multiplication table

def multi_table(n):
    for i in range(1,n+1):
        print(i,'X',n,'=',i*n)
n=int(input("enter a number"))
multi_table(n)


def digits(n):
     sum=0
     while n!=0:
         rem=n%10
         sum+=rem
         n=n//10
     return(sum) 
n=int(input("Enter a number"))

res=digits(n)
print(res)


def display():
     n=int(input("Enter a number"))
     if n%2==0:
          display()
     else:
          print("over")
display()

#recursive function
def fact(n):
     if n==0:
          return 1
     return n*fact(n-1)
res=fact(5)
print(res)

#logic
#4!
#4*fact(3)
#4*3*fact(2)
#4*3*3*2*fact(1)
#4*3*2*1*fact(0)
#hence output is 24
#functions returns more values 
#add and sub of 2numbers in one function

def add_sub(x,y):
    sub=x-y
    add=x+y
    return sub,add
res1,res2=add_sub(20,10)
print(res1)
print(res2)


#variable length method
def summ(*a):
    c=0
    for i in a:
        c=c+i
    print(c)
summ(10,2,3,1,2)












           














































