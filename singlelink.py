class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def addnodebeg(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def addnodepos(self,data,pos):
        nb=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        nb.next=temp.next
        temp.next=nb
    def addnodeend(self,data):
        nb=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=nb
        nb.next=None
    def show(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
    def delbeg(self):
        temp=self.head
        self.head=temp.next
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
        del temp
        
l=SLL()      
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
l.addnodeend(50)
l.addnodebeg(0)
l.addnodepos(40,4)
l.show()
print("after deletion")
l.delbeg()
l.delend()
l.delpos(3)
l.show()
    
