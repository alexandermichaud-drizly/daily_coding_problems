def get_itinerary(flights, start):
		if len(flights) == 1 and flights[0][0] == start:
				return [flights[0][0], flights[0][1]]

		output = None
		index = 0
		while index < len(flights):
				if flights[index][0] == start:
						next_dest = flights.pop(index)
						index += 1
						search = get_itinerary(flights, next_dest[1])
						if search is not None:
								output = [next_dest[0]] + search
				index += 1
		
		return output

test = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
# results = ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

print(get_itinerary(test, 'YUL'))

fail_test = [('SFO', 'COM'), ('COM', 'YYZ')]
print(get_itinerary(fail_test, 'COM'))

multiple_possible = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
print(get_itinerary(multiple_possible, 'A'))
