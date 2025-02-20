a = 1
b = 2
c = 3 
d = 4
print(a+b)#加法
print(b-1)#减法
print(c*d)#乘法
print(d/c)#除法
print(d//c)#整除
print(d%c)#求模
print(c<<1)#左移一位
print(c>>1)#右移一位

# 按位与：
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1
print(c&d)
# 按位或：
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1
print(c|d)
# 按位非：补码转源码取反加1
# ~0 = 1
# ~1 = 0
print(~d)
# 异或：
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
print(c^d)