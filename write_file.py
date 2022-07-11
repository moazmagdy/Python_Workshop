"""
This script write date and time to a file.
"""
from datetime import datetime
import time

f = open('log.txt', "w+")

for i in range(10):
    print(datetime.now().strftime("%Y/%m/%d_%H:%M:%S - "), i)
    f.write(datetime.now().strftime("%Y/%m/%d_%H:%M:%S - "))
    time.sleep(2)
    f.write(str(i))
    f.write('\n')
f.close()