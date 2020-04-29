# from sqlalchemy import Column, String, Integer, Date
# from class.simpanpinjam import simpanpinjam
# from database import base

from sqlalchemy import Column, String, Integer, Text
from base import Base, sessionFactory
#from Class.HakAkses import HakAkses

class SimpanPinjamORM(base):
    __tablename__='SimpanPinjam'

    id_nasabah = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    jumlah_simpan = Column(Integer)
    jumlah_pinjam = Column(Integer)

    def __init__(self, id_nasabah, tanggal, jumlah_simpan, jumlah_pinjam):
        self.id_nasabah= id_nasabah
        self.tanggal = tanggal
        self.jumlah_simpan = jumlah_simpan
        self.jumlah_pinjam = jumlah_pinjam
        
#sessionFactory()
