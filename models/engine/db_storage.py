#!/usr/bin/python3
"""new database storage engine"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User



class DBStorage(__engine=None, __session=None):
    """SQL database storage"""
    def __init__(self):
        """initialize the engine"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getemv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        environ = os.getenv("HBNB_ENV", "none")
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db), pool_pre_ping=True)
        
        if environ == 'test':
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """query on the current database session"""
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for element in query:
                key = f"{type(element.__name__)}.{element.id}"
                dic[key] = element
        return dic
    
    def new(self, obj):
        """add an object to the current database"""
        self.__session.add(obj)
    
    def save(self):
        """Save all changes to the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete object from current database"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """recreate current database session using sessionmaker"""
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()
    
    def close(self):
        """close session"""
        self.__session.close()
