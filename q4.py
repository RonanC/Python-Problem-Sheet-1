# using list comprehension


def inter(lst1, lst2):
    lst3 = [val for val in lst1 if val in lst2]
    return lst3

print(inter(['a', 'b', 'c', 'd'], ['c', 'd', 'e']))
