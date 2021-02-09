const schedule = async (f, n) => {
  return (new Promise(r => setTimeout(r, n)).then(f));
};

const test_func = () => console.log('Done');

schedule(test_func, 3000);
