# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# def is_prime(num):
#
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
#
# print is_prime(7)



def is_prime(num):

    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def prime_creator():

    num = 1
    prime_count = 0
    while prime_count < 10001:
        num += 1
        if is_prime(num):
            prime_count += 1

    print num


prime_creator()
