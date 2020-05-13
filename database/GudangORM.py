from sqlalchemy import Column, String, Integer, Date
from database.base import Base, sessionFactory


class GudangORM(Base):
    __tablename__='gudang'
    id_barang = Column(Integer, primary_key=True)
    nama_produk = Column(String)
    jumlah_barang = Column(String)
    lokasi = Column(String)
    tanggal_masuk = Column(String)
    harga_barang = Column(String)

    def __init__(self, nama_produk, jumlah_barang, lokasi, tanggal_masuk, harga_barang):
        self.setWindowIcon(QtGui.QIcon('assets/img/icon.png'))
        self.nama_produk = nama_produk
        self.jumlah_barang = jumlah_barang
        self.lokasi = lokasi
        self.tanggal_masuk = tanggal_masuk
        self.harga_barang = harga_barang

    @staticmethod
    def insertGudang(self):
        try:
            session = sessionFactory()
            gudang = GudangORM(self.nama_produk, self.__jumlah_barang, self.__lokasi, self.__tanggal_masuk, self.__harga_barang)
            session.add(gudang)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Disimpan!")

    @staticmethod
    def dataGudang():
        session = sessionFactory()
        return session.query(GudangORM).all()
        session.close()


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
            newNama_produk = input("Masukkan Nama Produk : ")
            newJumlah_barang = input("Jumlah Barang : ")
            newLokasi = input("Lokasi : ")
            newTanggal_masuk = input("Tanggal Masuk : ")
            newHarga_barang = input("Harga Barang : ")
            session = sessionFactory()
            session.query(GudangORM).filter_by(id_barang=id_barang).update({
                GudangORM.jumlah_barang: newJumlah_barang, GudangORM.nama_produk: newNama_produk, GudangORM.lokasi: newLokasi,
                GudangORM.tanggal_masuk: newTanggal_masuk, GudangORM.harga_barang: newHarga_barang
            }, synchronize_session=False)
            session.commit()
            session.close()
        except Exception as e:
            print("===>", e)
        else:
            print("Data telah Terupdate!")


# for i in GudangORM.dataGudang():
#     print(i.nama_produk)

