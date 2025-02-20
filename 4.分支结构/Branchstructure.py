# a = input("请输入密码")#input输入的是字符串，需要进行转换
# if int(a) == 5555:
#     print("登录成功")
# else:
#     print("密码错误")

status_code = int(input("请输入状态码"))
match status_code:
    case 200: description = "ok"
    case 404: description = "Not found"
    case 500: description = "errer"
    case _: description = 'Unknown Status Code'#_是通配符，上面没有匹配上就会选择_
print("状态码：",description)