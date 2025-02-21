#集合能消除重复元素
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
if 'apple' in basket:
    print("此元素在此集合中")

a = set('anjkfnklnakln')#可以用set函数创建集合，不能建立空集合，空集合只能用set函数建立，要不然会被视为字典
b = set('ksjhnkdnkmkd')
print(a&b)#对两个集合进行按位与，就是取两个集合都有的元素
print(a^b)#按位或，要存在于 a 或 b 中但非两者中皆有的元素