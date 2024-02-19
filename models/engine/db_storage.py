#!/usr/bin/python3
""" This module represents the Database engine """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import environ

from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.base_model import Base


class DBStorage:
    """ Database Storage Class """
    __engine = None
    __session= None

    def __init__(self):
        """ Instantiates new object """
        user = environ.get("HBNB_MYSQL_USER")
        pwd = environ.get("HBNB_MYSQL_PWD")
        host = environ.get("HBNB_MYSQL_HOST")
        env = environ.get("HBNB_ENV")
        db = environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Makes a query on the current database session """
        new_dict = {}
        all_classes = {"Amenity": Amenity, "City": City,
            "Place": Place, "Review": Review, "State": State, "User": User}
        if cls:
            result = self.__session.query(cls).all()
        else:
            result = []
            for clas in all_classes:
                result = self.__session.query(all_classes[clas]).all()
        for instance in result:
            key = f"{instance.__class__.__name__}.{instance.id}"
            new_dict[key] = instance
        return new_dict

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes to the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session 'obj' if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def close(self):
        """ Closes the current session """
        self.__session.close()
