# timedir

A Python app which will produce a directory tree in this format:
`output_dir/year/month/day/hour/min`
---
EXAMPLES:

Create a new directory: ./foo/bar/$CurrentYear

`timedir -s year foo/bar`

---

If `/baz` is a file, moves it to `/foo/bar/[year]/[month]/[day]` based on last modified time of `baz`. If `/baz` is a
directory, moves contents based on each file's last modified time.

`timedir -f /baz /foo/bar`

---

by J. Grant Boling [gboling]at[gmail]dot[com]