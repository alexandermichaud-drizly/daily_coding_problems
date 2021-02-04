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
  let omissions = 0;
  let appendix = [];
  for (let i = 0; i < list.length; i++) {
    if (list[i] < 1) {
      appendix = appendix.concat(list.splice(i, 1));
      omissions += 1;
    }
  }
  list = list.concat(appendix);

  // Make values at index of extant values negative
  for (let j = 0; j < list.length - omissions; j++) {
    let index = Math.abs(list[j]) - 1;
    if (index < list.length - omissions) {
      list[index] = (-1)*Math.abs(list[index]);
    }
  }

  // Find first positive
  let k = 0;
  while (k < list.length) {
    if (list[k] > 0) {
      return k+1;
    }
    k++;
  }
  return k;
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
assert.deepEqual(result5, 5);
assert.deepEqual(result6, 3);
assert.deepEqual(result7, 3);
