const assert = require('assert')

// O(n!) solution
/*
const greatestNonadjacentSum = list => {
  
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

  return adjacent > max ? adjacent : max;
};
*/
const greatestNonadjacentSum = list => {
    let included = 0;
    let excluded = 0;
    let new_excluded = 0;

    list.forEach( n => {
      new_excluded = Math.max(excluded, included);

      included = excluded + n;
      excluded = new_excluded; 
    });

    return Math.max(included, excluded);
};

const tests = [
  {input: [2,4,6,2,5], result: 13},
  {input: [5,1,1,5],   result: 10}
];

tests.forEach( test => {
    assert.deepEqual(greatestNonadjacentSum(test.input), test.result)
});
