#!/usr/bin/python3
""" This fabric script does the follwing stuff:
    - Creates versions folder if it doesn't exist
    - Creates .tgz file of all the web_static folder components """

from fabric.api import local
from datetime import datetime


def creaets_folder():
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
    creaets_folder()
    compress_all()
