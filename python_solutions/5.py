# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def small_checker():

    num_list = range(20,1000000)
    divider_list = range(1,20)

    for num in num_list:
        res = all([num%x==0 for x in range(1,20)])
        if res == True:
            print num


small_checker()
