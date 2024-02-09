#!/usr/bin/python3
""" This fabric script does the follwing stuff:
    - distributes an archive to my web servers """

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['ubuntu@54.174.144.6', 'ubuntu@34.229.137.175']
env.key_filename = ['~/.ssh/id_rsa']


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

    remote_name = local('basename {} .tgz'.format(archive_path))
    remote_file = "{}.tgz".format(remote_name)

    if put(archive_path, '/tmp/{}'.format(remote_file)).failed ==  True:
        return False
    if run("mkdir -p /data/web_static/releases/{}".format(remote_name)).failed == True:
        return False
    if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(remote_file, remote_name)).failed ==  True:
        return False
    if run('rm -r /tmp/{}'.format(remote_file)).failed == True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(remote_name, remote_name)).failed == True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(remote_name)).failed == True:
        return False
    if run("rm -rf /data/web_static/current").failed == True:
        return False
    if run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.format(remote_name)).failed == True:
        return False
    return True
