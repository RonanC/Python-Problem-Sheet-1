

def to_binary(n):
    lst = []
    while n > 0:
        a = int(float(n % 2))
        lst.append(a)
        n = int(n / 2)
    return list(reversed(lst))


def convert(lst):
    str_bin = ''
    for x in range(len(lst_bin)):
        str_bin += str(lst_bin[x])
    return str_bin


lst_bin = to_binary(21)
str_bin = convert(lst_bin)

print(str_bin)
