#!/usr/bin/env python3
from fabric import Connection
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the versions directory if it does not exist
    os.makedirs("versions", exist_ok=True)

    # Generate archive name with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    # Create the archive using Fabric 3 syntax
    print(f"Packing web_static to {archive_name}")

    try:
        # Use Connection().run() to run a local command
        result = Connection("localhost").run(f"tar -cvzf {archive_name} web_static", hide=True)

        if result.ok:
            print(f"Archive created: {archive_name}")
            return archive_name
        else:
            print("Failed to create archive.")
            return None
    except Exception as e:
        print(f"Error during packaging: {e}")
        return None

