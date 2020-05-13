from sqlalchemy import Column, String, Integer
from database.base import Base, sessionFactory


class BarangORM(Base):
    __tablename__='gudang'
    id_barang = Column(Integer, primary_key=True)
    nama_barang = Column(String)
    jumlah_barang = Column(String)
    lokasi = Column(String)
    tanggal_masuk = Column(String)
    harga_barang = Column(String)

    def __init__(self, nama_barang, jumlah_barang, lokasi, tanggal_masuk, harga_barang):
        self.nama_barang = nama_barang
        self.jumlah_barang = jumlah_barang
        self.lokasi = lokasi
        self.tanggal_masuk = tanggal_masuk
        self.harga_barang = harga_barang

    @staticmethod
    def insertBarang(self):
        try:
            session = sessionFactory()
            barang = BarangORM(self.nama_barang, self.__jumlah_barang, self.__lokasi, self.__tanggal_masuk, self.__harga_barang)
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
            newLokasi = input("Lokasi : ")
            newTanggal_masuk = input("Tanggal Masuk : ")
            newHarga_barang = input("Harga Barang : ")
            session = sessionFactory()
            session.query(BarangORM).filter_by(id_barang=id_barang).update({
                BarangORM.jumlah_barang: newJumlah_barang, BarangORM.nama_produk: newNama_produk, BarangORM.lokasi: newLokasi,
                BarangORM.tanggal_masuk: newTanggal_masuk, BarangORM.harga_barang: newHarga_barang
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")


BarangORM.dataBarang()