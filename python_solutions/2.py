def fib():
    x = 0
    y = 1

    total = 0

    # for x in range(0, 4000000):
    while y < 4000000:
        z = x
        x = y
        y = z + x
        if y % 2 == 0:
            total = total + y

    print total

fib()
