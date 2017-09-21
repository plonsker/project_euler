# def trip(num_1,num_2,num_3):
#     print(num_1**2)
#     print(num_2**2)
#
#     print(num_1**2 + num_2**2)
#     print(num_3**2)
#
#     print(num_1 + num_2 + num_3)
#
# trip(3,4,5)


# def trip_finder():
#     num_list = range(1001)
#     i = 1
#     j = 2
#
#     for num in num_list:
#         print(num)
#         print(num+i)
#         print(num+j)
#         print("")
#         print(num + (num+i) + (num+j))
#         print("")
#         print("")
#         j += 1
#         if num**2 + (num+i)**2 == (num+j)**2 and num + num_1 + num_2 == 1000:
#             print(num)
#             print(num+i)
#             print(num+j)
#         else:
#             trip_finder
#
#
# trip_finder()


def trip_finder():
    # the basic logic
    num_list = range(1,1001)

    for num in num_list:
        for num_2 in num_list:
            for num_3 in num_list:
                if num < num_2 < num_3:
                    if num**2 + (num_2)**2 == (num_3)**2 and num + num_2 + num_3 == 1000:
                        print(num)
                        print(num_2)
                        print(num_3)
                        break
                    else:
                        print("")
                        print(num)
                        print(num_2)
                        print(num_3)
                        print("")
                        print("-----------")
                        print("~----------")
                        print("-~---------")
                        print("--~--------")
                        print("---~-------")
                        print("----~------")
                        print("-----~-----")
                        print("------~----")
                        print("-------~---")
                        print("--------~--")
                        print("---------~-")
                        print("----------~")







trip_finder()
