#!/usr/bin/python3
""" This fabric script does the follwing stuff:
    - Creates versions folder if it doesn't exist
    - Creates .tgz file of all the web_static folder components """

from fabric.api import local


def creaets_folder():
    """ creates versions folder """
    local("mkdir -p versions")


def file_name():
    return str(local("date +'%Y%m%%d%H%M%S'"))


def compress_all():
    """ creates an archive compressed file """
    local(f"tar -cvzf versions/archive.tgz web_static/*")
    file = "web_static_{}".format(file_name())
    local("mv versions/archive.tgz versions/{}".format(file))


def do_pack():
    """ The main fuction """
    creaets_folder()
    compress_all()
