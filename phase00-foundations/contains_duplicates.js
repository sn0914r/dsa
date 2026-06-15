// Problem: Contains duplicates
// Approach: Brute force

const containsDuplicates = (arr) => {
  const tracker = {};

  for (let i of arr) {
    if (tracker[i]) {
      return true;
    }

    tracker[i] = 1;
  }

  return false;
};

const isContainsDups = containsDuplicates("Sivaa");
console.log(isContainsDups);
