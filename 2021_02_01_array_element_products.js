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

const test_list_1 = [1,2,3,4,5];

console.log(getProducts(test_list_1));
console.log(getProductsWithoutDivision(test_list_1));
