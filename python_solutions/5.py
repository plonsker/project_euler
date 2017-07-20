# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def divisible(num):
    num_list = range(1,20)

    for num_item in num_list:
        if num % num_item != 0:
            return False

    return True

    # return all(map(lambda y: num % y == 0, num_list))

i = 1

while not divisible(i):
    i += 1

print i
