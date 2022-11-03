# Implementation of Linked list

class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

class linkedList:
    def __init__(self):
        self.head=None
    
    # insert item at the begining of the linked list
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    # printing the items of the linked list

    def print(self):
        # checking if there are elements in the list or not 
        if self.head is None:
            print("liked list is Empty.")
            return 
        
        llist=''
        itr=self.head

        while itr:
            llist+= str(itr.data) + '-->'
            itr=itr.next

        print(llist)

    # inser item at the end of linked list 
    def insert_at_End(self,data):
        # Check if the list is empty or not
        if self.head is None:
            self.head=Node(data,None)
            return 
        # if list is not empty
        
        itr=self.head
        # Go throw the linked list to reach the last element
        while itr.next:
            itr=itr.next
        # insert the new node after the last element.
        itr.next=Node(data,None)

    def insert_values(self, valuesList):
        self.head=None

        for data in valuesList:
            self.insert_at_End(data)
    
    def get_length(self):
        counter=0
        itr=self.head
        while itr:
            counter+=1
            itr=itr.next
        return counter

if __name__=='__main__':
    item=linkedList()
    item.insert_values(["Mostafa","Rady","Mizar"])
    item.print()
    print(item.get_length())