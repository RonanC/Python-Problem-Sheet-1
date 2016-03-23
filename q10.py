# flatten list using global list and recursion
# could possibly use iterators, generators, yield and/or list comprehension.

lst = ['a', ['b', 'c'], 'd', ['e', ['f']], 'g']
letters = ['a', 'b', 'c', 'd']
# V1
# def flatten(lst):
#     for item in range(len(lst)):
#         if isinstance(lst[item], list):
#             flatten(lst[item])
#         else:
#             print(lst[item])

# V2
lst_flat = []


def flatten(lst):
    for item in range(len(lst)):
        if isinstance(lst[item], list):
            flatten(lst[item])
        else:
            lst_flat.append(lst[item])
flatten(lst)
print(lst_flat)
