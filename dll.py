class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def show(self):
        temp=self.head
        while(temp.next != None):
            print(temp.data)
            temp=temp.next
        print(temp.data)
    def addbeg(self,data):
        nb=Node(data)
        nb.next=self.head
        (self.head).prev=nb
        self.head=nb
    def addend(self,data):
        nb=Node(data)
        temp=self.head
        while(temp.next != None):
            temp=temp.next
        temp.next=nb
        nb.prev=temp
    def addpos(self,data,pos):
        nb=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp2=temp
            temp=temp.next
        temp2.next=nb
        nb.prev=temp2
        nb.next=temp
        temp.prev=nb
    def delbeg(self):
        temp=self.head
        self.head=temp.next
        (self.head).prev=None
        del temp
    def delend(self):
        temp=self.head
        while(temp.next!=None):
            temp2=temp
            temp=temp.next
        temp2.next=None
        del temp
    def delpos(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp2=temp
            temp=temp.next
        temp2.next=temp.next
        (temp.next).prev=temp2
        del temp
        
        
        
l=DLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n2.next=n3
n3.prev=n2
l.addbeg(0)
l.addend(40)
l.addpos(15,3)
l.show()
l.delpos(5)
l.delbeg()
l.delend()
print("after deletion")
l.show()
