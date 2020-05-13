from sqlalchemy import Column, String, Integer
from database.base import Base, sessionFactory


class GudangORM(Base):
    __tablename__='gudangInt.py'

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

    @staticmethod
    def insertGudang(self):
        try:
            session = sessionFactory()
            gudang = GudangORM(self.__jumlah_barang, self.__lokasi, self.__tanggal_masuk, self.__harga_barang)
            session.add(gudang)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Disimpan!")

    @staticmethod
    def dataGudang():
        try:
            session = sessionFactory()
            for gudang in session.query(GudangORM).all():
                print(
                    "Id barang = {}\n Jumlah barang = {}\n Lokasi = {}\n Tanggal Masuk = {} \n Harga barang = {} \n===================="
                        .format(gudang.id_barang, gudang.jumlah_barang, gudang.lokasi, gudang.tanggal_masuk,
                                gudang.harga_barang))
            session.close()
        except Exception as e:
            print("===>", e)

    @staticmethod
    def deleteGudang(id_barang):
        try:
            session = sessionFactory()
            session.query(GudangORM).filter_by(id_barang=id_barang).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data terlah terhapus!")

    @staticmethod
    def updateGudang(id_barang):
        try:
            newJumlah_barang = input("Jumlah Barang : ")
            newLokasi = input("Lokasi : ")
            newTanggal_masuk = input("Tanggal Masuk : ")
            newHarga_barang = input("Harga Barang : ")
            session = sessionFactory()
            session.query(GudangORM).filter_by(id_barang=id_barang).update({
                GudangORM.jumlah_barang: newJumlah_barang, GudangORM.lokasi: newLokasi,
                GudangORM.tanggal_masuk: newTanggal_masuk, GudangORM.harga_barang: newHarga_barang
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")