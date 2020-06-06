from sqlalchemy import Column, String, Integer
from database.base import Base, sessionFactory, modelFactory


class GudangORM(Base):
    __tablename__='Gudang'

    id_barang = Column(Integer, primary_key=True)
    nama_produk = Column(String)
    jumlah_barang = Column(String)
    lokasi = Column(String)
    tanggal_masuk = Column(String)
    harga_barang = Column(String)

    def __init__(self, nama_produk, tanggal_masuk, lokasi, harga_barang, jumlah_barang):
        session = sessionFactory()
        self.nama_produk = nama_produk
        self.tanggal_masuk = tanggal_masuk
        self.lokasi = lokasi
        self.harga_barang = harga_barang
        self.jumlah_barang = jumlah_barang
        session.add(self)
        session.commit()
        session.close()

    def dataGudang():
        session = sessionFactory()
        return session.query(GudangORM).all()
        session.close()

    def delGudang(id):
        session = sessionFactory()
        session.query(GudangORM).filter_by(id_barang=id).delete()
        session.commit()
        session.close()


    def updateGudang(ID,newNama_produk, newTanggal_masuk, newLokasi, newHarga_barang, newJumlah_barang):
        session = sessionFactory()
        session.query(GudangORM).filter_by(id_barang=ID).update({
            GudangORM.nama_produk: newNama_produk,
            GudangORM.tanggal_masuk: newTanggal_masuk,
            GudangORM.lokasi: newLokasi,
            GudangORM.harga_barang: newHarga_barang,
            GudangORM.jumlah_barang: newJumlah_barang,
        }, synchronize_session=False)
        session.commit()
        session.close()
        pass

modelFactory()


