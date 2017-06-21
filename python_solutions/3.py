#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def prime_finder(num):
    num_list = []

    for possible_factor in range(2,num):
        if num % possible_factor == 0:
            num_list.append(possible_factor)

    print num_list

    

    for factor in num_list:
        if factor %  3 == 0:
            num_list.remove(factor)

    print num_list

prime_finder(13195)
