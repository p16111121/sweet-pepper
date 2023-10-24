#pip install apscheduler
from apscheduler.schedulers.background import BackgroundScheduler 
from upload_imgbb import geturlandtime
from saveimgurl import inserturl
from catch_time import rmoldimg
import cv2
import time,datetime
import os
import threading
path="./historypic" #儲存位置
state=0

if os.path.exists(path)== False:
    os.makedirs(path)
def takephoto():    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()   
    ret,frame = cap.read()
    if ret:
        print("Start take a picture...")
        loctime= time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
        filename=path+'/{0}.jpg'.format(loctime)
        cv2.imwrite(filename,frame)
        print("Success save "+filename)
        displayurl,updatetime,time_sec=geturlandtime(filename,loctime)
        insertthreading=threading.Thread(target=inserturl,args=(displayurl,updatetime,time_sec))
        insertthreading.start()
        insertthreading.join()
    print("take picture is done")
    cap.release()

if __name__=='__main__':
    print("Start to run...")
    # 定義BlockingScheduler BackgroundScheduler
    sched = BackgroundScheduler()
    sched.add_job(takephoto, 'cron', minute = '*/20',jitter=30)
    sched.start()
    
    #sched1 = BackgroundScheduler()
    #sched1.add_job(rmoldimg, 'cron', day_of_week = 'sun',hour = 23,minute = 59,jitter=30,args= (path,250))
    #sched1.start()
    print('Press Ctrl+{0} to exit'.format('C' if os.name == 'nt' else 'C'))
    try:
        while True:
            state=state+1
            if state==1000:
                state=0
    except KeyboardInterrupt as error:
        sched.shutdown()
        print("Stop because {}".format(type(error)))
        