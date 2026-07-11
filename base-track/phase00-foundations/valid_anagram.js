// Problem: Valid Anagram
// Approach: Brute force

const validAnagram = (word1, word2) => {
  if (word1.length !== word2.length) {
    return false;
  }

  let chars = {};

  for (let ch of word1) {
    if (Object.hasOwn(chars, ch)) {
      chars[ch] += 1;
      continue;
    }
    chars[ch] = 1;
  }

  for (let ch of word2) {
    if (Object.hasOwn(chars, ch)) {
      chars[ch] -= 1;

      if (chars[ch] === 0) {
        delete chars[ch];
      }
    }
  }

  if (Object.keys(chars) > 1) {
    return false;
  }
  return true;
};

const isAnagram = validAnagram("dusty", "study");
console.log(isAnagram);
