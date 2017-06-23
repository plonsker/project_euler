def is_prime(num):

    num_range = range(2,num-1)

    for x in num_range:
        if num % x == 0:
            print "not prime"
is_prime(5)
