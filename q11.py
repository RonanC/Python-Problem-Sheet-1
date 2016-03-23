# fibbonachi sequence


def fibo():
    # returns a, then goes to next iteration
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + a


def firstn(g, n):
    for i in range(n):
        yield g.__next__()


print(list(firstn(fibo(), 10)))
