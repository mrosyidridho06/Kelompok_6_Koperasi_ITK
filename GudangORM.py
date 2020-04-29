from sqlalchemy import Column, String, Integer, Date
from base import Base

class GudangORM(Base):
    __tablename__='gudang'
    id_barang = Column(Integer, primary_key=True)
    jumlah_barang = Column(Integer)
    lokasi = Column(String(32))
    tanggal_masuk = Column(Date)
    harga_barang = Column(Integer)

    def __init__(self, id_barang, jumlah_barang, lokasi, tanggal_masuk, harga_barang):
        self.__id_barang = id_barang
        self.__jumlah_barang = jumlah_barang
        self.__lokasi = lokasi
        self.__tanggal_masuk = tanggal_masuk
        self.__harga_barang = harga_barang