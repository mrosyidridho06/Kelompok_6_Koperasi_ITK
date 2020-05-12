from base import sessionFactory
from SimpanPinjamORM import SimpanPinjamORM

class Simpanpinjam:
    def __init__(self, id_nasabah, tanggal, jumlah_simpan, jumlah_pinjam):
        self.__id_nasabah = id_nasabah
        self.__tanggal = tanggal
        self.__jumlah_simpan = jumlah_simpan
        self.__jumlah_pinjam = jumlah_pinjam

    @property
    def id_nasabah(self):
        return self.__id_nasabah

    @id_nasabah.setter
    def Id_nasabah(self, id):
        self.__id_nasabah = id
        
   @property
    def tanggal(self):
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, tanggal):
        self.__tanggal = tanggal

    @property
    def jumlah_simpan(self):
        return self.__jumlah_simpan
    
    @jumlah_simpan.setter
    def jumlah_simpan(self, jumlah_simpan):
        self.__jumlah_simpan = jumlah_simpan

    @property
    def jumlah_pinjam(self):
        return self.__jumlah_pinjam

    @jumlah_pinjam.setter
    def jumlah_pinjam(self, jumlah_pinjam):
        self.__jumlah_pinjam = jumlah_pinjam

    def insertSimpanPinjam(self):
            try:
                session = sessionFactory()
                simpanpinjam = SimpanPinjamORM(self.__id_nasabah, self.__tanggal, self.__jumlah_simpan, self.__jumlah_pinjam)
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
                        .format(simpanpinjam.id_nasabah, simpanpinjam.tanggal, simpanpinjam.jumlah_simpan, simpanpinjam.jumlah_pinjam))
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

x = Simpanpinjam(12, "15 feb 2020", 250000, 0)
#print(x)
x.insertSimpanPinjam()
#Simpanpinjam.deleteSimpanPinjam(2)
#Simpanpinjam.updateSimpanPinjam(2)
Simpanpinjam.DataSimpanPinjam()
