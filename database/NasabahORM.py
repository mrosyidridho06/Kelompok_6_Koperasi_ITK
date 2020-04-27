from sqlalchemy import Column, String, Integer, Text
from base import Base, sessionFactory
#from Class.HakAkses import HakAkses


class NasabahORM(Base):
    __tablename__ = 'nasabah'

    id_nasabah = Column(Integer, primary_key=True)
    nama_nasabah = Column(String)
    alamat = Column(String)
    no_telp = Column(String)
    

    def __init__(self, nama, alamat, noTelp ):
        self.nama_nasabah = nama
        self.alamat = alamat
        self.no_telp = noTelp
      