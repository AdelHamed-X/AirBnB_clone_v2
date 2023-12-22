#!/usr/bin/python3
""" This module represents the Database engine """
from sqlalchemy import create_engine
from os import environ

user = environ.get("HBNB_MYSQL_USER")
pwd = environ.get("HBNB_MYSQL_PWD")
host = environ.get("HBNB_MYSQL_HOST")
env = environ.get("HBNB_ENV")
db = environ.get("HBNB_MYSQL_DB")


class DBStorage:
    """ Database Storage Class """
    __engine = None
    __session= None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(environ['HBNB_MYSQL_USER'],
                                              environ['HBNB_MYSQL_PWD'],
                                              environ['HBNB_MYSQL_HOST'],
                                              environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True, echo=True)

        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """ Makes a query on the current database session """
        result_dict = {}
        classes = [User, State, City, Amenity, Place, Review]  # Add other classes as needed

        if cls is None:
            classes_to_query = classes
        else:
            classes_to_query = [cls]

        for class_obj in classes_to_query:
            objects = self.__session.query(class_obj).all()
            for obj in objects:
                key = f"{class_obj.__name__}.{obj.id}"
                result_dict[key] = obj

        return result_dict
    def new(self, obj):
        """
        Add the object to the current database session (self.__session).
        """
        if obj:
            self.__session.add(obj)
    def save(self):
        """
        Commit all changes of the current database session (self.__session).
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None.
        """
        if obj:
            self.__session.delete(obj)
    def reload(self):
        """
        Create all tables in the database (feature of SQLAlchemy).
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
