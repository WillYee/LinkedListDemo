class Node():

	def __init__(self, value, next, previous):
		self._value = value
		self._next = next
		self._previous = previous

class LinkedList():

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def append(self, value):

		# Empty LinkedList
		if self.length == 0:
			self.head = Node(value, None, None)
			self.tail = self.head
		elif self.length == 1:
			# 1 element LinkedList
			self.tail = Node(value, None, self.head)
			self.head._next = self.tail

		elif self.length > 1:
			# More than 1 element LinkedList
			new_node = Node(value, None, self.tail)
			self.tail._next = new_node
			self.tail = new_node

		self.length += 1

	def prepend(self, value):

		# Empty LinkedList
		if self.length == 0:
			self.head = Node(value, None, None)
			self.tail = self.head
		elif self.length == 1:
			# LinkedList has 1 element
			self.head = Node(value, self.tail, None)
			self.tail._previous = self.head

		elif self.length > 1:
			# Not empty LinkedList
			new_node = Node(value, self.head, None)
			self.head._previous = new_node
			self.head = new_node

		self.length += 1

	def pop(self):

		removed_node = self.head

		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.head._next._previous = None
			self.head = self.head._next

		self.length -= 1

		return removed_node

	def remove(self, value):

		if self.length == 1:
			self.head = None
			self.tail = None
			self.length = 0

		current_node = self.head

		while current_node != None:

			if current_node._value == value: # Must remove at least one node

				if current_node == self.head: # Case 1: Node is head
					self.head = current_node._next
					self.head._previous = None

				elif current_node == self.tail: # Case 2: Node is tail
					self.tail = current_node._previous
					self.tail._next = None

				elif current_node._value == value: # Case 3: Node is in list but not head or tail
					current_node._previous._next = current_node._next
					current_node._next._previous = current_node._previous

				self.length -= 1
				break

			current_node = current_node._next

	def reverse(self):
		self._reverse(self)

	def _reverse(self, linked_list): # Recursive reverse

		# Base case: 1 element
		if linked_list.length == 1:
			return linked_list

		# Recursive case
		reverse_node = linked_list.pop()
		linked_list._reverse(linked_list).append(reverse_node._value)
		return linked_list

	def get_size(self):
		return self.length

	def is_empty(self):
		if self.length == 0:
			return True
		else:
			return False

	def __str__(self):
		returnString = ""
		current_node = self.head

		while current_node != None:
			returnString = returnString + " " + str(current_node._value)
			current_node = current_node._next

		return returnString 

