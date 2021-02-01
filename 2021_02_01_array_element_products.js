const performance = require('perf_hooks').performance;

const getProducts = list => {
  const product = list.reduce((a, n) => a * n);

  const listFilled = Array(list.length).fill(product);
  
  let newList = Array();

  for (let i = 0; i < list.length; i++) {
    newList[i] = listFilled[i] / list[i];
  }
  return newList;
}

const getProductsWithoutDivision = list => {
  let outputList = Array(list.length).fill(1);

  list.forEach( (n, i) => {
    for ( let j = 0; j < list.length; j++) {
      if (j !== i) {
        outputList[i] *= list[j];
      }
    }
  });

  return outputList;
}

const getProductsWithoutDivisionOptimized = list => {
  let outputList = Array(list.length);
  for (let i = 0; i < list.length; i++) {
    outputList[i] = list.slice(0,i).concat(list.slice((i + 1), list.length)).reduce((a, r) => a * r);
  }
  return outputList;
}

const test_list_1 = [1,2,3,4,5,6,7,8,9,10,11,12];

const t1 = performance.now();
getProducts(test_list_1);
const t2 = performance.now();

const t3 = performance.now();
getProductsWithoutDivision(test_list_1);
const t4 = performance.now();

const t5 = performance.now();
getProductsWithoutDivisionOptimized(test_list_1);
const t6 = performance.now();

console.log(`Efficiency of division: ${t2 - t1}`);
console.log(`Efficiency of O(n^2) solution: ${t4 - t3}`);
console.log(`Efficiency of efficient solution: ${t6 - t5}`);
