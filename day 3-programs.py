#1)create a list with 10 times print the elements one by one?

l=[1,2,3,4]
for i in range(len(l)):
    print(l[i])
for j in l:
     print(j)

#after creating a list with 6 elements from the user extract only even munbers and print
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if(i%2==0):
        print(i)
        
#create a list with 5 float numbers find out and display sum and average of a list
l=[20.5,13.4,1.4,6.7,8.9]
for i in range(len(l)):
     i=sum(l)
print(i)         
print("average",i/len(l))

#LIST PROGRAMS
l=[i for i in "JAYANTH"]
print(l)

L1=[2**x for x in range(2,10)]
print(L1)

L2=[a for a in range (100,201,20)]
print(L2)

L3=[1,2,3,4,5,6]
L4=[i for i in L3 if (i<5)]
print(L4)

#SET EXAMPLES
s={1,2,3}
s1={1,2,3,4}
s2=s1.issuperset(s)
print(s2)


s1={1,2,3,5,10}
s2={4,1,9,2,10}
s1^s2
{3, 4, 5, 9}
print(s1.symmetric_difference(s2))
{3, 4, 5, 9}

s={1,2,3,4,5,6,7,8,9}
print(s)
print(s.add(10))
print(s)
print(s.update([20,40]))
print(s)
print(s.discard(20))
print(s)
print(s.remove(10))
print(s)

#LIST THE NUMBER IS < 750
l=list(map(int,input("Enter").split()))
p=1
for i in l:
    p=i*p
if p<750:
        print("yes:",p)
else:
        print(sum(l))
        


l=list(map(int,input("Enter").split()))
print(l)
p=1
n=0
for i in l:
    p=i*p
    n=n+i
if p<=750:
        print(p)
else:
        print(n)



#FOR LOOP
size=int(input("size"))
L=[]
for i in range(size):
    ele=int(input("element :"))
    L.append(ele)
print(L)

for j in L:
    if(j%2==0):
        print(j)
#DICTIONARY PROGRAM
        d={1:"one",2:"two"}
print(type(d))

print(d.keys())

print(d.values())

print(d.items())


d={'syl':'techno','chaaru':'meizu'}
print(type(d))

print(d.keys())

print(d.values())































