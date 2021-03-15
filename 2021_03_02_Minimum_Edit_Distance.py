def edit_distance(a,b):
    if len(a) == 0:
        return 0
    else:
        change_from = a[0]
        change_to = b[0]

        dist = 0

        # DELETE
        if change_from != '' and change_to == '':
            dist = 1 + edit_distance(a[1:], b[1:])

        # PREPEND OR APPEND
        elif change_from == '' and change_to != '':
            dist = 1 + edit_distance(a[1:], b[1:])
        
        # NO SUBSTITUION
        elif change_from == '' and change_to == '':
            dist += edit_distance(a[1:], b[1:])
        elif change_from == change_to:
            dist += edit_distance(a[1:], b[1:])
        
        else:
            # SUBSTITUTION
            sub = 1 + edit_distance(a[1:], b[1:])

            # INSERTION
            b += ''
            ins = 1 + edit_distance(a,b[1:])
            dist = min(ins,sub)

        return dist
    
def get_minimum_edit_distance(a,b):
    max_length = len(a) + len(b)
    min_edit = None
    
    temp_a = '' * len(b)
    temp_b = '' * len(a)
    temp_a = a + temp_a
    temp_b = temp_b + b

    for i in range(max_length):
        edit = edit_distance(temp_a, temp_b)
        if min_edit is None or min_edit > edit:
            min_edit = edit
        
        del temp_a[0]
        temp_a += ''

    return min_edit
           

assert get_minimum_edit_distance('kitten', 'sitting') == 3

