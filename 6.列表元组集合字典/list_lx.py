# 简单用法
# sports = ["跑步","跳绳","爬山"]
# sports.append("羽毛球")#添加元素
# sports.insert(2,"俯卧撑")#插入元素
# sports.remove("羽毛球")#删除元素
# del sports[3]#删除指定下标的元素
# for sport in sports:
#     print(sport)

# print(sports[1:3])#左闭右开：起始下标包含，结束下标不包含。切片规则：slice[start:end]，其中 start 包含，end 不包含。也就是第2个元素到第3个。

#用列表实现堆栈（后进先出）
# stack = [1,2,3,4]
# stack.append(5)
# stack.append(6)
# print(stack)
# stack.pop()#pop函数不指定索引，自动弹出最后一个元素
# print(stack)
# print(stack.pop())

#用列表实现队列（先进先出）
# from collections import deque
# queue = deque(["jet","air","sui"])#名字都是瞎打的，现在是这三个人在排队
# queue.append("terry")#后来的排在后面
# queue.append("tom")#tom是最后来的
# print(queue.popleft())
# print(queue.popleft())