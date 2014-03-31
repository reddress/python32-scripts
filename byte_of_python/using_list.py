shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('I also have to buy rice')
shoplist.append('rice')
print('list is now', shoplist)

shoplist.sort()
print('sorted:', shoplist)

print('the second item is:', shoplist[1])
olditem = shoplist[1]

del shoplist[1]

print('I bought the', olditem)
print('list is:', shoplist)
