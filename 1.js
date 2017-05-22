//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

//Find the sum of all the multiples of 3 or 5 below 1000.

function multi(num){
  var numArr = []
  for (i = 1; i < num; i++)
    if (i % 3 === 0){
      numArr.push(i);
    } else if (i % 5 === 0) {
      numArr.push(i);
    }
  var sum = numArr.reduce(function(x,y) {return x + y;}, 0);
  console.log(sum);
}

multi(1000);

//233168
