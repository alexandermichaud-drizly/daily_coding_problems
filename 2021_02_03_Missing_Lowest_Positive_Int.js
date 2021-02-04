const assert = require('assert');

const test_input_list_1 = [3,4,-1,1];
const test_input_list_2 = [4,2,1];
const test_input_list_3 = [1,2,0];
const test_input_list_4 = [5,2,3,1,7,6];
const test_input_list_5 = [2, 3, 10, 4, 1];
const test_input_list_6 = [2,2,5,1,4];
const test_input_list_7 = [2,1,7,5];

// Assumes no duplicates or multiple missing integers
// 
// const findMissing = list => {
//     let max = list[0];
//     
//     const incompleteSum = list.reduce((a, x) => {
//         if (x > max) {
//           max = x;
//         }
//         return x > 0 ? a + x : a;
//     });
// 
//     const diff = ((max * (max + 1))/2) - incompleteSum;
//     return diff === 0 ? (max + 1) : diff;
// };

const findMissing = list => {
  let max = 1;
  for (let i = 0; i < list.length; i++) {
    if (list[i] > max) {
      max = list[i];
    }
    if (list[i] < 1) {
      list.splice(i, 1);
    }
  }

  // Make values at index of extant values negative
  for (let j = 0; j < list.length; j++) {
    if (list[j] < list.length) {
      list[list[j] - 1] = (-1)*Math.abs(list[j])
    }
  }

  console.log(list);
  // Find first positive
  let k = 0;
  while (k < list.length) {
    if (list[k] > 0) {
      return k+1;
    }
    k++;
  }
  return max + 1;
}

const result1 = findMissing(test_input_list_1);
const result2 = findMissing(test_input_list_2);
const result3 = findMissing(test_input_list_3);
const result4 = findMissing(test_input_list_4);
const result5 = findMissing(test_input_list_5);
const result6 = findMissing(test_input_list_6);
const result7 = findMissing(test_input_list_7);

assert.deepEqual(result1, 2);
assert.deepEqual(result2, 3);
assert.deepEqual(result3, 3);
assert.deepEqual(result4, 4);
assert.deepEqual(result5, 1);
assert.deepEqual(result5, 3);
assert.deepEqual(result5, 3);
