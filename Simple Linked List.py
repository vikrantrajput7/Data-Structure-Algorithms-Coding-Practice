class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head=new
    def display(self):
        print("Current Linked List")
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            if temp.next != None:
                print("-->",end=" ")
            temp=temp.next
lst=LinkedList()
lst.insert(4)
lst.insert(2)
lst.insert(3)
lst.insert(6)
lst.insert(1)
lst.display()
