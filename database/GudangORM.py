from sqlalchemy import Column, String, Integer, Date
from class.gudang import gudang
from database import base

class GudangORM(base):
    __tablename__='Gudang'
    id = Column(Integer, primary_key=True)
    jumlah_produk = Column(Integer)
    lokasi = Column(String(32))
    tanggal_masuk = Column(Date)
    harga_produk = Column(Integer)

    def __init__(self, id_produk, jumlah_produk, lokasi, tanggal_masuk, harga_produk):
        self.__id_produk = id_produk
        self.__jumlah_produk = jumlah_produk
        self.__lokasi = lokasi
        self.__tanggal_masuk = tanggal_masuk
        self.__harga_produk = harga_produk