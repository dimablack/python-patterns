class LinkedListNode:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node


class LinkedList:
	def __init__(self, head=None):
		self.head = head
	
	def insert(self, value):
		node = LinkedListNode(value)
		if self.head is None:
			self.head = node
			return
		
		cur_node = self.head
		while True:
			if cur_node.next_node is None:
				cur_node.next_node = node
				break
			cur_node = cur_node.next_node
	
	def print_linked_list(self):
		cur_node = self.head
		while cur_node is not None:
			print(cur_node.value, "->", end=' ')
			cur_node = cur_node.next_node
		print('None')


lList = LinkedList()
lList.print_linked_list()
lList.insert(11)
lList.print_linked_list()
lList.insert(12)
lList.print_linked_list()
lList.insert(13)
lList.print_linked_list()
lList.insert(14)
lList.print_linked_list()
lList.insert(15)
lList.print_linked_list()
lList.insert(16)
lList.print_linked_list()
