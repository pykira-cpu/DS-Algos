'''A linked list is a data structure made of a chain of node objects. Each node contains a value and a pointer to the next node
 in the chain.

Linked lists are preferred over arrays due to their dynamic size and ease of insertion and deletion properties.

The head pointer points to the first node, and the last element of the list points to null. When the list is empty, the head
pointer points to null.

Original Python does not ship with a built-in linked list data structure like the one seen in Java.

Let’s see how we can create our own implementation of a standard class-based singly linked list in Python.
'''
# A single node of a singly linked list
class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

#Creating single node
sample_node = Node(3)
print(sample_node.data)

'''The next step is to join multiple single nodes containing data using the next pointers, and have a single head pointer
 pointing to a complete instance of a Linked List.

Using the head pointer, we will be able to traverse the whole list, even perform all kinds of list manipulations while we are
 at it.
'''

# Udacity 

class Element(object):
	def __init__(self,value):
		self.value = value
		self.next = None



class LinkedList(object):
	
	def __init__(self,head = None):
		self.head = head

	def append(self,new_element):
		self.head = current 
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element 

	def insert_first(self,new_element):
		new_element.next = self.head
		self.head = new_element

	def delete_first(self):
		if self.head:
			delete_element = self.head
			temp = delete_element
			self.head = temp
			return  delete_element
		else:
			return None

#x = LinkedList()
#x.head = Element(7)
#print(x.head.value)
'''
Stack - LIFO(Last In First Out)
	
'''

class Stack(object):

	def __init__(self,top = None):
		self.a = LinkedList(top)

	def push(self,new_element):
		self.a.insert_first(new_element)

	def pop(self):
		return self.a.delete_first()

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
stack.push(e1)
print(stack.pop().value)
print(stack.pop().value)



'''
Queue - FIFO(First In First Out)

'''

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())

