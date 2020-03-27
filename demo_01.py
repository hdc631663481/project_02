import time
# import random
# def add(a , b):
#     return a + b 
# c = add(2 , 6)
# print(c)


# try:
#     1 + 2
# except :
#     print("代码错误!)
# print("继续执行!")

# name = input("请输入你的名字: ")
# age  = input("请输入你的年龄: ")
# try:
#     if  int(age) > 18:

#         print(name, "成年了!")
#     else:
#         print(name , "未成年!")
# except  Exception as  e:
#     print("代码报错!" , e)


# try:
#     print(1 + jhjh)
# except Exception  as e:
#     print("上面的代码写错了!" , e)



# name = input("请输入你的名字: ")
# age  = input("请输入你的年龄: ")
# try: 
#     if int(age) > 18:
#         print(name , "成年了!")
#     else:
#         print(name , "未成年!")
# except:
#     pritn("请输入正确的年龄!")
# for i  in range(10):
#     time.sleep(1)
#     print(i)
 

# a = random.randint(1 , 10)
# print(a)



# def chechuserinfo(username ):
#     """
#         验证账号信息!


#     """
#     if 5 <= len(username) <= 10:
#         if username[0].islower():
#             print("您输的的账号是: " , username)
#         else:
#             print("账号开头必须以小写字母开头!")
#     else:
#         print("输入的账号不符合长度规范!")


# a = input("请输入你的账号: ")
# chechuserinfo(a)




# def add(a , b):
  
        
#     if type(a) is int  and type(b) is int :
#         print( a + b)
#     else:
#         return "请输入数字!" 


# c = add(5, 5)

# print(c)


# a = []
# print(a.append("哈哈"))
# print(a.count("哈哈"))





# a = [1 , 4, 4, "ha"]
# x = a.index("ha")

# print(a[x])

# x = 0 
# shuzi = []
# for i  in range(10):

#     shuzi.append(int(input("请输入数字: ")))
    
# print(shuzi)
# for j in shuzi:
#     if j % 7 == 0:
#         print(j)
#         x = 1
#         break
# if x == 0:
#     print("not exits!")   
# class Friend():
#     def __init__(self , sex , high , weight , hair , age):
#         self.sex    = sex
#         self.high   = high
#         self.weight = weight
#         self.hair   = hair
#         self.age    = 20    
#     def caiyi(self, num):
#         if num == 1:
#             print("爱好是:sing!")
#         if num == 2:
#             print("爱好是:dance!")
#         if num == 3:
#             print("爱好是:drawing") 
#     def cook(self):
#         print("精通八大厨艺!")
#     def work(self):
#         print("working!")
# friend = Friend("女" , "170cm" , "50kg" , "大波浪" , 20)
# print("头发:" , friend.hair)
# print("身高:" , friend.high)
# print("体重:" , friend.weight)
# print("性别:" , friend.sex)
# print("年龄:" , friend.age)



# friend.caiyi(1)
# friend.cook()
# friend.work()



# class Car():
#     def __init__(self , price , color , brand):
#         self.price = price
#         self.color = color
#         self.brand = brand
#     def fly(self):
#         print("汽车飞起来!")

#     def qianshui(self):
#         print("汽车会潜水!")
# car = Car("100" , "白色" , "fengtian")
# print("价格:" , car.price)
# print("颜色:" , car.color)
# print("价格:" , car.brand)
# car.fly()
# car.qianshui()



# class SubCar(Car):
#     def fly(self):
#         print("汽车飞飞飞飞起来!")
#     def pao(self):
#         print("汽车会跑!")
# car2 = SubCar("178" , "蓝色" , "奥迪")
# print("价格:" , car2.price)
# print("颜色:" , car2.color)
# print("价格:" , car2.brand)

# car2.fly()
# car2.qianshui()

# car2.pao()






now = time.strftime('%y-%m-%d %H:%M:%S')

text = input('请输入今天的事情!:')
with  open('F:\日记.txt' , 'a' , encoding='utf8') as f:
    f.write(now + '\n')
    f.write(text + '\n')



    