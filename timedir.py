#!/usr/bin/env python

"""
    To make a directory tree like this: output_dir/year/month/day/hour/min
    Also get mtime of an arbitrary file and returns namedtuple for datetime and elements.
    Returns a namedtuple with values for each level at time of function call.

    Copyright (C) 2016 J. Grant Boling [gboling]at[gmail]dot[com]

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import datetime
import os
import argparse

from collections import namedtuple

timedir_ntuple = namedtuple('timedir', 'yearDir monthDir dayDir hourDir minDir')
mtimedir_ntuple = namedtuple('mtimedir', 'yearDir monthDir dayDir hourDir minDir mtime mdtime')


def nowdir(output_dir, scopelevel):
    now = datetime.datetime.now()
    n_year = now.strftime('%Y')
    n_month = now.strftime('%m')
    n_day = now.strftime('%d')
    n_hour = now.strftime('%H')
    n_min = now.strftime('%M')
    year_dir = os.path.join(output_dir, n_year)
    month_dir = os.path.join(year_dir, n_month)
    day_dir = os.path.join(month_dir, n_day)
    hour_dir = os.path.join(day_dir, n_hour)
    min_dir = os.path.join(hour_dir, n_min)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(year_dir) and scopelevel >= 0:
        os.mkdir(year_dir)

    if not os.path.exists(month_dir) and scopelevel >= 1:
        os.mkdir(month_dir)

    if not os.path.exists(day_dir) and scopelevel >= 2:
        os.mkdir(day_dir)

    if not os.path.exists(hour_dir) and scopelevel >= 3:
        os.mkdir(hour_dir)

    if not os.path.exists(min_dir) and scopelevel == 4:
        os.mkdir(min_dir)

    return timedir_ntuple(year_dir, month_dir, day_dir, hour_dir, min_dir)


def mtimedir(mtime_file, mtoutput_dir):
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


def main():
    td_parser = argparse.ArgumentParser(description='Make a directory tree for year-month-day-hour-minute.')
    td_parser.add_argument('output_dir',
                           default=os.getcwd(),
                           help="Specify the base directory."
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

    td_args = td_parser.parse_args()
    output_dir = td_args.output_dir

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

    nowdir(output_dir, scopelevel)


if __name__ == '__main__':
    main()
