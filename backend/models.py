from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Producto(Base):
  __tablename__ = "producto"
  id = Column(Integer, primary_key=True, index=True)
  referencia = Column(Integer)
  descripcion = Column(String)
  condicion = Column(String)
  precio = Column(Integer)
