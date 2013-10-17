#!/usr/bin/python
import os
import threading
import time
import Queue
import signal
import subprocess
import collections

q = Queue.Queue()

ls = collections.deque( ["5XTtUYV.jpg", "dwarfEntrance.png", "CD16E4u.jpg" ])

def showstuff():
    while ( True ):
        sb = subprocess.Popen(["feh", "-Z", "-g" ,"800x400",ls[0]])
        while( True ):
            a = q.get()
            print a
            if ( a == "stop" ):
                sb.terminate()
                exit()
            elif ( a == "next"):
                ls.rotate(1)
                sb.terminate()
                break
    

def amin():
    showOff = threading.Thread(target=showstuff)
    showOff.start()
    for i in range(6):
        time.sleep(5)
        q.put("next")
    time.sleep(2)
    q.put("stop")

amin()
