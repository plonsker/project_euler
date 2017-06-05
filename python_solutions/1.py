



def multi(num):
    total = 0

    num_range = range(0,num)

    for x in num_range:
        if x % 3 == 0 or x % 5 == 0:
            total = total + x

    print total


    # while i < 0:
    #     if i % 3 === 0:
    #         num_arr.append(i)
    #     elif i % 5 === 0:
    #         num_arr.append(i)
    #     i++
    #
    # for multiple in num_arr:
    #     print multiples

multi(1000)
