from sqlalchemy import Column, String, Integer
from database.base import Base, sessionFactory, modelFactory

class SimpanPinjamORM(Base):
    __tablename__='SimpanPinjam'

    id_nasabah = Column(Integer, primary_key=True)
    nama_nasabah = Column(String)
    tanggal = Column(String)
    jumlah_simpan = Column(String)
    jumlah_pinjam = Column(String)

    def __init__(self, nama_nasabah, tanggal, jumlah_simpan, jumlah_pinjam):
        session = sessionFactory()
        self.nama_nasabah = nama_nasabah
        self.tanggal = tanggal
        self.jumlah_simpan = jumlah_simpan
        self.jumlah_pinjam = jumlah_pinjam
        session.add(self)
        session.commit()
        session.close()


    def dataSijam():
        session = sessionFactory()
        return session.query(SimpanPinjamORM).all()
        session.close()



    def delSijam(id):
        session = sessionFactory()
        session.query(SimpanPinjamORM).filter_by(id_nasabah=id).delete()
        session.commit()
        session.close()

    def updateSimpanPinjam(ID, newNama, newTanggal, newSimpan, newPinjam):
        session = sessionFactory()
        session.query(SimpanPinjamORM).filter_by(id_nasabah=ID).update({
            SimpanPinjamORM.nama_nasabah: newNama,
            SimpanPinjamORM.tanggal: newTanggal,
            SimpanPinjamORM.jumlah_simpan: newSimpan,
            SimpanPinjamORM.jumlah_pinjam: newPinjam
        }, synchronize_session=False)
        session.commit()
        session.close()
        pass


modelFactory()