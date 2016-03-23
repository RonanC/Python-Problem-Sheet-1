def discount(init_price, disc_per):
    disc_num = disc_per / 100
    discount = init_price * (1 - disc_num)
    return discount

print('%.2f' % float(discount(10, 5)))
print(discount(29.90, 50))