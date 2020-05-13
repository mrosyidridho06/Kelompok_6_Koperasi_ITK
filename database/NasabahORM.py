from sqlalchemy import Column, String, Integer, Text
from database.base import Base, sessionFactory
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

    #CRUD
    @staticmethod
    def insertNasabah(self):
        try:
            session = sessionFactory()
            nasabah = NasabahORM(self.__nama_nasabah, self.__alamat, self.__no_telp)
            session.add(nasabah)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Disimpan!")

    @staticmethod
    def DataNasabah():
        try:
            session = sessionFactory()
            for nasabah in session.query(NasabahORM).all():
                print(
                    "Id nasabah = {}\nNama = {}\nAlamat = {}\nNo Telp = {}\n===================="
                        .format(nasabah.id_nasabah, nasabah.nama_nasabah, nasabah.alamat, nasabah.no_telp))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def deleteNasabah(id_nasabah):
        try:
            session = sessionFactory()
            session.query(NasabahORM).filter_by(id_nasabah=id_nasabah).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data terlah terhapus!")

    @staticmethod
    def updateNasabah(id_nasabah):
        try:
            newNama = input("Nama Nasabah : ")
            newAlamat = input("Alamat Nasabah : ")
            newNotelp = input("No Telp Nasabah: ")
            session = sessionFactory()
            session.query(NasabahORM).filter_by(id_nasabah=id_nasabah).update({
                NasabahORM.nama_nasabah: newNama, NasabahORM.alamat: newAlamat,
                NasabahORM.no_telp: newNotelp
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")

