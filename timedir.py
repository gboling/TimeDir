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



# Make sure to return pathlib objects for all of these path builders.
def nowdir(od, sl):
    now = datetime.datetime.now()
    print(now)
    n_year = now.strftime('%Y')
    n_month = now.strftime('%m')
    n_day = now.strftime('%d')
    n_hour = now.strftime('%H')
    n_min = now.strftime('%M')
    if sl == 0:
        od_now = PurePath(od).joinpath(n_year)
    elif sl == 1:
        od_now = PurePath(od).joinpath(n_year, n_month)
    elif sl == 2:
        od_now = PurePath(od).joinpath(n_year, n_month, n_day)
    elif sl == 3:
        od_now = PurePath(od).joinpath(n_year, n_month, n_day, n_hour)
    elif sl == 4:
        od_now = PurePath(od).joinpath(n_year, n_month, n_day, n_hour, n_min)
    else:
        od_now = PurePath(od).joinpath(n_year, n_month, n_day)

    print(od_now)
    return od_now


def mtimedir(od, sl, mtf):
    mtime = os.path.getmtime(mtf)
    mdtime = datetime.datetime.fromtimestamp(mtime)
    m_year = mdtime.strftime('%Y')
    m_month = mdtime.strftime('%m')
    m_day = mdtime.strftime('%d')
    m_hour = mdtime.strftime('%H')
    m_min = mdtime.strftime('%M')
    if sl == 0:
        od_mt = PurePath(od).joinpath(m_year)
    elif sl == 1:
        od_mt = PurePath(od).joinpath(m_year, m_month)
    elif sl == 2:
        od_mt = PurePath(od).joinpath(m_year, m_month, m_day)
    elif sl == 3:
        od_mt = PurePath(od).joinpath(m_year, m_month, m_day, m_hour)
    elif sl == 4:
        od_mt = PurePath(od).joinpath(m_year, m_month, m_day, m_hour, m_min)
    else:
        od_mt = PurePath(od).joinpath(m_year, m_month, m_day)

    return od_mt


# def get_mtime(d):
#     filelist = Path(d).glob('*')
#
#     for path in sorted(d.rglob('*')):
#         depth = len(path.relative_to(d).parts)
#         # Use a dictionary key:value for filename/mtime
#          = (f'{spacer}+ {path.name}')
#         time, file_path = max((f.stat().st_mtime, f) for f in d.iterdir())
#         (datetime.fromtimestamp(time), file_path)
#         adding to a dict: mydict[key] = "value"


def make_tree(od):
    print("Creating Directories")
    Path(od).mkdir(parents=True, exist_ok=True)
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
    # TODO: Fill a directory tree with calendar for specified period of time
    # TODO: Require option for -f whether to copy or move

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
        output_dir_mt = mtimedir(output_dir, scopelevel, td_args.td_files)
        make_tree(output_dir_mt)
    else:
        output_dir_nd = nowdir(output_dir, scopelevel)
        make_tree(output_dir_nd)

    return


if __name__ == '__main__':
    main()