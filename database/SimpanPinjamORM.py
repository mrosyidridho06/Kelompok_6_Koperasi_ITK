# from sqlalchemy import Column, String, Integer, Date
# from Class.simpanpinjam import simpanpinjam
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

    @staticmethod
    def insertSimpanPinjam(self):
        try:
            session = sessionFactory()
            simpanpinjam = SimpanPinjamORM(self.__id_nasabah, self.__tanggal, self.__jumlah_simpan,
                                           self.__jumlah_pinjam)
            session.add(simpanpinjam)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Disimpan!")

    @staticmethod
    def DataSimpanPinjam():
        try:
            session = sessionFactory()
            for simpanpinjam in session.query(SimpanPinjamORM).all():
                print(
                    "Id nasabah = {}\nTanggal = {}\nJumlah Simpanan = {}\nJumlah Pinjaman = {}\n===================="
                        .format(simpanpinjam.id_nasabah, simpanpinjam.tanggal, simpanpinjam.jumlah_simpan,
                                simpanpinjam.jumlah_pinjam))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def deleteSimpanPinjam(id_nasabah):
        try:
            session = sessionFactory()
            session.query(SimpanPinjamORM).filter_by(id_nasabah=id_nasabah).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data terlah terhapus!")

    @staticmethod
    def updateSimpanPinjam(id_nasabah):
        try:
            newIdNasabah = input("Id Nasabah : ")
            newTanggal = input("Tanggal : ")
            newSimpan = input("Simpanan : ")
            newPinjam = input("Pinjaman : ")
            session = sessionFactory()
            session.query(SimpanPinjamORM).filter_by(id_nasabah=id_nasabah).update({
                SimpanPinjamORM.id_nasabah: newIdNasabah, SimpanPinjamORM.tanggal: newTanggal,
                SimpanPinjamORM.jumlah_simpan: newSimpan, SimpanPinjamORM.jumlah_pinjam: newPinjam
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")
