#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with your server IPs
env.user = 'ubuntu'  # SSH username
env.key_filename = '~/.ssh/id_rsa'  # SSH private key path


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers

    Args:
        archive_path: Path to the archive to deploy

    Returns:
        True if all operations were successful, False otherwise
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the server
        put(archive_path, '/tmp/')

        # Extract archive filename without extension
        archive_filename = archive_path.split('/')[-1]
        release_name = archive_filename.split('.')[0]
        release_path = f'/data/web_static/releases/{release_name}'

        # Create release directory
        run(f'mkdir -p {release_path}')

        # Uncompress the archive
        run(f'tar -xzf /tmp/{archive_filename} -C {release_path}')

        # Remove the archive from /tmp/
        run(f'rm /tmp/{archive_filename}')

        # Move contents to proper location
        run(f'mv {release_path}/web_static/* {release_path}/')
        run(f'rm -rf {release_path}/web_static')

        # Remove existing symlink
        run('rm -rf /data/web_static/current')

        # Create new symlink
        run(f'ln -s {release_path} /data/web_static/current')

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
