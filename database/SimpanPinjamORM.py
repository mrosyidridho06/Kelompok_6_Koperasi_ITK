from sqlalchemy import Column, String, Integer
from database.base import Base, sessionFactory, modelFactory

class SimpanPinjamORM(Base):
    __tablename__='SimpanPinjam'

    id_nasabah = Column(Integer, primary_key=True)
    nama_nasabah = Column(String)
    tanggal = Column(String)
    jumlah_simpan = Column(Integer)
    jumlah_pinjam = Column(Integer)

    def __init__(self, nama_nasabah, tanggal, jumlah_simpan, jumlah_pinjam):
        session = sessionFactory()
        self.nama_nasabah = nama_nasabah
        self.tanggal = tanggal
        self.jumlah_simpan = jumlah_simpan
        self.jumlah_pinjam = jumlah_pinjam
        session.add(self)
        session.commit()
        session.close()


    # @staticmethod
    # def insertSimpanPinjam(self):
    #     try:
    #         session = sessionFactory()
    #         simpanpinjam = SimpanPinjamORM(self.__tanggal, self.__jumlah_simpan,
    #                                        self.__jumlah_pinjam)
    #         session.add(simpanpinjam)
    #         session.commit()
    #         session.close()
    #     except Exception as e:
    #         print("===>", e)
    #     else:
    #         print("Data telah Disimpan!")


    def showSijam():
        session = sessionFactory()
        return session.query(SimpanPinjamORM).all()
        session.close()


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

# a=SimpanPinjamORM()
# a.insertSimpanPinjam("21/05/2000",10000,10000)
modelFactory()