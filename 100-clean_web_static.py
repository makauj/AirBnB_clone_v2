#!/user/bin/python3
"""Fabric script that deletes out-of-date archives,
using the function do_clean
"""
from fabric.api import local, put, run, lcd
import os


def do_clean(number=0):
    """
    Deletes out-of-date archives, keeping only the most recent `number` of archives.
    
    Arguments:
    number -- The number of archives to keep, including the most recent.
              If 0 or 1, keeps only the most recent archive.
              If 2, keeps the most recent and the previous archive.
    """
    number = 1 if int(number) == 0 else int(number)
    files = sorted(os.listdir("versions"))
    for file in files[:-number]:
        local("rm versions/{}".format(file))
    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
