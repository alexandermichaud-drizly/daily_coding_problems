const assert = require('assert');

const possibleDecodings = input => {
  
  if (input.length === 0) {
    return 1;
  }

  let one_digit_char = 0;
  let two_digit_char = 0;
  const leadingDigits = parseInt(input.substring(0,2));

  if (input[1] !== 0) {
    one_digit_char = possibleDecodings(input.substring(1));
  }


  if (leadingDigits < 27 && leadingDigits > 9) {
    two_digit_char += possibleDecodings(input.substring(2));
  } 

  return one_digit_char + two_digit_char;
};

const test_str_1 = '111';
const test_str_2 = '99999999';
const test_str_3 = '2132137211';
const test_str_4 = '2010112210122';
const test_str_5 = '2110';

assert.deepEqual(possibleDecodings(test_str_1), 3);
assert.deepEqual(possibleDecodings(test_str_2), 1); 
console.log(possibleDecodings(test_str_3));
console.log(possibleDecodings(test_str_4));
console.log(possibleDecodings(test_str_5));
