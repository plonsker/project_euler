// The prime factors of 13195 are 5, 7, 13 and 29.
//
// What is the largest prime factor of the number 600851475143 ?

function primeFact(num){
  var numArr = [];
  // var numCheckArr = [];

  for (x = 2; x <= num; x++){
    while (num % x === 0){
      numArr.push(x);
      num = num / x;
    }
  }
  return numArr[numArr.length-1];
}

primeFact(600851475143);


// function primeFact(num){
//   var numArr = [];
//   var numCheckArr = [];
//   //evenly divisible
//   // if (num % x === 0 )
//   for (x = 1; x <= num; x++){
//     if (num % x === 0){
//       numArr.push(x);
//     }
//   }
//   // at this point x is the number we are trying to determine if prime
//   // range of 1 through x
//   console.log(numArr);
//   for (var x in numArr){
//     for (i = 1; i <= numArr[x]; i++){
//       if (numArr[x] % i === 0){
//         console.log(numArr[x]);
//       }
//     }
//   }
//   // numArr.pop();
//   console.log(numArr);
// }
//
// primeFact(13195);
