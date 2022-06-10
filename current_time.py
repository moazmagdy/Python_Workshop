"""
This module outputs the current system time.
"""
import datetime
time = datetime.datetime.now().time()
"""
if __name__ == '__main__
It is used when you want to be able to execute
the script by itself, but also be able to import objects from the script as though it were a
regular module.
"""
if __name__ == '__main__':
    print(time)