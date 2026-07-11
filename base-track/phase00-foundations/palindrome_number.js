// Problem: Palindrome Number

const isPalindromeNumber = (num) => {
  const originalNum = num;
  let revNum = 0;
  while (num) {
    const digit = num % 10;
    revNum = revNum * 10 + digit;
    num = Math.floor(num / 10);
  }

  return revNum === originalNum;
};  

console.log(isPalindromeNumber(676));
