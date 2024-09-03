from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from app.database import engine
from app import models

#create tables
models.Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    credentials = relationship('Credential', back_populates='owner')


class Credential(Base):
    __tablename__ = 'credentials'

    id =  Column(Integer, primary_key=True, index=True)
    service_name = Column(String, index=True)
    encrypted_username = Column(String)
    encrypted_password = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('user', back_populates='credentials')
