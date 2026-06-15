// Problem: Two Sum
// Approach: Brute Force

const twoSum = (arr_nums, target) => {
  for (let i = 0; i < arr_nums.length; i++) {
    for (let j = i + 1; i < arr_nums.length; j++) {
      if (arr_nums[i] + arr_nums[j] === target) {
        return [i, j];
      }
    }
  }
};
const nums = [2, 7, 11, 15];
const target = 9;

result = twoSum(nums, target);
console.log(result);
