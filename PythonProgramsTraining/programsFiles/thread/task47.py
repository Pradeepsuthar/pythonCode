import time
import os
from threading import Thread

class Task(Thread):
    'to execute multiple task by threads'

    def run(self):
        'to execute task of thread'
        name = self.getName()
        if name=="1st":
            self.loop(100000)
        elif name=="2nd":
            self.playTime(60)
        else:
            self.copy("E://html/images/four.jpg",
             "E://GITS_3rd/four.jpg")

    def loop(self, MAX):
        'to execute loop for MAX times'
        for i in range(MAX+1):
            if i == MAX/2:
                input("Press Any key to continue : ")
            print("I is : %d " %i)
        else:
            print("Loop Done")
    
    def playTime(self, Time):
        'to consume/pass given time'
        for i in range(Time+1):
            print("Time : %d seconds" %i)
            # delay/sleep for 1 sec
            time.sleep(1)
        else:
            print("Time Completed")
    
    def copy(self, SFPATH, DFPATH):
        'to copy and paste'
        # finding given file size
        FS = os.stat(SFPATH).st_size
        # opening file in read binary mode
        FR = open(SFPATH, "rb")
        # opening file in write binary mode
        FW = open(DFPATH, "wb")
        for i in range(FS):
            # read & write byte
            FW.write(FR.read())
            print("%0.2f KB DONE" %(i/1024) )
        else:
            FR.close()
            FW.close()
            print("Copy Paste Done")
# creating object
t1 = Task()
t2 = Task()
t3 = Task()
t1.setName("1st")
t2.setName("2nd")
t3.setName("3rd")
t1.start()
t2.start()
t3.start()








