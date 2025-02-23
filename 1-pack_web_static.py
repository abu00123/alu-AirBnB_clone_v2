#!/usr/bin/env python3

from fabric.operations import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it does not exist
    os.makedirs("versions", exist_ok=True)
    
    # Generate archive name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    
    # Create the archive
    print(f"Packing web_static to {archive_name}")
    result = local(f"tar -cvzf {archive_name} web_static", capture=True)
    
    # Return the archive path if successful, otherwise return None
    return archive_name if result.succeeded else None

