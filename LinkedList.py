class LinkedList:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node


cur_node = LinkedList(1, LinkedList(123, LinkedList(23, LinkedList(34, LinkedList(45, LinkedList(56, LinkedList(67)))))))

while cur_node is not None:
	print(cur_node.value, "->", end=' ')
	cur_node = cur_node.next_node
print('None')
