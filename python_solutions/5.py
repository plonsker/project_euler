# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# def divisible(num):
#     num_list = range(1,10)
#     print all(map(lambda y: num%y == 0, num_list))
#
# divisible(2520)

def small_checker(num_input):

    num_list = range(1,20)

    for num in num_input:
        print all(map(lambda y: num%y == 0, num_list))
        print num
        if all(map(lambda y: num%y == 0, num_list)):
            break

small_checker(range(1,100000000))
