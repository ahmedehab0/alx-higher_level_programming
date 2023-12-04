#!/usr/bin/python3
"""model defining state class"""


from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    __tablename__ : name of the table
    id = (int) represents a column of an auto generated, uniqe integer
    name = (string) represents a column of a string
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
    name = Column(String(128), nullable = False)
