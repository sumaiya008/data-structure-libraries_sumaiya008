# Simple linked list implementation

# creating class node.
class Node(object):
    # node carry data and a pointer which points to next data.
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;

#creating LinkedList class.
class LinkedList(object):
    #Defining head
    def __init__( self ):
		self.head = None

   
    
		