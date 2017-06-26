

def pali():
    num_list = range(100,1000)
    num_list_2 = range(100,1000)

    product_list = []

    for num in num_list:
        for num_2 in num_list_2:
            potential_pali = str(num * num_2)
            if potential_pali == potential_pali[::-1]:
                print potential_pali
                product_list.append(potential_pali)

    product_list = map(int, product_list)

    for x in sorted(product_list):
        print x



pali()
