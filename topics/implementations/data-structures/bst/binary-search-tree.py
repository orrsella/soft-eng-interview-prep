from node import Node

class BST(object):

	def __init__(self, root = None):
		self.root = root


	def __is_empty(self):
		return self.root is None


	def insert(self, node_to_insert):
		if self.__is_empty():
			self.root = node_to_insert

		else:
			self.__insert_aux(self.root, node_to_insert)


	def __insert_aux(self, node, node_to_insert):
		if node.get_value() < node_to_insert.get_value():
			if node.get_right_child() is None:
				node.set_right_child(node_to_insert)
				node_to_insert.set_parent(node)

			else:
				self.__insert_aux(node.get_right_child(), node_to_insert)

		else:
			if node.get_left_child() is None:
				node.set_left_child(node_to_insert)
				node_to_insert.set_parent(node)

			else:
				self.__insert_aux(node.get_left_child(), node_to_insert)


	def search(self, value_to_search):
		value_found = self.__search_aux(self.root, value_to_search)

		return value_found


	def __search_aux(self, node, value_to_search):
		if node and node.get_value() == value_to_search:
			return node

		if node is None:
			return node

		if node.get_value() < value_to_search and node.get_right_child():
			return self.__search_aux(node.get_right_child(), value_to_search)

		return self.__search_aux(node.get_left_child(), value_to_search)	


	def delete(self, node_value):
		node_found = self.search(node_value)

		if node_found:
			if node_found.has_only_one_child():
				self.__delete_node_one_child(node_found)

			elif node_found.is_leaf():
				self.__delete_node_leaf(node_found)

			else:
				self.__delete_node_with_two_children(node_found)

		return node_found


	def __delete_node_one_child(self, node):
		if node.get_right_child():
			node.set_value(node.get_right_child().get_value())
			node.set_right_child(None)

		elif node.get_left_child():
			node.set_value(node.get_left_child().get_value())
			node.set_left_child(None)


	def __delete_node_leaf(self, node):
		parent = node.get_parent()

		if parent.get_right_child() is node:
			parent.set_right_child(None)

		else:
			parent.set_left_child(None)


	def __delete_node_with_two_children(self, node):
		successor = self.__min_tree_value(node.get_right_child())
		node.set_value(successor.get_value())

		if successor.is_leaf():
			self.__delete_node_leaf(successor)

		elif successor.get_right_child():
			successor_parent = successor.get_parent()
			successor_parent.set_left_child(successor.get_right_child())


	def absolute_min(self):
		return self.__min_tree_value(self.root)


	def __min_tree_value(self, node):
		if not self.__is_empty():
			if node.get_left_child():
				return self.__min_tree_value(node.get_left_child())

			return node


	def inorder(self):
		self.__inorder_aux(self.root)


	def __inorder_aux(self, node):
		if node is not None:
			self.__inorder_aux(node.get_left_child())
			print node.get_value()
			self.__inorder_aux(node.get_right_child())




# I will write a test later :)
tree = BST()
tree.insert(Node(50))
tree.insert(Node(30))
tree.insert(Node(20))
tree.insert(Node(40))
tree.insert(Node(70))
tree.insert(Node(60))
tree.insert(Node(80))
tree.insert(Node(63))
tree.insert(Node(61))
tree.insert(Node(64))

print tree.search(50)
print tree.search(20)
print tree.search(80)
print tree.search(1)
print tree.search(-1)
print tree.search(70)
print tree.search(60)
print tree.search(40)
print tree.search(30)

tree.delete(50)
print "########"
tree.inorder()
