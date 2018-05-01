class Node(object):
	def __init__(self, value, left = None, right = None, parent = None):
		self.__left = left
		self.__right = right
		self.__value = value
		self.__parent = parent


	def is_leaf(self):
		return self.__left == None and self.__right == None


	def set_right_child(self, node):
		self.__right = node


	def set_left_child(self, node):
		self.__left = node


	def set_parent(self, node):
		self.__parent = node


	def set_value(self, value):
		self.__value = value


	def get_right_child(self):
		return self.__right


	def get_left_child(self):
		return self.__left


	def get_parent(self):
		return self.__parent


	def get_value(self):
		return self.__value


	def is_leaf(self):
		return self.__left is None and self.__right is None


	def has_only_one_child(self):
		#XOR to decide if it has only one child
		return (self.__left and not self.__right) or (not self.__left and self.__right)


	def has_two_children(self):
		return self.__right and self.__left
