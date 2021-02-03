const assert = require('assert');

const test_input_list_1 = [3,4,-1,1];
const test_input_list_2 = [4,2,1];
const test_input_list_3 = [1,2,0];
const test_input_list_4 = [5,2,3,1,7,6];
const test_input_list_5 = [2];


const findMissing = list => {
    let n = 1;

    return n;
};

const result1 = findMissing(test_input_list_1);
const result2 = findMissing(test_input_list_2);
const result3 = findMissing(test_input_list_3);
const result4 = findMissing(test_input_list_4);
const result5 = findMissing(test_input_list_5);

assert.deepEqual(result1, 2);
assert.deepEqual(result1, 3);
assert.deepEqual(result1, 3);
assert.deepEqual(result1, 4);
assert.deepEqual(result1, 1);
