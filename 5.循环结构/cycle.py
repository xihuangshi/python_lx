for i in range(10):
    print("hello,world")

for _ in range(10):
    print("对于不需要用到循环变量的for-in循环结构，可以把循环变量命名为_")

#1到100求和
# range(101)生成的是0,1,2,...,100，循环101次，计算的是0到100的和=5050
# range(1, 101)生成的是1,2,3,...,100，循环100次，计算的是1到100的和=5050
# range(100)生成的是0,1,2,...,99，循环100次，计算的是0到99的和=4950
total = 0
for i in range(1,101):
    total +=i
print(total)

#while循环求0到100的和

total = 0
i = 1
while i <= 100:
    total += i
    i +=1
print(total)

#break 和 continue
#当数大于五十的时候直接结束循环
total = 0
for i in range(1,101):
    if i > 50:
        break
    total +=i
print(total)

#只求奇数和
total = 0
for i in range(1,101):
    if i % 2 == 0:
        continue
    total +=i
print(total)