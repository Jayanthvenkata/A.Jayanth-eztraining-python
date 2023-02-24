L=[1,2,3]
r=map(lambda x:x+x,L)
print(list(r))

res=map(lambda n:pow(n,2),L)
print(list(res))


name="jayanth"
(lambda name:print(name)) (name)


L=[2,4,6,8,10,12,14]
r=map(lambda x:pow(x,1/2),L)
print(list(r))


from abc import ABC,abstractmethod
class abstractdemo(ABC):
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()


#one parent and one child class
class parent:
    def display(self):
        print("parent class")
#Derived class
class child(parent):
    def show(self):
        print("child class")
c=child()
c.display()
c.show()
    
#single inheritance    
class A:
    n=30
class B(A):
    def calc(self):
        c=self.n+70
        print(c)
obj=B()
obj.calc()
#multiple inheritance
class mom:
    def mdisplay(self):
        print("mom class")
class dad:
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
c1=child()
c1.cdisplay()
c1.mdisplay()
c1.ddisplay()

#multi level inheritance
class grandparent:
    def display(self):
        print("grand parent class")
class parent(grandparent):
    def show(self):
        print("parent class")
class child(parent):
    def printing(self):
        print("child class")
c=child()
c.display()
c.show()
c.printing()
#hererical inheritance
class parent:
    def pdisplay(self):
        print("parent class")
class child1(parent):
    def c1show(self):
        print("child1 class")
class child2(parent):
    def c2show(self):
        print("child2 class")
c1=child1()
c1.c1show()
c1.pdisplay()
c2=child2()
c2.c2show()
c2.pdisplay()

#hybrid inheritance        
class parent:
    def pdisplay(self):
        print("parent class")
class child1(parent):
    def c1show(self):
        print("child1 class")
class child2(parent):
    def c2show(self):
        print("child2 class")    

class kid1(child1):
    def k1display(self):
        print("kid1 class")

class kid2(child1):
    def k2display(self):
        print("kid2 class")
class kidd1(child2):

    def k1show(self):
        print("kidd1 class")        
class kidd2(child2):
    def k2show(self):
        print("kidd2 class")
        
c1=kid1()
c1.k1display()
c1.c1show()
c1.pdisplay()
c2=kid2()
c2.k2display()
c2.c1show()
c2.pdisplay()
c3=kidd1()
c3.k1show()
c3.c2show()
c3.pdisplay()
c4=kidd2()
c4.k2show()
c4.c2show()
c4.pdisplay()


#happy numbers
def Happy(num):
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum
num=int(input("enter a number:"))
res=num
   
while(res!=1 and res!=4):
    res=Happy(res) 


if(res==1):    
    print(str(num)+" is a happy number")
elif(res==4):

    print(str(num)+" is not a happy number")




    


































