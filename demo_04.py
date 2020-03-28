# import random
# import time 
import pymysql
# while True:
    # for i  in range(10000):
        
        
    #     time.sleep(2)
    #     if i % 2 == 0:
            
    #         print(i )
        
# a = random.randint(1 , 100)
# print(a)
db = pymysql.connect(host = "127.0.0.1" , user = "root" , password = "123456" , db = "hdc")
cur = db.cursor()
try:
    cur.execute("select * from t_class;")
    res = cur.fetchall()
    print(res)
    for i  in res:
        print(i)
except Exception as e:
    print("SQL语句写错!" , e)
    








# light = {"红灯":30 , "绿灯":20 , "黄灯":10}
# for i in light:
#     for j in range(light[i]):
#         print("{}还有{}秒!".format(i , light[i]-j))
#     for k in range(3):
#         print()    
    
