import sys
import time
for i in range(10):    
    sys.stdout.write('\rloading |')
    time.sleep(0.1)
    sys.stdout.write('\rloading /')
    time.sleep(0.1)
    sys.stdout.write('\rloading -')
    time.sleep(0.1)
    sys.stdout.write('\rloading \\')
    time.sleep(0.1)
    sys.stdout.write('\rDone!     ')