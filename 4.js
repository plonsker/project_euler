// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.

// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.

// function pali(num){
//   var numStr = num.toString();
//   var numArr = numStr.split('');
//   console.log(numArr);
//   console.log(numArr.reverse())
//   console.log(numArr.reverse().join(''))
//   if (numArr.join('') === numArr.reverse().join('')){
//     return true;
//   } else {
//     return false;
//   }
//
// }
//
// pali(3333)


// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.

// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.

// function pali(num){
//   var numStr = num.toString();
//   var numArr = numStr.split('');
//   console.log(numArr);
//   console.log(numArr.reverse())
//   console.log(numArr.reverse().join(''))
//   if (numArr.join('') === numArr.reverse().join('')){
//     return true;
//   } else {
//     return false;
//   }
//
// }
//
// pali(3333)


function pali(num){

  var numStr = num.toString();
  var numArr = numStr.split('');
  console.log(numArr);
  console.log(numArr.reverse());
  console.log(numArr.reverse().join(''));
  if (numArr.join('') == numArr.reverse().join('')){
    return true;
  } else {
    return false;
  }

}

function paliFinder(){
  var arr1 = [];
  var arr2 = [];
  var crossCheck = [];

  for (i = 1; i < 1000; i+=1){
    arr1.push(i);
    arr2.push(i);
    }


  for (var x in arr1){
    for (var y in arr2){
        var crossProduct = arr1[x] * arr2[y];
        crossCheck.push(crossProduct);

        //I get it now. I'm just pulling the first one.
        if (pali(crossProduct)){
          console.log("--------------");
          console.log(crossProduct);
          console.log("--------------");
          {break;}
        }
    }
  }

}


paliFinder();
