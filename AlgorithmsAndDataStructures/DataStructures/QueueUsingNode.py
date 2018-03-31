from Node import Node

class QueueUsingNode(object):
    """description of class"""
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = Node(data)
        if self.head == None :
           self.head = newNode
           self.tail = newNode
        else:
           currentNode = self.head
           while currentNode.next != None:
               currentNode = currentNode.next
           self.tail.next = currentNode
           self.tail = currentNode
               
           
    def remove(self):
        if self.head == None:
            print('No items to remove from the queue')
        elif self.head.next == None:
            retVal = self.head.data
            self.head = None
            self.tail = None
            return retVal
        else:
            retVal = self.head.data
            self.head = self.head.next
            return retVal

    def peak(self):
        if self.head == None:
            print('No items to remove from the queue')
        else :
            return self.head.data
        