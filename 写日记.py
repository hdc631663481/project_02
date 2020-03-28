import time
now = time.strftime('%y-%m-%d %H:%M:%S')

text = input('请输入今天的事情!:')
with  open('F:\写日记.txt' , 'a' , encoding='utf8') as f:
    f.write(now + '\n')
    f.write(text + '\n')
    f.write('=======================================================' + '\n')