

def reversel(lst):
    lst2 = []
    for x in reversed(range(len(lst))):
        lst2.append(lst[x])
    return lst2

print(reversel(['a', 'b', 'c', 'd']))
