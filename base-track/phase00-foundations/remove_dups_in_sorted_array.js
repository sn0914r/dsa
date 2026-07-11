// Problem: Remove duplicates in sorted array - in-place, return new length

const removeDups = (sortedArray) => {
  let j = 0;

  for (let i = 0; i < sortedArray.length - 1; i++) {
    if (sortedArray[i] !== sortedArray[i + 1]) {
      const temp = sortedArray[i];
      sortedArray[i] = sortedArray[j];
      sortedArray[j] = temp;

      j += 1;
    }
  }

  sortedArray[j] = sortedArray[sortedArray.length - 1];

  return j + 1
};

const test = [1, 2, 2, 3, 3, 3, 4, 4];
const noDupsLength = removeDups(test);
console.log(noDupsLength)
