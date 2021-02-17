def max_sub_arrays(values, k):
	if k == 1:
		for i in values:
			print(i)
	else:
		left_index = 0
		right_index = 1
		max_index = 0
		max2_index = 1 

		while right_index < k:
			if values[right_index] > values[max_index]:
				max2_index = max_index
				max_index = right_index
			else:
				max2_index = right_index if values[right_index] > values[max2_index] else max2_index
			right_index += 1
			
		print(values[max_index])
		
		while right_index < len(values):
			left_index += 1

			if left_index > max_index:
				max_index = max2_index
			elif left_index > max2_index:
				max2_index = left_index if left_index is not max_index else left_index + 1
			
			
			if values[right_index] > values[max_index]:
				max2_index = max_index
				max_index = right_index
			else:
				max2_index = right_index if values[right_index] > values[max2_index] else max2_index
		
			print(values[max_index])
			
			right_index += 1 
	

test_input = [10, 5, 2, 7, 8, 7]

for k in range(1,7):
	print(f'Solution for k={k}')
	max_sub_arrays(test_input, k)
	print('\n')
