#字典就是键值对 
user = {'username' :"admin",'password':123456}
print(user['username'])
print(user['password'])

for k,v in user.items():#可以用items函数提取键值
    print(k,v)