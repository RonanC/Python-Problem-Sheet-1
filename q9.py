

def sum35(n):
    sum = 0
    for x in range(1, n):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum

print(sum35(1000))
