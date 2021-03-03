def fill(elevations):
    tallest = -1
    units = 0
    for wall in elevations:
        if wall > tallest:
            tallest = wall
        else:
            units += tallest - wall
    return units

test_1 = [3, 0, 1, 3, 0, 5]
test_2 = [2, 1, 2]

assert fill(test_1) == 8
assert fill(test_2) == 1
