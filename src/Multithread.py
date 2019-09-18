from threading import *
from time import sleep

class Hi(Thread):
    def run(self):  # multi thread work only if name of the method is run
        for i in range(5):
            print("Hi...")
            sleep(2)

class Hello(Thread):
    def run(self):  # multi thread work only if name of the method is run
        for i in range(5):
            print("Hello++++++++")
            sleep(2)
        
h1 = Hi()
ho1 = Hello()
h1.start() # this will trigger method which name is run
sleep(0.2)
ho1.start() # this will trigger method which name is run
print("Started both thread..")

h1.join()
ho1.join()
print("==============Done===============")