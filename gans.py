from time import gmtime, strftime
import os
import datetime
t=datetime.datetime.now().time()
t=str(t)
t=t.split(":")
f=int(t[0])+1
print(f)
def dwnld(fil) :
    import wget
    wget.download(fil, '') 

def dumpall() :
    import datetime
    import os
    import time
    now = datetime.datetime.now() 
    time.sleep(10)
    dwnld('https://storage.googleapis.com/9gans/mini/1.jpg?1581947061587')
    dwnld('https://storage.googleapis.com/9gans/mini/2.jpg?1581947061588')
    dwnld('https://storage.googleapis.com/9gans/mini/3.jpg?1581947061588')
    dwnld('https://storage.googleapis.com/9gans/mini/4.jpg?1581947061588')
    dwnld('https://storage.googleapis.com/9gans/mini/5.jpg?1581947061588')
    dwnld('https://storage.googleapis.com/9gans/mini/6.jpg?1581947061589')
    dwnld('https://storage.googleapis.com/9gans/mini/7.jpg?1581947061589')
    dwnld('https://storage.googleapis.com/9gans/mini/8.jpg?1581947061589')
    dwnld('https://storage.googleapis.com/9gans/mini/9.jpg?1581947061590')
    os.rename('1.jpg', str(str(now.timestamp())+'1.jpg'))
    os.rename('2.jpg', str(str(now.timestamp())+'2.jpg'))
    os.rename('3.jpg', str(str(now.timestamp())+'3.jpg'))
    os.rename('4.jpg', str(str(now.timestamp())+'4.jpg'))
    os.rename('5.jpg', str(str(now.timestamp())+'5.jpg'))
    os.rename('6.jpg', str(str(now.timestamp())+'6.jpg'))
    os.rename('7.jpg', str(str(now.timestamp())+'7.jpg'))
    os.rename('8.jpg', str(str(now.timestamp())+'8.jpg'))
    os.rename('9.jpg', str(str(now.timestamp())+'9.jpg'))

dumpall()
while True :
    import datetime
    t=datetime.datetime.now().time()
    t=str(t)
    t=t.split(":")
    print(t[0],f)
    if t[0]==f :
        print('dumping...')
        dumpall()
        if t[0]== 23 :
            f=0
        else :
            f=int(t[0])+1

