const assert = require('assert')

const greatestNonadjacentSum = list => {
  
  console.log('Current value: ' + list[0])
  if (list.length === 0) {
    return 0
  }
  if (list.length < 3) {
    return list[0];
  }

  let max = 0;

  for (let i = 2; i < list.length; i++) {
    let comparison = greatestNonadjacentSum(list.slice(i));
    max = comparison > max ? comparison : max;
  }
  
  let adjacent = greatestNonadjacentSum(list.slice(1));
  max += list[0];

  console.log('New Max: ', max);
  return adjacent > max ? adjacent : max;
};

const tests = [
  {input: [2,4,6,2,5], result: 13},
  {input: [5,1,1,5],   result: 10}
];

tests.forEach( test => {
    assert.deepEqual(greatestNonadjacentSum(test.input), test.result)
});
