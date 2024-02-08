#!/usr/bin/python3
""" This fabric script does the follwing stuff:
    - distributes an archive to my web servers """

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['54.174.144.6', '34.229.137.175']


def create_folder():
    """ creates versions folder """
    local("mkdir -p versions")


def file_name():
    current_date = datetime.utcnow()
    filename = "web_static_{}{}{}{}{}{}".format(current_date.year,
                                                current_date.month,
                                                current_date.day,
                                                current_date.hour,
                                                current_date.minute,
                                                current_date.second)
    return filename


def compress_all():
    """ creates an archive compressed file """
    local(f"tar -cvzf versions/{file_name()}.tgz web_static/*")


def do_pack():
    """ The main fuction """
    create_folder()
    compress_all()


def do_deploy(archive_path):
    """ distributes an archive to web servers """
    if not path.isfile(archive_path):
        return False
    
    uncompressed_file_name = local(f'basename {archive_path} .tgz')

    put(archive_path, '/tmp/')
    run(f'tar -xzf /tmp/{uncompressed_file_name}.tgz -C versions/{uncompressed_file_name}')
    run(f'rm -r /tmp/{uncompressed_file_name}.tgz')
    run(f'ln -sf /data/web_static/releases/{uncompressed_file_name} /data/web_static/current')