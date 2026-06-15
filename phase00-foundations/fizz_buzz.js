// Problem: FizzBuzz

const fizzBuzz = (num) => {
  if (num % 3 === 0 && num % 5 === 0) {
    console.log("FizzBuzz");
  } else if (num % 3 === 0) {
    console.log("Fizz");
  } else if (num % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(num);
  }
};

const fizzBuzzNums = (num) => {
  for (let i = 1; i <= num; i++) {
    fizzBuzz(i);
  }
};

fizzBuzzNums(16);
