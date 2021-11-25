#!/usr/bin/env python

"""
Generate a bunch of 0 byte files with different mtimes for testing purposes.
"""

# import timedir
import os
import random
from datetime import datetime
import time
from pathlib import PurePath, Path


def mk_test_dir(d):
    Path(d).mkdir(parents=True, exist_ok=True)


def mk_mt_files(n, d):
    dp = Path(d)
    for f in range(n):
        fp = Path(str(f))
        df = dp / fp
        Path(df).touch()


def mod_time_epoch(year, month, day, hour, minute, second):
    tt = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    tte = time.mktime(tt.timetuple())
    return tte


def mod_mt(d):
    filelist = Path(d).glob('*')
    # Initial values don't really matter, what's important is getting a range of modified times later to test timedir.
    now = datetime.now()
    year = random.randint(1997, (now.year - 1))
    month = random.randint(1, 12)
    day = random.randint(1, 27)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    # testtime = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    # testtimeepoch = mod_time_epoch(testtime, year, month, day, hour, minute, second)
    # testtimeEpoch = time.mktime(testtime.timetuple())
    # nowTimeEpoch = time.mktime(datetime.timetuple(datetime.now()))
    counter = 0

    for file in filelist:
        # accessTime = time.mktime(datetime.timetuple(datetime.now()))
        ostinfo = str(datetime.fromtimestamp(os.stat(str(file)).st_mtime))
        print(str(file) + " original timestamp: " + ostinfo)
        counter +=1
        ctr = (counter % 5)

        if ctr == 1:
            year = random.randint(1997, (now.year - 1))
        elif ctr == 2:
            month = random.randint(1, 12)
        elif ctr == 3:
            day = random.randint(1, 27)
        elif ctr == 4:
            hour = random.randint(0, 23)
        elif ctr == 0:
            minute = random.randint(0, 59)

        testtimeepoch = mod_time_epoch(year, month, day, hour, minute, second)

        os.utime(str(file), (testtimeepoch, testtimeepoch))

        stinfo = os.stat(str(file))
        print(str(file) + " modified timestamp: " + str(datetime.fromtimestamp(stinfo.st_mtime)))


def main():
    mk_test_dir('tmp')
    mk_mt_files(100, 'tmp')
    mod_mt('tmp')

if __name__ == '__main__':
    main()