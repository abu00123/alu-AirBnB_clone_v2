#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of the AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        # Create versions directory if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir -p versions")

        # Generate timestamp for the archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)

        # Create the .tgz archive
        print("Packing web_static to {}".format(archive_path))
        cmd = "tar -cvzf {} web_static".format(archive_path)
        result = local(cmd)

        # Check if the archive was created successfully
        if result.succeeded:
            size = os.path.getsize(archive_path)
            print("web_static packed: {} -> {}Bytes".
                  format(archive_path, size))
            return archive_path
        return None
    except Exception:
        return None
