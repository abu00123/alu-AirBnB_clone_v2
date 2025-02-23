from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the versions directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Generate the archive name using the current date and time
        now = datetime.now()
        archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

        # Create the archive using the tar command
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path to the archive if successful
        return "versions/{}".format(archive_name)
    except Exception as e:
        # Return None if any error occurs
        return None
