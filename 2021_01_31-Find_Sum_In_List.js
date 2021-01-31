// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

const sumExists = (list, k) => {
    let sum_table = {};

    for(let i = 0; i < list.length; i++) {
        let n = list[i];
        if (sum_table[n]) {
            return true;
        }
        sum_table[(k - n)] = true;
    }
    return false;
};

const test_list_1 = [10,0,5,3,4];
const test_sum_1  = 14;

console.log(sumExists(test_list_1, test_sum_1));