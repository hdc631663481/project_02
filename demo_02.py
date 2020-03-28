# def userinfor(username , password):
#     userinfo = {}

#     if 5 <= len(username) <= 10:
#         if username[0].islower():
#             if 6 <= len (password) <= 12:
#                     print("注册成功!")
#                     userinfo["账号"] = username
#                     userinfo["密码"] = password
#                     print(userinfo)
#             else:
#                 print("密码长度6-12位!")
                
#         else:
#                 print("账号开头必须小写!")
#     else:
#             print("请输入5-10位的账号!")    

# username = input("请输入账号: ")
# password = input("请输入密码: ")
# userinfor(username , password)





userinfo = {}


def userinfor(username , password):
    
    if 5 <= len(username) <= 10:
        if username[0].islower():
            return True
        else:
            return "账号开头必须小写!"
    else:
        return "请输入5-10位的账号!" 

username = input("请输入账号: ")
password = input("请输入密码: ")
userinfor(username , password)



if userinfor(username , password)  == True:
    if 6 <= len (password) <= 12:
        userinfo["账号"] = username
        userinfo["密码"] = password
        print(userinfo)
    else:
        print("密码长度6-12位!")
else:
    print(userinfor(username , password))


