#Simple example showing how to create a process in python , how to fork it in run-time.

import os

def child():
   print('\nSpawning a new child process here with PID ',  os.getpid())
   os._exit(0)  

def parent():
   while True:
      #fork a new process and assign the newpid
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("Created parent process : %d, child: %d\n" % pids)
      reply = input("q - quit / c - new fork")
      if reply == 'c': 
          continue
      else:
          break
print("########################################################################")
print("Lets start to fork, sample program to showcase how process and fork work")

parent()

print("Exiting Program")
print("########################################################################")