from collections import namedtuple
import re

class Deserializer:

	Longest = namedtuple('Longest', ['path', 'length'])

	def __init__():
		self.__file_system = None

	def __new_file_system(self, root):
		self.__file_system = Directory(root)

	def __deserialize_helper(self, file_path):
		longest = Longest('', 0)

		if file_path[0] is not :
			root = file_path.split()[0]
			self.__new_file_system(root)

		return longest

	def deserialize(self, file_path):
		return self.__deserialize_helper(file_path).length
		

class Directory:
	def __init__(self, name, parent=None):
		self.name = name
		self.parent = parent
		self.abs_path = self.parent.name + "/" + self.name if parent is not None else self.name
		self.contents = []

	def add(self, item):
			self.contents.append(item)

class File:
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.abs_path = self.parent.name + "/" + name

test_input_1 = r"dir\n\tsubdir1\n\tsubdir2\n\t\tfile1.ext"
test_input_2 = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t\subsubdir2\n\t\t\tfile2.ext"
test_input_3 = r"dir\n\tsubdir1\n\t\tsubsubdir1" 

driver = Deserializer()
driver.deserialize()
