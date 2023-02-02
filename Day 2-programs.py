#FLOAT AND INTEGER PROGRAM
n=10
res=n-int(n)
if res!=0:
    print("it is a float")
else:
    print("it is a integer")

n=25.0
if isinstance(n,int):
    print("a is integer")
else:
    print("a is float")
    
#DIVISIBLE BY 11
n=int(input("enter"))
if n%11==0:
    print(" its is divisible by 11")
else:
    print("not divisible by 11")
    
#500 IF ELSE PROGRAM
n=int(input("enter a number"))
if n==500:
   print("yes it is num",n)
else:
    print("not")
    
#EVEN AND ODD FUNCTION
n=int(input("Enter a number"))
if n%2==0:
      if n>0:
          print("number is even-postive")
      else:
          print("number is even-negative")
else:
    if n>0:
        print("number is odd-postive")
    else:
        print("number is odd-negative")
        

#BIGGER NUMBER
n=int(input("Enter a number"))
m=int(input("enter a number"))
if n>m:
    print("n is bigger:",n)
else:
    print("m is bigger:",m)
    
#DIVISIBLE BY 2(OR)5
n=int(input("enter"))
if n%2==0 and n%5==0:
    print("the number is divisible by 2 and 5")
else:
    print("not divisible by 2 and 5")
    
#3-BIGGEST NUMBERS
n=int(input("Enter:"))
m=int(input("Enter:"))
a=int(input("Enter:"))
if n>m and n>a:
    print(" n is bigger:",n)
elif m>n and m>a:
    print("m is bigger",m)
elif a>m and a>m:
    print("a is biogger",a)

#INPUT FUNCTION
n=int(input("enter a number"))
if n==500:
   print("yes it is num",n)
else:
    print("not")

#BITWISE PROGRAM
x,y=int(input("Enter:")),int(input("Enter:"))
x,y<=15
z=x&y
print("Bitwise and:",z)
a=x|y
print("Bitwise or:",a)
b=x^y
print("Bitwise xor:",b)
