import re

def longest_file_path(path):
	length = 0
	split_path = re.split(r'\\n', path)
	split_path.reverse()

	for i, possible_file in enumerate(split_path):
		if re.search(r'\.', possible_file):
			depth = len(re.findall(r'\\t', possible_file)) - 1
			j = i + 1
			abs_path = re.split(r'\\t', possible_file)[-1]
			while depth > -1:
				possible_parent = split_path[j]
				if len(re.findall(r'\\t', possible_parent)) == depth and not re.search(r'\.', possible_parent):
					abs_path = re.split(r'\\t', possible_parent)[-1] + '/' + abs_path
					depth -= 1
				j += 1
			print(abs_path)
			length = max(length, len(abs_path))

	return length

test_input_1 = r"dir\n\tsubdir1\n\tsubdir2\n\t\tfile1.ext"
test_input_2 = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
test_input_3 = r"dir\n\tsubdir1\n\t\tsubsubdir1" 

print(longest_file_path(test_input_1))
print(longest_file_path(test_input_2))
print(longest_file_path(test_input_3))
