from collections import namedtuple
import re

class Deserializer:

	Longest = namedtuple('Longest', ['path', 'length'])

	def __init__(self):
		self.__file_system = None

	def __new_file_system(self, root):
		self.__file_system = Directory(root)

	def __deserialize_helper(self, file_path):
		longest = self.Longest('', 0)

		if not re.match(r'^\\n', file_path):
			root = re.match(r'^[a-z0-9]+', file_path).group()
			self.__new_file_system(root)
			# Call helper on file_path minus root
		else:
			# Parse path for leading newline + number of tabs
			# Split based on matches of identical number of \t
			# For each subitem
			#	if blank, return ('',0)
			#	elif contains period, return (filename, length of file)
			#	else call deserialize helper on everything from next \n to end. 
			#		Create new directory objects
			#		longest.length = abs_path length + longest.length if greater than longest.length 


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
test_input_2 = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
test_input_3 = r"dir\n\tsubdir1\n\t\tsubsubdir1" 

driver = Deserializer()
print(driver.deserialize(test_input_1))
print(driver.deserialize(test_input_2))
print(driver.deserialize(test_input_3))
