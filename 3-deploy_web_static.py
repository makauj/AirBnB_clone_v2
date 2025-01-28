#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
using the function deploy
"""
from datetime import datetime
from fabric.api import local, put, run
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        archive = 'versions/web_static_{}.tgz'.format(date)
    
        if os.path.isdir("versions") is False:
            if local("mkdir -p versions").failed is True:
                return None

        if local(f'tar -cvzf {archive} web_static').failed is True:
            return None
        return archive
    except:
        return None

def do_deploy(archive):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive):
        return False

    try:
        # Get the name of the archive (without the .tgz extension)
        archive_name = archive.split("/")[-1]
        file_no_extension = archive_name.split('.')[0]
        upload_path = f"/tmp/{archive_name}"

        # Upload the archive to the web server /tmp/ directory
        put(archive, upload_path)

        # Create the release directory
        release_dir = f"/data/web_static/releases/{file_no_extension}"
        run(f"mkdir -p {release_dir}")

        # Uncompress the archive to the release directory
        run(f"tar -xzf {upload_path} -C {release_dir}/")

        # Remove the archive from the server
        run(f"rm {upload_path}")

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link pointing to the new release
        run(f"ln -s {release_dir} /data/web_static/current")

        return True
    except Exception:
        return False

def deploy():
    """
    Create and deploy an archive to the web servers.

    Returns:
    True if deployment is successful, False otherwise.
    """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
