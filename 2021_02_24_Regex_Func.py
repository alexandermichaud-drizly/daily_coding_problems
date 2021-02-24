def regex_checker(string, exp):
	s_index = 0
	e_index = 0

	while s_index < len(string):

		# Expression has matched substring
		# But there are remaining chars
		if e_index >= len(exp):
			return False

		elif exp[e_index] == '.':	
			if e_index + 1 < len(exp) and exp[e_index + 1] == '*':
				e_index += 2
				s_index += 1

				while string[s_index] != exp[e_index]:
					# Exp ends with .* 
					# Matches remaining chars of str
					if s_index >= len(string):
						return True

					s_index += 1

			else:
				s_index += 1
				e_index += 1
		
		elif exp[e_index] == '*':
			prev = e_index
			e_index += 1

			while s_index < len(string) and string[s_index] == exp[prev]:
				s_index += 1

		elif exp[e_index] != string[s_index]:
			return False
		
		else: # matches
			s_index += 1
			e_index += 1

	return True


assert regex_checker('ray',     'ra.')  == True
assert regex_checker('raymond', 'ra.')  == False
assert regex_checker('chat',    '.*at') == True
assert regex_checker('chats',   '.*at') == False
