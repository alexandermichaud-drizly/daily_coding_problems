test_arr = [34, -50, 42, 14, -5, 86]

def get_largest_sum(a):
		max_sum = 0
		working_sum = 0

		for i in a:
				temp_sum = working_sum + i
				if temp_sum > 0:
						working_sum = temp_sum
				else:
						working_sum = 0
				max_sum = max(max_sum, working_sum)


		return max_sum

print(get_largest_sum(test_arr))
