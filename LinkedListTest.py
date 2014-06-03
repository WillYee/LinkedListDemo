import sys
import random
from LinkedList import LinkedList

def testPrepend():
	my_linked_list = LinkedList()

	for i in range(0,10):
		my_linked_list.prepend(i)

	print my_linked_list

def testAppend():
	my_linked_list = LinkedList()

	for i in range(0, 10):
		my_linked_list.append(i)

	print my_linked_list

def testRemove():
	my_linked_list = LinkedList()

	for i in range(0, 10):
		my_linked_list.append(i)

	for i in range(0, 10):
		print "removing " + str(i)
		my_linked_list.remove(i)
		print my_linked_list

def testPop():
		my_linked_list = LinkedList()

		for i in range(0, 10):
			my_linked_list.append(i)

		for i in range(0, 10):
			node = my_linked_list.pop()
			print str(node._value)
			print "New LinkedList: " + str(my_linked_list)

def testReverse():

	my_linked_list = LinkedList()
	
	for i in range(0, 10):
		my_linked_list.append(random.randint(0,9999))

	print my_linked_list

	my_linked_list.reverse()

	print my_linked_list

def main():

	print "Testing LinkedList Append"
	testAppend()

	print ""

	print "Testing LinkedList Prepend"
	testPrepend()

	print ""

	print "Testing LinkedList Remove"
	testRemove()

	print ""

	print "Testing LinkedList Pop"
	testPop()

	print ""

	print "Testing LinkedList Reverse"
	testReverse()

if __name__ == "__main__":
	main()
