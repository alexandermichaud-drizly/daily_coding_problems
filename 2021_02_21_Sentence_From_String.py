def dictionarify(words):
	output = {}
	for word in words:
		output[word] = True
	return output

def sentence(string, words):
	dictionary = dictionarify(words)
	i = 1
	output = []
	while i <= len(string):
		substring = string[:i]
		if dictionary.get(substring):
			output.append(substring)
			string = string[i:]
			i = 1
		else:
			i += 1
	return output if string == '' else None

test_words_1 = ['bed','bath','bedbath','and','beyond']
test_words_2 = ['the','quick','brown','fox']

print(sentence('bedbathandbeyond', test_words_1))
print(sentence('thequickbrownfox', test_words_2))
