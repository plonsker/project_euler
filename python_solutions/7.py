# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def prime_finder(num):

    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print prime_finder(4)
