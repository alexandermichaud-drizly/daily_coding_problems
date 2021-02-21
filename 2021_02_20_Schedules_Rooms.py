test_schedule_1 = [[30,75], [0,50], [60, 150]]
test_schedule_2 = [[0,50], [60, 150]]
test_schedule_3 = [[30,75], [0,50], [60, 150], [140, 160], [40, 180]]

def rooms(schedule):
	schedule = sorted(schedule, key=lambda x: x[0])
	i = 0
	j = 1 

	while i < len(schedule):
		if j >= len(schedule):
			i += 1
			j = i + 1
		elif schedule[i][1] < schedule[j][0]:
			schedule[i][1] = schedule[j][1]
			schedule.pop(j)
		else:
			j += 1

	return len(schedule)

assert rooms(test_schedule_1) == 2
assert rooms(test_schedule_2) == 1
assert rooms(test_schedule_3) == 3
