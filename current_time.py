"""
This module outputs the current system time.
"""
import datetime
time = datetime.datetime.now().time()
if __name__ == '__main__':
    print(time)