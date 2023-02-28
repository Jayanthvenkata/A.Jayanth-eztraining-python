class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        if not temp:
            print("List is empty")
            return
        else:
            print("Start: ",end="")
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next            
        print("end")
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        elif self.head.data >= new_node.data:
            new_node.next =self.head
            self.head =new_node
        else:
            current=self.head
            while current.next and new_node.data>current.next.data:
                current=current.next
            new_node.next=current.next
            current.next=new_node               
    def delete(self,key):
        if self.head is None:
            print("Deletion Error: The list is empty")
            return
        if self.head.data == key:
            self.head=self.head.next
            return
        current=self.head
        while current:
            if current.data ==  key:
                break
            previous = current
            current=current.next
        if current is None:
            print("Deletion Error: key not found")
        else:
            previous.next=current.next          
if __name__=="__main__":    
    LL=LinkedList()
    print("")
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    
    LL.insert(10)
    LL.printlist()
    LL.delete(12)
    LL.delete(8)
    LL.delete(10)
    LL.printlist()
             
L=[10,20,30,40,50,60]                
print(L)                
                
l=list(map(int,input("enter number").strip().split()))[ :4]                  


#creating my modules
import fn
fn.printing()

print(__name__)

def printing():
    print("Hi")

print("before function")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__=="__main__":
    f1()
    f2()
    f3()
print("name:",__name__)




class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.display()
                 

#Double linked list at start(insert)
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head =n
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_start()
l.display()
                              

#Double linked list at end(insert)
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_end()
l.display()



#Double linked list at postion(insert)
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_pos(2)
l.display()




#Double linked list at beginning(delete)
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_beginning()
l.display()



#Double linked list at end(delete)
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_end()
l.display()


#Double linked list at position(delete)
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_position(2)
l.display()

#circular linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class createList:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head
    def add(self,data):
        newNode=Node(data)
        if self.head.data is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.tail.next=self.head

        def display(self):
            current=self.head
            if self.head is None:
                print("List is Empty")
                return
            else:
                print("Nodes of the circular linked list:")
                print(current.data,"-->")
                while (current.next!=self.head):
                    current=current.next
                    print(current.data,"-->")
class CircularLinkedList:
    c1=createList()
    c1.add("J")
    c1.add("A")
    c1.add("Y")
    c1.add("A")
    c1.add("N")
    c1.add("T")
    c1.add("H")
    c1.display()
    
                    









    
    





















































































































