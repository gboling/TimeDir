#!/usr/bin/env python

"""
Generate a bunch of 0 byte files with different mtimes for testing purposes.
"""

# import timedir
import os
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


def mod_time_epoch(tt, year, month, day, hour, minute, second):
    tt = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    print(tt)
    tte = time.mktime(tt.timetuple())
    return tte


def mod_mt(d):
    filelist = Path(d).glob('*')
    # Initial values don't really matter, what's important is getting a range of modified times later to test timedir.
    year = 1997
    month = 10
    day = 22
    hour = 19
    minute = 39
    second = 0
    testtime = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    testtimeepoch = mod_time_epoch(testtime, year, month, day, hour, minute, second)
    # testtimeEpoch = time.mktime(testtime.timetuple())
    # nowTimeEpoch = time.mktime(datetime.timetuple(datetime.now()))
    counter = 0

    for file in filelist:
        # accessTime = time.mktime(datetime.timetuple(datetime.now()))
        print(file)
        counter +=1
        ctr = (counter % 5)

        if ctr == 1:
            year +=1
        elif ctr == 2:
            month +=1
            if month > 12:
                month = 1
        elif ctr == 3:
            day +=1
            if day > 27:
                day = 1
        elif ctr == 4:
            hour +=1
            if hour > 23:
                hour = 0
        elif ctr == 0:
            minute +=1
            if minute > 59:
                minute = 0

        testtimeepoch = mod_time_epoch(testtime, year, month, day, hour, minute, second)

        os.utime(str(file), (testtimeepoch, testtimeepoch))

        stinfo = os.stat(str(file))
        print("Modified:")
        print(stinfo.st_mtime)
