def divisible(num):
    num_list = range(1,20)
    print all(map(lambda y: num%y == 0, num_list))

divisible(500)

# range(1,100,000,00)
#
# def small_checker(num_input):
#
#     num_list = range(1,20)
#
#     for num in num_input:
#         print all(map(lambda y: num % y == 0, num_list))
#         print num
#         if all(map(lambda y: num % y == 0, num_list)):
#             break
#
# small_checker(range(1,10000000))
