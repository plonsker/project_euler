from functools import reduce

def diff_finder():
    nat_num_list = range(101)

    squared_results = list(map(lambda num: num**2, nat_num_list))
    product_of_squared_results = reduce((lambda x, y: x + y), squared_results)

    summed_results = (reduce((lambda x, y: x + y), nat_num_list))**2


    print summed_results - product_of_squared_results



diff_finder()
