from sqlalchemy import Column, String, Integer
from database.base import Base, sessionFactory


class BarangORM(Base):
    __tablename__='barang'
    id_barang = Column(Integer, primary_key=True)
    nama_barang = Column(String)
    jumlah_barang = Column(String)
    harga_barang = Column(String)

    def __init__(self, nama_barang, jumlah_barang, harga_barang):
        self.nama_barang = nama_barang
        self.jumlah_barang = jumlah_barang
        self.harga_barang = harga_barang

    @staticmethod
    def insertBarang(self):
        try:
            session = sessionFactory()
            barang = BarangORM(self.nama_barang, self.__jumlah_barang, self.__harga_barang)
            session.add(barang)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Disimpan!")

    @staticmethod
    def dataBarang():
        session = sessionFactory()
        return session.query(BarangORM).all()
        session.close()


    @staticmethod
    def deleteBarang(id_barang):
        try:
            session = sessionFactory()
            session.query(BarangORM).filter_by(id_barang=id_barang).delete()
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data terlah terhapus!")

    @staticmethod
    def updateBarang(id_barang):
        try:
            newNama_produk = input("Masukkan Nama Produk : ")
            newJumlah_barang = input("Jumlah Barang : ")
            newHarga_barang = input("Harga Barang : ")
            session = sessionFactory()
            session.query(BarangORM).filter_by(id_barang=id_barang).update({
                BarangORM.jumlah_barang: newJumlah_barang, BarangORM.nama_produk: newNama_produk,
                BarangORM.harga_barang: newHarga_barang
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")


BarangORM.dataBarang()