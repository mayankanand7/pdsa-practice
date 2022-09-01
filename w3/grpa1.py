from requests import head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None


    def insert_end(self, data):
        temp = Node(data)

        if self.head == None:
            self.head = temp
            self.head.next = self.last
            return

        if self.last == None:
            self.head.next = temp
            temp.prev = self.head
            self.last = temp
            return
        
        (temp.prev, self.last.next) = (self.last, temp)
        self.last = temp
        return

    def delete_end(self):
        if self.last == None:
            return
                
        temp = self.last
        self.last = temp.prev
        self.last.next = None


L = [1,3,5,7,9]
dll = doubly_linked_list()
for i in L:
  dll.insert_end(i)

temp = dll.head