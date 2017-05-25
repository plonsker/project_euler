// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.

function pali(num){
  var numStr = num.toString();
  var numArr = numStr.split('');
  console.log(numArr);
  console.log(numArr.reverse())
  console.log(numArr.reverse().join(''))
  if (numArr.join('') === numArr.reverse().join('')){
    return true;
  } else {
    return false;
  }

}

pali(3333)
