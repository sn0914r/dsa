// Problem: Find maximum and minimum in an array

const findMaxMinNums = (nums) => {
  let minimum = +Infinity;
  let maximum = -Infinity;

  for (let num of nums) {
    if (num > maximum) {
      maximum = num;
    }

    if (num < minimum) {
      minimum = num;
    }
  }

  return {
    maximum,
    minimum,
  };
};

const result = findMaxMinNums([2, 7, 11, 15, 6, 8]);
console.log(result);
