#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import local
from os import path
import time

def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.
    The archive is saved to the versions directory.
    The name of the archive is formatted as
    `web_static_<year><month><day><hour><minute><second>.tgz.`
    Returns the archive path if successful, otherwise returns None.
    """
    try:
        local("mkdir -p versions")
        archive = "versions/web_static_{}.tgz".format(
            time.strftime("%Y%m%d%H%M%S", time.gmtime()))
        local("tar -cvzf {} web_static".format(archive))
        if path.exists(archive):
            return archive
        return None
    except:
        return None
