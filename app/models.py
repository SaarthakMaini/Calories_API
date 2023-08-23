from sqlalchemy import Column,Integer,String,Boolean
from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer,primary_key=True,nullable=False)
    username = Column(String,nullable=False,unique=True)
    user_email = Column(String,nullable=False,unique=True) 
    password = Column(String,nullable=False)