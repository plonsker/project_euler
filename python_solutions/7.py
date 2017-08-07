# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

def is_prime(num):

    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print is_prime(7)


def prime_collector(num_range):
    prime_list = []

    for num in num_range:
        if is_prime(num):
            prime_list.append(num)

    print prime_list[10001]

prime_collector(range(2,10000))
