d={n:n*n for n in range(1,5)}
print(d)


old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price)in
     old.items()}
print(new)

real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items()
     if age>20}
print(now)

# create a list with 8 customers names.display and dictionary which as customers names along with discounts for them from a particular shop
import random
l=["ANIL","JAY","RAJ","KUMAR","NAIDU","BHUVAN","SURYA","SAI"]
l_dict={names:random.randint(1,100) for names in l}
print(l_dict)



#
L1=['a','b','c']
L2=[1,2,3]
d={a:b for (a,b) in zip(L1,L2)}
print(d)


students=["ANIL","JAY","RAJ","KUMAR","NAIDU"]
marks=[500,499,480,330,250]
d={name:(percnt/500)*100 for(name,percnt) in zip(students,marks)}
print(d)

s='A.V.N.S.JAYANTH'
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace('H','A'))
print(s.strip())
print(s.split())
print(s.center(31,'*'))
print(s.split('A'))

print(s.count('A'))
print(s.count('A',5,len(s)))
print(s.endswith('A',0,len(s)))
print(s.find('A',0,len(s)))
print(s.index('A',7,len(s)))

print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.startswith('hello',0,len(s)))
print(s.rfind('A',0,len(s)))
      

s=input('enter a string')
c=input("enter a character")
if c in s:
    print("yes it was right")
else:
    print("no it was wrong")


s=input("Enter a string")
k=s[::-1]
print(s,k)
if (s==k):
    print("palindrome")
else:
    print("not palindrome")

s=(input("enter a string:"))
p=0
for i in s:
    if i==' ':
        p+=1
if p!=0:
    print("no of spaces",p)
else:
    print("no spaces")

    
s=input("Enter:")
char=input()
for i in s:
    if i==char:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("present")
else:
    print("not present")



st=input("enter the string:")
char=input("enter req char:")
a="yes" if char in st else no

print(a)




l=['A','E','I','O','U']
s=input("Enter a string:")
count=0
for i in s:
    if i in l:
        count+=1
print(count)




#MATH MODULE
import math
print("CEil 12.5:",math.ceil(12.5))
print("FLOOR 12.5:",math.floor(12.5))
print("SQRT 345:",math.sqrt(345))
print("FACTORIAL 3:",math.factorial(3))
print("power 2,3:",math.pow(2,3))
print("Remainder 10,3:",math.fmod(10,3))

a,b=divmod(10,3)
print(a,b)






























print("cell 12.5:",math.cell(12.5))
