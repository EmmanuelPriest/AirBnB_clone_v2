#!/usr/bin/python3

"""Defines the class DBStorage"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage:
    """Defines new engine class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the engine class DBStorage environ tables"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session of all objects
        depending of the class name
        """
        dictionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dictionary[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dictionary[key] = elem
        return dictionary

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        create_sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(create_sess)
        self.__session = Session()

    def close(self):
        """closes the sqlalchemy working session"""
        self.__session.close()
