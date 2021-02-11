def step_count(steps, increments=[1]):
    if steps < 0:
        return -1
    if steps == 0:
        return 1
    else:
        count = 0
        for i in increments:
            attempt = step_count(steps - i, increments)
            if attempt > 0:
                count += attempt
        return count
    

test_increments_1 = [1]
test_increments_2 = [1,2]
test_increments_3 = [1,3,5]

assert step_count(1, test_increments_1) == 1
assert step_count(2, test_increments_1) == 1
assert step_count(3, test_increments_2) == 3
assert step_count(4, test_increments_2) == 5
assert step_count(4, test_increments_3) == 3
assert step_count(5, test_increments_3) == 5 
    
