// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

function primeFact(num){
  var numArr = [];
  var numCheckArr = [];

  for (x = 2; x <= num; x++){
    while (num % x === 0){
      numArr.push(x)
    }
  }
  return numArr;
}

primeFact(13195);
