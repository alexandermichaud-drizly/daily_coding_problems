test_arr = [34, -50, 42, 14, -5, 86]

def get_largest_sum(a):
		max_with = 0
		max_without = 0

		for i in a:
				temp_sum = max_with + i	
				max_without = max(max_with, max_without)
				max_with = temp_sum if temp_sum > max_with else 0


		return max(max_with, max_without)

print(get_largest_sum(test_arr))
