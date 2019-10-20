def fibonacci(n):
    x0 = 0
    x1 = 1
    fib_series = []
    fib_series.append(x0)
    fib_series.append(x1)

    if(not isinstance(n, int)):
        raise Exception("Invalid input type. Should be single integer number.")

    if n < 0:
        raise Exception("Input is incorrect, should be >0.")
    elif n == 0:
        return [0]
    elif n == 1:
        return[0, 1]
    else:
        for i in range(n-1):
            fib_series.append(fib_series[-1]+fib_series[-2])

    return fib_series
