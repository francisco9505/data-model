import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True)
        username = Column(String(250))
        firstname = Column(String(250))
        lastname =Column(String(250))
        email = Column(String(250))


class Post(Base):
        __tablename__ = 'post'
        id = Colum(Integer, primary_key=True)
        user_id = Colum(Integer, ForeignKey('User.id'))

        
       

class Comment(Base):
        __tablename__ = 'Comment'
        id = Column(Integer, primary_key=True)
        comment_text = Column(String(250))
        author_id = Column (Integer, ForeignKey('User.id'))
        post_id = Column (Integer,ForeignKey('Post.id'))

class Media(Base):
        __tablename__ = 'Media'
        id = Column(Integer, primary_key=True)
        type = Column(String(250))
        url = Column(String(250))
        post_id = (Integer,ForeignKey('Post.id'))

class Follower(Base):
        __tablename__ = 'follower'
        id = Column(Integer, primary_key=True)
        user_from_id(Integer,ForeignKey('User.id'))
        user_to_id(Integer,ForeignKey('User.id'))


def to_dict(self):
        return {}



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
