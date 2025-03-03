def fibancciSeries(n):
    fib_series = [0, 1]

    for i in range(2,n):
        next_value = fib_series[-1]  + fib_series[-2]
        fib_series.append(next_value)
    return fib_series

print(fibancciSeries(10))