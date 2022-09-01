class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return(True)
        return(False)
    
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        
        temp.next = Node(data)
    

    def insertAtBegining(self, data):
        temp = Node(data)
        if self.isEmpty():
            self.head = temp
            return
        
        (temp.data,self.head.data) = (self.head.data, temp.data)
        (temp.next, self.head.next) = (self.head.next, temp)
    

    def insertAtPos(self, pos, data):
        if (self.isEmpty()):
            self.insertAtBegining(data)
            return(True)
        
        i = 1
        temp = self.head
        while (i < pos):
            if (temp.next == None):
                return(False)

            temp = temp.next
            i = i + 1
        
        if (i == pos):
            newNode = Node(data)
            (temp.data, newNode.data) = (newNode.data, temp.data)
            (newNode.next, temp.next) = (temp.next, newNode)
            return(True)
        else:
            return(False)
    
    def delete(self, v):
        if (self.isEmpty()):
            return(False)
        
        temp = self.head
        if (temp.data == v):
            temp.data = temp.next.data
            temp.next = temp.next.next
            return(True)

        while(temp.next.data != v):
            temp = temp.next
            if (temp.next == None):
                return(False)
        temp.next = temp.next.next
        return(True)

    def display(self):
        if self.head == None:
            print('None')
        
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print()

L = LinkedList()
L.append(30)
L.append(40)
L.append(50)
L.display()
L.delete(50)
L.display()