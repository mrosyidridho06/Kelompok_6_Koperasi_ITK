from sqlalchemy import Column, String, Integer, Date
from class.simpanpinjam import simpanpinjam
from database import base

class SimpanpinjamORM(base):
    __tablename__='SimpanPinjam'

    id_nasabah = Column(Integer, primary_key=True)
    tanggal = Column(Date)
    jumlah_simpan = Column(Integer)
    jumlah_pinjam = Column(Integer)

    def __init__(self, id_nasabah, tanggal, jumlah_simpan, jumlah_pinjam):
        self.__id_nasabah= id_nasabah
        self.__tanggal = tanggal
        self.__jumlah_simpan = jumlah_simpan
        self.__jumlah_pinjam = jumlah_pinjam
