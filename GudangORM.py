from sqlalchemy import Column, String, Integer
from base import Base, sessionFactory

class GudangORM(Base):
    __tablename__='gudang'

    id_barang = Column(Integer, primary_key=True)
    jumlah_barang = Column(String)
    lokasi = Column(String)
    tanggal_masuk = Column(String)
    harga_barang = Column(String)

    def __init__(self, jumlah_barang, lokasi, tanggal_masuk, harga_barang):
        self.jumlah_barang = jumlah_barang
        self.lokasi = lokasi
        self.tanggal_masuk = tanggal_masuk
        self.harga_barang = harga_barang