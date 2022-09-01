class Node:
    # Constructor
    def __init__(self, v):
        self.v = v
        self.next = None
    
    # Is Empty
    def isEmpty(self):
        if self.v == None:
            return True
        return False
    
    # Append Recursively
    def append(self, v):
        if self.isEmpty():
            self.v = v
            return
        
        if self.next == None:
            self.next = Node(v)
            return
        
        self.next.append(v)
    
    # Append Iteratively
    def appendi(self, v):
        if (self.v == None):
            self.v = v
            self.next = None
            return
        
        temp = self
        while (temp.next != None):
            temp = temp.next
        
        self.next = Node(v)
    
    
    def insertAtBegining(self, v):
        if (self.isEmpty()):
            self.v = v
            return
        
        newNode = Node(v)

        # Exchange values
        (self.v, newNode.v) = (newNode.v, self.v)

        # Exchange links
        newNode.next = self.next
        self.next = newNode


    def insertAtPos(self, pos, v):
        if pos < 1:
            return("Invalid position")
        
        if pos == 1:
            return(self.insertAtBegining(v))

        i = 1
        temp = self
        while (i < pos):
            temp = temp.next
            i = i + 1
        if (i == pos):
            newNode = Node(v)
            (newNode.v, temp.v) = (temp.v, newNode.v)
            (newNode.next, temp.next) = (temp.next, newNode)
        else:
            return("Position is out of range")
    

    def delete(self, v):
        if self.isEmpty():
            return(False)
        
        temp = self
        if temp.v == v:
            self = temp.next
            return(True)

        while (temp.next.v != v):
            temp = temp.next
            if (temp.next == None):
                return(False)
        temp.next = temp.next.next
    

    def deleteAtPos(self, pos):
        if self.isEmpty():
            return(False)
        
        temp = self
        if pos == 1:
            self.v = temp.next.v
            self.next = temp.next.next
            return(True)

        i = 2
        curr = self.next
        while (i < pos):
            if (curr.next == None):
                return(False)
            temp = curr
            curr = curr.next
            i = i + 1

        temp.next = curr.next

    

    def display(self):
        if self.isEmpty():
            return()
        
        temp = self
        while(temp.next != None):
            print(temp.v)
            temp = temp.next
        print(temp.v)
        return

n = Node(1)
n.append(2)
n.append(3)
# n.display()
# n.insertAtBegining(-1)
# n.insertAtPos(2, 0)
n.delete(3)
# n.deleteAtPos(3)
n.display()
