#!/user/bin/python3
""" Fabric script that generates a .tgz archive """
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
