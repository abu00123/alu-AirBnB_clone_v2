from datetime import datetime
import os
import subprocess

def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.
    """
    # Create the versions directory if it does not exist
    if not os.path.exists("versions"):
        os.makedirs("versions")
    
    # Generate the archive name using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    
    # Create the archive using tar
    print(f"Packing web_static to {archive_name}")
    try:
        result = subprocess.run(["tar", "-cvzf", archive_name, "web_static"], check=True)
    except subprocess.CalledProcessError:
        return None
    
    return archive_name

