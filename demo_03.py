light = {'红灯':30 ,
        '绿灯':35 , 
        '黄灯':3 }
for i in light :
    for j in range(light[i]):
        print("{}还有{}秒".format(i,light[i]-j))
        
    print("================================================================================================")
