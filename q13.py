"""
My implementation of Heaps algorithm
"""


def heap_perm(n, A):
    if n == 1:
        yield A
    else:
        for i in range(n-1):
            for hp in heap_perm(n-1, A):
                yield hp
            j = 0 if (n % 2) == 1 else i
            A[j],  A[n-1] = A[n-1], A[j]
        for hp in heap_perm(n-1, A):
            yield hp


def perm_num(lst):
    count = 1
    for x in range(len(lst)):
        y = x+1
        count = count * y
    return count


def heap_gen(gen, n):
    perms = []
    for x in range(n):
        perms.append(''.join(list(gen.__next__())))
    return perms


lst = ['a', 'b', 'c', 'd']
gen = heap_perm(len(lst), lst)
num = perm_num(lst)
perms = heap_gen(gen, num)
print(perms)
