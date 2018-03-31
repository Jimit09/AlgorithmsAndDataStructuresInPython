from Node import Node
class StackUsingNode(object):
    """description of class"""
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        if self.top == null:
            self.top = newNode
        else:   
            newNode.next = self.top
            self.top = newNode 
    
    def pop(self):
        if self.top != null:
            retVal = self.top.data
            self.top = self.top.next 
            return retVal
        else: 
            # Throw exception
            print('No items in the Queue')
            

    def peak(self):
          if self.top != null:
              return self.top.data
          else: 
            print('No items in the Queue')

