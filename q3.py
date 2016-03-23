def appearances(item, items):
    count = 0
    for item_num in range(0, len(items)):
        if item == items[item_num]:
            count += 1
    return count

print(appearances('a', ['a', 'b', 'c', 'a', 'a']))
