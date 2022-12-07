#!/usr/bin/python3

"""Defines the class DBStorage"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.place import place_amenity

classes = {"User": User, "State": State, "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}


class DBStorage:
    """Defines new engine class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the engine class DBStorage"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session of all objects
        depending of the class name
        """
        dictionary = {}
        if cls is None:
            for all_obj in classes.value():
                all_objects = self.__session.query(all_obj).all()
                for object in all_objects:
                    key = object.__class__.__name__ + "." + object.id
                    dictionary[key] = object
        else:
            all_objects = self.__session.query(cls).all()
            for object in all_objects:
                key = object.__class__.__name__ + "." + object.id
                dictionary[key] = object
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as exp:
                self.__session.rollback()
                raise exp

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.query(type(obj)).filter(type(obj).id == obj.id).
            delete()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        create_sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(create_sess)()

    def close(self):
        """closes the sqlalchemy working session"""
        self.__session.close()
