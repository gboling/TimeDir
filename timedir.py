#!/usr/bin/env python

"""
    To make a directory tree like this: output_dir/year/month/day/hour/min
    Also get mtime of an arbitrary file and returns namedtuple for datetime and elements.
    Returns a namedtuple with values for each level at time of function call.

    Copyright (C) 2016 J. Grant Boling [gboling]at[gmail]dot[com]

"""

import datetime
import os
import argparse

from pathlib import Path, PurePath
from collections import namedtuple

timedir_ntuple = namedtuple('timedir', 'yearDir monthDir dayDir hourDir minDir')
mtimedir_ntuple = namedtuple('mtimedir', 'yearDir monthDir dayDir hourDir minDir mtime mdtime')


def nowdir(output_dir):
    now = datetime.datetime.now()
    print now
    n_year = now.strftime('%Y')
    n_month = now.strftime('%m')
    n_day = now.strftime('%d')
    n_hour = now.strftime('%H')
    n_min = now.strftime('%M')
    od_now = PurePath(output_dir).joinpath(n_year, n_month, n_day, n_hour, n_min)
    print od_now
    # timedir_ntuple(*od_now)
    # year_dir =  timedir_ntuple.n_year
    # month_dir = timedir_ntuple.n_month
    # day_dir = timedir_ntuple.n_day
    # hour_dir = timedir_ntuple.n_hour
    # min_dir = timedir_ntuple.n_min
    # return timedir_ntuple(year_dir, month_dir, day_dir, hour_dir, min_dir)
    return outdir_now


def mtimedir(mtime_file, output_dir):
    mtime = os.path.getmtime(mtime_file)
    mdtime = datetime.datetime.fromtimestamp(mtime)
    m_year = mdtime.strftime('%Y')
    m_month = mdtime.strftime('%m')
    m_day = mdtime.strftime('%d')
    m_hour = mdtime.strftime('%H')
    m_min = mdtime.strftime('%M')
    mtyear_dir = os.path.join(mtoutput_dir, m_year)
    mtmonth_dir = os.path.join(mtyear_dir, m_month)
    mtday_dir = os.path.join(mtmonth_dir, m_day)
    mthour_dir = os.path.join(mtday_dir, m_hour)
    mtmin_dir = os.path.join(mthour_dir, m_min)

    return mtimedir_ntuple(mtyear_dir, mtmonth_dir, mtday_dir, mthour_dir, mtmin_dir, mtime, mdtime)


def get_mtime(directory):
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        # Use a dictionary key:value for filename/mtime
         = (f'{spacer}+ {path.name}')
        time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
        (datetime.fromtimestamp(time), file_path)
        # adding to a dict: mydict[key] = "value"




def make_tree(scopelevel, **kwargs):
    if not kwargs.get('od_now') or kwargs.get('od_mt'):
        raise noInput("No input given")
    
    if kwargs.get('od_now'):
        _od_now = kwargs.get('od_now')
        print("Creating Directories")
        Path(_od_now).mkdir(parents=True, exist_ok=True)
    

    return


def main():
    td_parser = argparse.ArgumentParser(description='Make a directory tree for year-month-day-hour-minute.')
    td_parser.add_argument('output_dir',
                           default=Path.cwd(),
                           help="Specify the base directory for the output."
                           )
    td_parser.add_argument('-v', '--verbose',
                           dest="verbose",
                           default=False,
                           action='store_true',
                           )
    td_parser.add_argument('-s', '--scope',
                           dest="scope",
                           choices=["year", "month", "day", "hour", "min"],
                           default="day",
                           help="Specify how deep to make the directory tree."
                           )
    td_parser.add_argument('-f', '--file',
                           dest="td_files",
                           help="Specify a file, directory, or comma-separated list" +
                                "to organize in a timedir tree by last modified time.",
                           nargs='*'
                           )

    # TODO: Act on a single file or comma-separated list
    # TODO: Move a directory of files to a timedir tree
    # TODO: Load a list from a file and move those files to a timedir tree

    td_args = td_parser.parse_args()
    output_dir = PurePath(td_args.output_dir)

    if td_args.scope == "year":
        scopelevel = 0

    elif td_args.scope == "month":
        scopelevel = 1

    elif td_args.scope == "day":
        scopelevel = 2

    elif td_args.scope == "hour":
        scopelevel = 3

    elif td_args.scope == "min":
        scopelevel = 4

    else:
        scopelevel = 2



    if 'td_args.td_files' in locals():
        mtimedir_ntuple = mtimedir(td_args.td_files, output_dir)
        make_tree(scopelevel, od_mt=)
    elif:
        timedir_ntuple = nowdir(output_dir)
        make_tree(scopelevel, od_now=timedir_ntuple)

    return


if __name__ == '__main__':
    try:
        main()
    except noInput as msg:
        print msg

