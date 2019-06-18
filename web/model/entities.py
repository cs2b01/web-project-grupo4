from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Client(connector.Manager.Base):
    __tablename__ = 'client'
    id = Column(Integer, Sequence('client_id_seq'), primary_key=True)
    username = Column(String(30))
    password = Column(String(30))
    name = Column(String(50))
    fullname = Column(String(50))
    phone = Column(String(20))
    address = Column(String(200))

class Provider(connector.Manager.Base):
    __tablename__ = 'provider'
    id = Column(Integer, Sequence('provider_id_seq'), primary_key=True)
    name_fullname = Column(String(60))
    email = Column(String(30))
    phone = Column(String(10))
    password = Column(String(15))
    name_restaurant = Column(String(30))
    num_mesas = Column(Integer)
    address = Column(String(50))
    slogan = Column(String(20))

class Restaurante(connector.Manager.Base):
    __tablename__ = 'restaurante'
    id = Column(Integer, Sequence('restaurante_id_seq'), primary_key=True)
    name_fullname = Column(String(60))
    username = Column(String(30))
    phone = Column(String(10))
    password = Column(String(15))
    name_restaurant = Column(String(30))
    num_mesas = Column(Integer)
    address = Column(String(50))
    slogan = Column(String(20))


class Menu(connector.Manager.Base):
    __tablename__ = 'menu'
    id = Column(Integer, Sequence('menu_id_seq'), primary_key=True)
    restaurant_id = Column(Integer)
    tipo_plato = Column(String(10))
    name = Column(String(30))
