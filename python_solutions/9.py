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

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
def trip_finder():
    for a in range(200,675):
        for b in range(200,675):
            for c in range(200,675):
                if a<b and b<c:
                    if a**2 + b**2 == c**2 and a + b + c == 1000:
                        print(a * b * c)
                        break







trip_finder()
