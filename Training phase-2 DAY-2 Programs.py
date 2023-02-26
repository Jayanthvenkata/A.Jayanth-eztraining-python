
##protected -\\

class encap:
    _a=int(input())
    c=20
    def encapfunction(self):
        _b=200
        print("encap fun_accessing protected")
obj=encap()
print(obj._a)
obj.encapfunction()
print
(obj.c)
##private

class encap:
    _a=input()
    print(_a)
    def encapfunction(self):
        print(self._a)
       
        print("encap fun_accessing private")
obj=encap()
obj.encapfunction()
print(obj._a)
#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
s=moverload()
s.display()
s.display(2,3)
s.display(5) 



#

class kakinada():
    def placename(self):
        print("kakinada placename is PEC")
    def student(self):
        print("yes-kakinada")
    def year(self):
        print("third year")
class rjy():
    def placename(self):
        print("rjy placename is PEC")
    def student(self):
        print("yes-rjy")
    def year(self):
        print("third year")
obj_kkd=kakinada()
obj_rjy=rjy()
for details in (obj_kkd,obj_rjy):
    details.placename()
    details.student()
    details.year()
#creating Node-declaration & definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            prinht("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-> ",end="")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display()
                

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            prinht("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-> ",end="")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.display()


#inserting node at the begining of the list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None                
    def insert_begining(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            prinht("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-> ",end="")
                temp=temp.next
obj=singlelinkedlist() 
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_begining(100)
obj.display()
print("")
print("after inserting 555")
obj.insert_begining(555)
obj.display()   
            
        
        
#inserting node at end of the list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None                
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            prinht("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-> ",end="")
                temp=temp.next
obj=singlelinkedlist() 
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_end(100)
obj.display()
print("")
print("after inserting 555")
obj.insert_end(555)
obj.insert_end(11111)
obj.display()


#inserting a node at position of the list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None                
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            prinht("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-> ",end="")
                temp=temp.next
obj=singlelinkedlist() 
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 25")
obj.display()
print("")
print("after inserting 25")
obj.insert_position(2,25)
obj.display()
print("")
print("after inserting 55")
obj.insert_position(5,55)
obj.display()




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self_node.next
    def display(self):
        current=self.head
        while current is not None:
             print("current.data",end="")
             current=current.next
a_1list=LinkedList()
n=int(input("How many elements would you like"))
for i in range (n):
    data=int(input("Enter data item:"))
    a_1list.append(data)
print("The linked list:",end="")
a_1list.display()
    
      


                   
            









    
                
            
                 







