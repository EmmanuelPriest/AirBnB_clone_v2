#!/usr/bin/python3
"""
Fabric script that distributes an archive to my webservers using do_deploy()
"""
import os
from fabric.api import *
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ['54.90.13.5', '18.207.139.113']


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    filename_without_extension = os.path.splitext(filename)[0]
    release_folder = '/data/web_static/releases/' + filename_without_extension
    release_folder_exists = run('ls {}'.format(release_folder))

    if release_folder_exists.succeeded:
        return False

    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(release_folder))
    run('tar -xzf /tmp/{} -C {}'.format(filename, release_folder))
    run('rm /tmp/{}'.format(filename))
    run('rm -f /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(release_folder))

    return True
